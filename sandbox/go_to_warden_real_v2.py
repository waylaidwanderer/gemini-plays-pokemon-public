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
        
        # Ledge jump check
        is_ledge_jump = (pos == (23, 22) and path[idx] == "Down")
        
        new_pos = walk_step_robust(path[idx])
        
        if new_pos is None:
            time.sleep(0.5)
            continue
            
        expected_change = (new_pos != pos)
        if is_ledge_jump:
            # If we jumped the ledge down, coordinate y goes from 22 to 24 (since ledge takes 2 steps or coordinate change is 24)
            expected_change = (new_pos[1] > pos[1])
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
    print("=== EXECUTING SAFE PATH FROM (26, 15) TO WARDEN'S HOUSE ===")
    
    pos = get_pos()
    print("Initial position:", pos)
    if pos is None:
        print("Failed to get starting position!")
        return
        
    if pos == (26, 15):
        # 1. Walk Up to Row 14
        # 2. Walk Left to Column 23
        # 3. Walk Down Column 23 to Row 22
        # 4. Jump down ledge to Row 23/24
        # 5. Walk Down to Row 27
        # 6. Walk Right to Column 27 (Warden's House door)
        # 7. Walk Up to enter
        path = (
            ["Up"] +                                                          # to (26, 14)
            ["Left"] * 3 +                                                    # to (23, 14)
            ["Down"] * 8 +                                                    # to (23, 22)
            ["Down"] +                                                        # Ledge jump to (23, 24)
            ["Down"] * 3 +                                                    # to (23, 27)
            ["Right"] * 4 +                                                   # to (27, 27)
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
