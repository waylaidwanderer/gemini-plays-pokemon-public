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
    print("=== CONTINUING TO AREA 3 (WEST) ===")
    
    pos = get_pos()
    print("Initial position:", pos)
    if pos is None:
        handle_battle()
        pos = get_pos()
        if pos is None:
            return
            
    # PHASE 1: Walk the rest of Area 1 starting from (5, 5)
    if pos == (5, 5):
        path_area1_remaining = (
            ["Left"] * 5                    # to transition at (0, 5)
        )
        print("Walking remaining path in Area 1 (East)...")
        if not run_path(path_area1_remaining, check_warp=True):
            return
            
    # Wait for map transition to stabilize
    bridge.press_buttons(["sleep 1000"])
    pos = get_pos()
    print("Arrived in Area 2 (North):", pos)
    
    # PHASE 2: Area 2 (North) to Area 3 (West)
    if pos is not None and pos[0] > 35:
        path_area2 = (
            ["Left"] * 17 +                 # to (22, 31)
            ["Up"] * 9 +                    # to (22, 22) (climb plateau)
            ["Left"] * 6 +                  # to (16, 22)
            ["Down"] * 6 +                  # to (16, 28) (descend plateau)
            ["Left"] * 4 +                  # to (12, 28)
            ["Down"] * 5 +                  # to (12, 33)
            ["Left"] * 4 +                  # to (8, 33)
            ["Down"] * 3                    # to transition warp at (8, 36)
        )
        print("Walking Area 2 (North) path...")
        if not run_path(path_area2, check_warp=True):
            return
            
    # Wait for map transition to stabilize
    bridge.press_buttons(["sleep 1000"])
    pos = get_pos()
    print("Arrived in Area 3 (West):", pos)

if __name__ == '__main__':
    main()
