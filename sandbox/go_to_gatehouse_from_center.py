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

def run_path(path, check_warp=False):
    idx = 0
    stuck_count = 0
    while idx < len(path):
        pos = get_pos()
        if pos is None:
            if check_warp:
                print("Transition occurred (pos is None)!")
                return True
            time.sleep(0.5)
            continue
            
        print(f"Step {idx}: At {pos}, walking {path[idx]}...")
        new_pos = walk_step_robust(path[idx])
        
        if new_pos is None:
            time.sleep(0.5)
            new_pos = get_pos()
            if new_pos is None:
                if check_warp:
                    print("Transition occurred (pos is None after retry)!")
                    return True
                continue
                
        if new_pos == pos:
            stuck_count += 1
            if stuck_count > 3:
                print(f"Blocked at {pos}! Exiting path.")
                return False
        else:
            stuck_count = 0
            if check_warp:
                dist = abs(new_pos[0] - pos[0]) + abs(new_pos[1] - pos[1])
                if dist > 5:
                    print(f"Transition occurred! New pos: {new_pos}")
                    break
            idx += 1
    return True

def main():
    print("=== EXECUTING detoured path around NPC at (24, 8) ===")
    
    pos = get_pos()
    print("Initial position:", pos)
    if pos != (23, 8):
        print("Not at starting position (23, 8)!")
        return
        
    # Detour around NPC at (24, 8):
    # 1. Walk Down 1 step to (23, 9)
    # 2. Walk Right 3 steps to (26, 9)
    # 3. Walk Up 1 step to (26, 8)
    # 4. Walk Right 11 steps to (37, 8)
    # 5. Walk Up 6 steps to (37, 2)
    # 6. Walk Left 19 steps to (18, 2)
    # 7. Walk Down 1 step to enter the Gatehouse at (18, 3) (Gatehouse warp)
    detour_path = (
        ["Down"] * 1 +
        ["Right"] * 3 +
        ["Up"] * 1 +
        ["Right"] * 11 +
        ["Up"] * 6 +
        ["Left"] * 19 +
        ["Down"]
    )
    
    if run_path(detour_path, check_warp=True):
        print("Successfully reached Safari Zone Gatehouse!")
        time.sleep(1.0)
        pos = get_pos()
        print("Inside Gatehouse position:", pos)
    else:
        print("Failed to reach Safari Zone Gatehouse from detour!")

if __name__ == "__main__":
    main()
