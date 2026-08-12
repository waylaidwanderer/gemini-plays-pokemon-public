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

def handle_battle():
    print("Wild battle/interaction detected! Escaping...")
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 250"])
    bridge.press_buttons(["Down", "sleep 250", "Right", "sleep 250", "A", "sleep 1200"])
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 200"])

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        handle_battle()
        return None
        
    bridge.press_buttons([direction])
    
    # Wait for position to change (up to 750 ms)
    for _ in range(5):
        time.sleep(0.15)
        new_pos = get_pos()
        if new_pos is None:
            return None
        if new_pos != pos:
            return new_pos
            
    print(f"Bumping/stuck at {pos} walking {direction}!")
    return pos

def run_path(path):
    idx = 0
    stuck_count = 0
    while idx < len(path):
        pos = get_pos()
        if pos is None:
            handle_battle()
            continue
            
        print(f"Path: At {pos}, walking {path[idx]}...")
        new_pos = walk_step_robust(path[idx])
        
        if new_pos is None:
            time.sleep(0.5)
            new_pos = get_pos()
            if new_pos is None:
                handle_battle()
                continue
                
        if new_pos == pos:
            stuck_count += 1
            if stuck_count > 3:
                return False
        else:
            stuck_count = 0
            idx += 1
    return True

def test_row28():
    # Currently at (13, 23).
    # 1. Walk Left to (7, 23)
    # 2. Walk Down to (7, 28)
    # 3. Walk Right as far as possible to see if we can cross Column 14
    
    print("=== TESTING ROW 28 RIGHT WALK ===")
    path_to_row28 = ["Left"] * 6 + ["Down"] * 5
    if not run_path(path_to_row28):
        print("Failed to reach (7, 28).")
        return
        
    pos = get_pos()
    print("Arrived at:", pos)
    if pos != (7, 28):
        print("Not at expected start position.")
        return
        
    # Walk Right up to 10 steps
    for step in range(10):
        curr_pos = get_pos()
        new_pos = walk_step_robust("Right")
        if new_pos is None:
            handle_battle()
            new_pos = get_pos()
        print(f"Step {step}: {curr_pos} -> {new_pos}")
        if new_pos == curr_pos:
            print("BLOCKED!")
            break

if __name__ == "__main__":
    test_row28()
