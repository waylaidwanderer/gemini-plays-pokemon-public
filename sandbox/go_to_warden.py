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
    print("=== JUMPING LEDGE AND WALKING TO WARDEN'S HOUSE ===")
    pos = get_pos()
    print("Starting position:", pos)
    
    if pos == (23, 21):
        print("Jumping down the ledge...")
        bridge.press_buttons(["Down"])
        time.sleep(0.8) # Wait for jump animation to fully complete
        
        pos = get_pos()
        print("Position after jump:", pos)
        
    # We should have landed at (23, 23)
    if pos is not None and pos[0] == 23 and pos[1] == 23:
        # Route to Warden's House:
        # 1. Walk Down 4 steps to Row 27 -> (23, 27)
        # 2. Walk Right 4 steps to Column 27 -> (27, 27)
        # 3. Walk Up to enter!
        path = (
            ["Down"] * 4 +
            ["Right"] * 4 +
            ["Up"]
        )
        if run_path(path):
            print("Successfully entered Warden's House!")
            time.sleep(1.0)
            print("Final Position:", get_pos())
        else:
            print("Failed to reach Warden's House door!")

if __name__ == "__main__":
    main()
