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
                print("Path blocked!")
                return False
        else:
            stuck_count = 0
            idx += 1
    return True

def main():
    print("=== WALKING NORTH ROUTE TO WARDEN'S HOUSE ===")
    pos = get_pos()
    print("Starting position:", pos)
    
    # We are at (18, 6) in Fuchsia City.
    # Route:
    # 1. Walk Right along Row 6 from Column 18 to Column 37 (19 steps Right) -> (37, 6)
    # 2. Walk Down Column 37 from Row 6 to Row 27 (21 steps Down) -> (37, 27)
    # 3. Walk Left along Row 27 to Column 27 (10 steps Left) -> (27, 27)
    # 4. Walk Up to enter Warden's House!
    path = (
        ["Right"] * 19 +
        ["Down"] * 21 +
        ["Left"] * 10 +
        ["Up"]
    )
    
    if run_path(path):
        print("Successfully reached and entered Warden's House!")
        time.sleep(1.0)
        print("Final Position:", get_pos())
    else:
        print("Failed to reach Warden's House!")

if __name__ == "__main__":
    main()
