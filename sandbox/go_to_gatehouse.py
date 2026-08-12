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
    print("=== NAVIGATING TO SAFARI ZONE GATEHOUSE FROM WARDEN'S ===")
    pos = get_pos()
    print("Starting position:", pos)
    
    # We are at (27, 28) outside the Warden's House.
    # Route:
    # 1. Walk Right along Row 28 from Column 27 to Column 37 -> (37, 28) (10 steps Right)
    # 2. Walk Up Column 37 from Row 28 to Row 2 -> (37, 2) (26 steps Up)
    # 3. Walk Left along Row 2 from Column 37 to Column 18 -> (18, 2) (19 steps Left)
    # 4. Walk Down 1 step to Row 3 to enter the Gatehouse -> (18, 3) (1 step Down - enter!)
    path = (
        ["Right"] * 10 +
        ["Up"] * 26 +
        ["Left"] * 19 +
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
