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
            
        if new_p := (new_pos != pos):
            stuck_count = 0
            idx += 1
        else:
            stuck_count += 1
            print(f"Stuck at {pos}! Stuck count: {stuck_count}")
            if stuck_count > 3:
                print("Path blocked. Exiting path.")
                return False
    return True

def main():
    print("=== EXECUTING DETOUR ROUTE V3 TO WARDEN'S HOUSE ===")
    
    pos = get_pos()
    print("Initial position:", pos)
    if pos is None:
        print("Failed to get starting position!")
        return
        
    if pos == (24, 26):
        # Path:
        # 1. Down 4 times to (24, 30)
        # 2. Right 6 times to (30, 30)
        # 3. Up 2 times to (30, 28)
        # 4. Left 3 times to (27, 28)
        # 5. Up 1 time to (27, 27) (Enter Warden's House)
        path = (
            ["Down"] * 4 +
            ["Right"] * 6 +
            ["Up"] * 2 +
            ["Left"] * 3 +
            ["Up"]
        )
        print("Walking detour path...")
        if run_path(path):
            print("Successfully reached and entered Warden's House!")
            time.sleep(1.0)
            print("Final Position:", get_pos())
        else:
            print("Failed to reach Warden's House!")

if __name__ == "__main__":
    main()
