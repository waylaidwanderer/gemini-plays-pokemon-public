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
    print("=== WALKING DIRECT ROUTE TO WARDEN'S HOUSE FROM (31, 14) ===")
    pos = get_pos()
    print("Starting position:", pos)
    
    # We are at (31, 14) in Fuchsia City.
    # Route:
    # 1. Walk Down 2 to Row 16 -> (31, 16)
    # 2. Walk Left to Column 26 -> (26, 16) (5 steps Left)
    # 3. Walk Down Column 26 to Row 27 -> (26, 27) (11 steps Down)
    # 4. Walk Right to Column 27 -> (27, 27) (1 step Right)
    # 5. Walk Up to enter Warden's House!
    path = (
        ["Down"] * 2 +
        ["Left"] * 5 +
        ["Down"] * 11 +
        ["Right"] +
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
