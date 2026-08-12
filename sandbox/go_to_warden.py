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
    print("=== DIALOGUE SEQUENCE WITH THE WARDEN ===")
    pos = get_pos()
    print("Starting position:", pos)
    
    # We are at (4, 7) inside the Warden's House.
    # Route:
    # 1. Walk Up to Row 4 -> (4, 4) (3 steps Up)
    # 2. Walk Left to Column 2 -> (2, 4) (2 steps Left)
    # 3. Walk Up to face Warden at (2, 3) (1 step Up)
    path = (
        ["Up"] * 3 +
        ["Left"] * 2 +
        ["Up"]
    )
    if run_path(path):
        print("Aligned in front of the Warden! Interacting...")
        # Press A to start talking
        bridge.press_buttons(["A"])
        time.sleep(1.0)
        
        # Press A/B multiple times to progress dialogue and give Gold Teeth -> receive HM04
        for i in range(12):
            print(f"Dialogue step {i+1}...")
            bridge.press_buttons(["A"])
            time.sleep(1.2)
            
        print("Dialogue sequence completed!")
    else:
        print("Failed to reach the Warden!")

if __name__ == "__main__":
    main()
