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
    print("=== PROBING COLUMN 15 WALKABILITY TO ROW 9 ===")
    
    pos = get_pos()
    print("Initial position:", pos)
    if pos is None:
        return
        
    # Walk to Column 15 on Row 18, then try to walk Up to Row 9
    path = []
    if pos == (13, 18):
        path.extend(["Right", "Right"]) # to (15, 18)
    
    path.extend(["Up"] * 9) # to (15, 9)
    
    if run_path(path):
        print("Successfully reached (15, 9)!")
    else:
        print("Failed to reach (15, 9)!")

if __name__ == "__main__":
    main()
