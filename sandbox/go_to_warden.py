import bridge
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    for _ in range(4):
        pos = bridge.get_coordinates()
        if pos is not None:
            return pos[0], pos[1]
        time.sleep(0.1)
    return None

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        return None
        
    bridge.press_buttons([direction])
    
    # Wait for position to change
    for _ in range(5):
        time.sleep(0.15)
        new_pos = get_pos()
        if new_pos is not None and new_pos != pos:
            return new_pos
            
    print(f"Bumping/stuck at {pos} walking {direction}!")
    return pos

def run_path(path):
    idx = 0
    stuck_count = 0
    while idx < len(path):
        pos = get_pos()
        if pos is None:
            time.sleep(0.5)
            continue
            
        print(f"Step {idx}: At {pos}, walking {path[idx]}...")
        
        # Handle ledge jump specially: if we are at (22, 22) and walk Down, coordinate changes by 2
        is_ledge_jump = (pos == (22, 22) and path[idx] == "Down")
        
        new_pos = walk_step_robust(path[idx])
        
        if new_pos is None:
            time.sleep(0.5)
            continue
            
        # Verify movement
        expected_change = (new_pos != pos)
        if is_ledge_jump:
            # For ledge jump, coordinate must change
            expected_change = (new_pos == (22, 24))
            if expected_change:
                print("Ledge jump successful!")
                
        if not expected_change:
            stuck_count += 1
            print(f"Stuck at {pos}! Stuck count: {stuck_count}")
            if stuck_count > 3:
                print("Path blocked. Exiting path.")
                return False
        else:
            stuck_count = 0
            idx += 1
    return True

def main():
    print("=== EXECUTING SAFE DETOUR ROUTE TO WARDEN'S HOUSE ===")
    
    pos = get_pos()
    print("Initial position:", pos)
    if pos is None:
        print("Failed to get starting position!")
        return
        
    if pos == (22, 4):
        # Walk Down Column 22 to Row 12, detour left to Column 21 to bypass (22, 13) door,
        # return to Column 22 Row 14, walk down to ledge at Row 22, jump ledge, and walk to Warden's House
        path = (
            ["Down"] * 8 +                                                    # to (22, 12)
            ["Left"] +                                                        # to (21, 12)
            ["Down"] * 2 +                                                    # to (21, 14)
            ["Right"] +                                                       # to (22, 14)
            ["Down"] * 8 +                                                    # to (22, 22)
            ["Down"] * 4 +                                                    # to (22, 27) (including ledge jump)
            ["Right"] * 5 +                                                   # to (27, 27)
            ["Up"]                                                            # Enter Warden's House!
        )
        print("Walking to Warden's House...")
        if run_path(path):
            print("Successfully reached and entered Warden's House!")
            time.sleep(1.0)
            print("Final Position:", get_pos())
        else:
            print("Failed to reach Warden's House!")

if __name__ == "__main__":
    main()
