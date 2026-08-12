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
        new_pos = walk_step_robust(path[idx])
        
        if new_pos is None:
            time.sleep(0.5)
            continue
            
        if new_pos == pos:
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
    print("=== EXECUTING SAFE DETOUR ROUTE TO WARDEN'S HOUSE V8 ===")
    
    pos = get_pos()
    print("Initial position:", pos)
    if pos is None:
        print("Failed to get starting position!")
        return
        
    if pos == (23, 8):
        # Walk Down to Row 9, Right to Column 26 to bypass the NPC at (24, 8),
        # then Up to Row 8, Right to Column 37, Down Column 37 to Row 27,
        # Left to Column 27, and Up to enter Warden's House
        path = (
            ["Down"] +                                                        # to (23, 9)
            ["Right"] * 3 +                                                   # to (26, 9)
            ["Up"] +                                                          # to (26, 8)
            ["Right"] * 11 +                                                  # to (37, 8)
            ["Down"] * 19 +                                                   # to (37, 27)
            ["Left"] * 10 +                                                   # to (27, 27)
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
