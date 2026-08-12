import bridge
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    for _ in range(4):
        pos = bridge.get_coordinates()
        if pos is not None:
            return pos[0], pos[1]
        bridge.press_buttons(["sleep 50"])
    return None

def handle_battle():
    print("Handling wild battle...")
    bridge.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    escape_sequence = [
        "Down", "sleep 200",
        "Right", "sleep 200",
        "A", "sleep 1500"
    ]
    bridge.press_buttons(escape_sequence)
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 200"])
    bridge.press_buttons(["sleep 500"])

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        handle_battle()
        return None
        
    bridge.press_buttons([direction])
    
    for _ in range(5):
        bridge.press_buttons(["sleep 100"])
        new_pos = get_pos()
        if new_pos is None:
            handle_battle()
            return None
        if new_pos != pos:
            return new_pos
            
    print(f"Bumping/stuck at {pos} walking {direction}!")
    return pos

def run_path(path, check_warp=False):
    idx = 0
    stuck_count = 0
    while idx < len(path):
        pos = get_pos()
        if pos is None:
            handle_battle()
            continue
            
        print(f"Step {idx}: At {pos}, walking {path[idx]}...")
        new_pos = walk_step_robust(path[idx])
        
        if new_pos is None:
            continue
            
        if new_pos == pos:
            time.sleep(0.5)
            check_pos = get_pos()
            if check_pos is None:
                handle_battle()
                stuck_count = 0
                continue
            stuck_count += 1
            print(f"Stuck at {pos}! Stuck count: {stuck_count}")
            if stuck_count > 3:
                print("Stuck! Pressing B and retrying...")
                bridge.press_buttons(["B", "sleep 300"])
                stuck_count = 0
        else:
            stuck_count = 0
            if check_warp:
                dist = abs(new_pos[0] - pos[0]) + abs(new_pos[1] - pos[1])
                if dist > 5:
                    print(f"SUCCESS! Transitioned to coordinates: {new_pos}")
                    break
            idx += 1
    return True

def main():
    print("=== CONTINUING SAFARI RUN TO AREA 2 (NORTH) ===")
    
    pos = get_pos()
    print("Starting position:", pos)
    if pos is None:
        handle_battle()
        pos = get_pos()
        if pos is None:
            return
            
    # Path to Area 2 (North) transition at (0, 5)
    # Remaining path from (9, 10):
    # - Walk Up 2 to (9, 8)
    # - Walk Right 3 to (12, 8)
    # - Walk Up 2 to (12, 6) (climbs stairs)
    # - Walk Right 5 to (17, 6)
    # - Walk Down 2 to (17, 8) (descends stairs)
    # - Walk Right 3 to (20, 8)
    # - Walk Up 5 to (20, 3)
    # - Walk Left 13 to (7, 3)
    # - Walk Down 2 to (7, 5)
    # - Walk Left 7 to (0, 5) (transition)
    path = (
        ["Up"] * 2 +
        ["Right"] * 3 +
        ["Up"] * 2 +
        ["Right"] * 5 +
        ["Down"] * 2 +
        ["Right"] * 3 +
        ["Up"] * 5 +
        ["Left"] * 13 +
        ["Down"] * 2 +
        ["Left"] * 7
    )
    
    if run_path(path, check_warp=True):
        print("Successfully reached Area 2!")
        time.sleep(1.0)
        pos = get_pos()
        print("Inside Area 2 position:", pos)
    else:
        print("Failed to reach Area 2!")

if __name__ == "__main__":
    main()
