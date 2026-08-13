# Complete robust script to run the Safari Zone Golden Route to retrieve the Gold Teeth starting from the current position.
import time
import sys
import bridge

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def handle_battle():
    print("Wild battle detected! Fleeing...")
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 150"])
    bridge.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 1200"])
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 150"])
    print("Fled from battle.")
    time.sleep(0.5)

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
            
        print(f"Step {idx}: At {pos}, walking {path[idx]}")
        new_pos = walk_step_robust(path[idx])
        
        if new_pos is None:
            continue
            
        if new_pos == pos:
            stuck_count += 1
            if stuck_count > 3:
                print(f"Blocked at {pos}! Pressing B and retrying.")
                bridge.press_buttons(["B", "sleep 300"])
                stuck_count = 0
        else:
            stuck_count = 0
            if check_warp:
                dist = abs(new_pos[0] - pos[0]) + abs(new_pos[1] - pos[1])
                if dist > 5:
                    print(f"Transition occurred! Jumped to {new_pos}")
                    return True
            idx += 1
    return True

def main():
    print("=== THE SAFARI ZONE GOLDEN TEETH RUN (CONTINUING) ===")
    
    pos = get_pos()
    print(f"Starting at {pos}")
    if pos is None:
        handle_battle()
        pos = get_pos()
        if pos is None:
            return
            
    # Phase 2: Continuing Area 1 (East) to Area 2 (North) transition at (0, 5)
    # We should be on column 8 or 9 on row >= 8.
    pos = get_pos()
    if pos is not None and pos[0] >= 5 and pos[0] <= 10 and pos[1] >= 8 and pos[1] <= 24:
        print("=== Phase 2: Continuing Area 1 (East) to Area 2 (North) ===")
        # Calculate remaining steps to (8, 8)
        up_steps = pos[1] - 8
        path_area1_rem = (
            ["Up"] * up_steps +      # to (8, 8)
            ["Right"] * 4 +          # to (12, 8)
            ["Up"] * 2 +             # to (12, 6) (climb stairs)
            ["Right"] * 5 +          # to (17, 6)
            ["Down"] * 2 +           # to (17, 8) (descend stairs)
            ["Right"] * 3 +          # to (20, 8)
            ["Up"] * 3 +             # to (20, 5)
            ["Left"] * 21            # to (0, 5) transition
        )
        if not run_path(path_area1_rem, check_warp=True):
            return
        time.sleep(1.0)
        pos = get_pos()
        print("Arrived in Area 2 (North):", pos)
        
    # Phase 3: Area 2 (North) to Area 3 (West) transition at (8, 36)
    # We should be at (39, 31).
    pos = get_pos()
    if pos is not None and pos[0] >= 35 and pos[1] >= 28:
        print("=== Phase 3: Area 2 (North) to Area 3 (West) ===")
        path_area2 = (
            ["Left"] * 24 +    # to (15, 31)
            ["Left"] * 2 +     # to (13, 31)
            ["Up"] * 10 +      # to (13, 21)
            ["Right"] * 2 +    # to (15, 21)
            ["Right"] * 1 +    # to (16, 21)
            ["Down"] * 9 +     # to (16, 30)
            ["Left"] * 8 +     # to (8, 30)
            ["Down"] * 5 +     # to (8, 35) through statue gap
            ["Down"] * 2       # to (8, 37) transition
        )
        if not run_path(path_area2, check_warp=True):
            return
        time.sleep(1.0)
        pos = get_pos()
        print("Arrived in Area 3 (West):", pos)
        
    # Phase 4: Area 3 (West) to Gold Teeth at (19, 25)
    # We should be at (26, 0).
    pos = get_pos()
    if pos is not None and pos[1] < 5:
        print("=== Phase 4: Area 3 (West) to Gold Teeth ===")
        path_area3 = (
            ["Left"] * 1 +     # to (25, 0)
            ["Down"] * 18 +    # to (25, 18)
            ["Left"] * 4 +     # to (21, 18)
            ["Down"] * 6 +     # to (21, 24)
            ["Left"] * 2       # to (19, 24)
        )
        if not run_path(path_area3):
            return
            
        time.sleep(0.5)
        pos = get_pos()
        print("Standing in front of Gold Teeth:", pos)
        
        # Interact with Gold Teeth
        print("Picking up Gold Teeth...")
        # Since we are at (19, 24) facing Down, we press Down once to face Down, then A to pick up!
        bridge.press_buttons(["Down", "sleep 200", "A", "sleep 1200"])
        bridge.press_buttons(["A", "sleep 1200"])
        print("Gold Teeth retrieved successfully!")
        
        # Check coordinates
        time.sleep(0.5)
        print("Final Position:", get_pos())

if __name__ == "__main__":
    main()
