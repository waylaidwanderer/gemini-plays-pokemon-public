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
    print("=== NAVIGATING TO GATEHOUSE (V2) ===")
    pos = get_pos()
    print("Starting position:", pos)
    
    # We are at (33, 28) in Fuchsia City.
    # Route:
    # 1. Walk Left to Column 31 -> (31, 28) (2 steps Left)
    # 2. Walk Down to Row 30 -> (31, 30) (2 steps Down)
    # 3. Walk Right to Column 35 -> (35, 30) (4 steps Right)
    # 4. Walk Up Column 35 to Row 14 -> (35, 14) (16 steps Up)
    # 5. Walk Left along Row 14 to Column 23 -> (23, 14) (12 steps Left)
    # 6. Walk Up Column 23 to Row 2 -> (23, 2) (12 steps Up)
    # 7. Walk Left along Row 2 to Column 18 -> (18, 2) (5 steps Left)
    # 8. Walk Down 1 step to enter Gatehouse -> (18, 3) (1 step Down)
    path = (
        ["Left"] * 2 +
        ["Down"] * 2 +
        ["Right"] * 4 +
        ["Up"] * 16 +
        ["Left"] * 12 +
        ["Up"] * 12 +
        ["Left"] * 5 +
        ["Down"]
    )
    
    if run_path(path):
        print("Successfully reached and entered Safari Zone Gatehouse!")
        time.sleep(1.0)
        print("Final Position:", get_pos())
    else:
        print("Failed to reach Safari Zone Gatehouse!")

if __name__ == "__main__":
    main()
