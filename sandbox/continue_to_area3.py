import bridge
import time

def get_pos():
    for _ in range(4):
        pos = bridge.get_coordinates()
        if pos is not None:
            return pos
        bridge.press_buttons(["sleep 50"])
    return None

def handle_battle():
    print("Wild battle detected! Escaping...")
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 200"])
    bridge.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 1500"])
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 200"])
    print("Escape completed. Stabilizing...")
    time.sleep(1.0)

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
            
    # Stuck or bumped!
    print(f"No movement detected after walking {direction} at {pos}. Checking for battle/dialogue...")
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 150"])
    bridge.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 1000"])
    for _ in range(2):
        bridge.press_buttons(["B", "sleep 200"])
        
    new_pos = get_pos()
    if new_pos is not None:
        return new_pos
    return pos

def run_path(path, check_warp=False):
    idx = 0
    stuck_count = 0
    while idx < len(path):
        pos = get_pos()
        if pos is None:
            handle_battle()
            continue
            
        print(f"Path step {idx}: At {pos}, sending {path[idx]}")
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
            if stuck_count > 3:
                print(f"Blocked at {pos}! Pressing B and retrying...")
                bridge.press_buttons(["B", "sleep 300"])
                stuck_count = 0
        else:
            stuck_count = 0
            if check_warp:
                dist = abs(new_pos[0] - pos[0]) + abs(new_pos[1] - pos[1])
                if dist > 5:
                    print(f"Transition occurred! Jumped to {new_pos}")
                    break
            idx += 1
    return True

def main():
    print("=== CONTINUING TO AREA 2 (NORTH) ===")
    
    pos = get_pos()
    print("Initial position:", pos)
    if pos is None:
        handle_battle()
        pos = get_pos()
        if pos is None:
            return
            
    # Walk the rest of Area 1 starting from (7, 24)
    # The target of the walk is transition at (0, 5) which goes to Area 2 (North) (39, 31)
    if pos == (7, 24):
        path_area1_remaining = (
            ["Right"] * 13 +                # to (20, 24)
            ["Up"] * 4 +                    # to (20, 20) (climb southern plateau)
            ["Left"] * 8 +                  # to (12, 20)
            ["Down"] * 2 +                  # to (12, 22) (descend southern plateau)
            ["Left"] * 4 +                  # to (8, 22)
            ["Up"] * 14 +                   # to (8, 8)
            ["Right"] * 4 +                 # to (12, 8)
            ["Up"] * 2 +                    # to (12, 6) (climb northern plateau)
            ["Right"] * 5 +                 # to (17, 6)
            ["Down"] * 2 +                  # to (17, 8) (descend northern plateau)
            ["Right"] * 3 +                 # to (20, 8)
            ["Up"] * 5 +                    # to (20, 3) (Row 3 bypass)
            ["Left"] * 13 +                 # to (7, 3)
            ["Down"] * 2 +                  # to (7, 5)
            ["Left"] * 7                    # to transition at (0, 5)
        )
        print("Walking remaining path in Area 1 (East)...")
        if not run_path(path_area1_remaining, check_warp=True):
            return
            
    # Wait for map transition to stabilize
    bridge.press_buttons(["sleep 1000"])
    pos = get_pos()
    print("Arrived at:", pos)

if __name__ == '__main__':
    main()
