# Script to retrieve the Gold Teeth using the Western Southern Plateau route in Area 2 (North)
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
        
    # Press direction once
    bridge.press_buttons([direction])
    
    # Sleep 300ms to let the movement complete
    bridge.press_buttons(["sleep 300"])
    
    new_pos = get_pos()
    if new_pos is None:
        handle_battle()
        return None
        
    if new_pos != pos:
        return new_pos
        
    # If position didn't change, we might be in a battle transition.
    # Sleep another 800ms and check again.
    bridge.press_buttons(["sleep 800"])
    new_pos = get_pos()
    if new_pos is None:
        handle_battle()
        return None
        
    # If it still hasn't changed, it's a real bump.
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
    print("=== RETRIEVING THE GOLD TEETH VIA PLATEAU ===")
    
    pos = get_pos()
    print(f"Starting at {pos}")
    if pos is None:
        handle_battle()
        pos = get_pos()
        if pos is None:
            return

    # Check if we are in Area 2 (North)
    # We should be at (18, 31) or similar.
    if pos[1] >= 28 and pos[0] >= 10:
        print("=== Phase 3: Area 2 (North) to Area 3 (West) ===")
        # Calculate steps to (22, 31)
        right_steps = 22 - pos[0]
        
        path_area2 = (
            ["Right"] * right_steps + # to (22, 31)
            ["Up"] * 8 +               # to (22, 23)
            ["Up"] * 1 +               # to (22, 22) (climb plateau)
            ["Left"] * 6 +             # to (16, 22)
            ["Down"] * 6 +             # to (16, 28) (descend plateau stairs to (16, 28))
            ["Left"] * 8 +             # to (8, 28)
            ["Down"] * 7 +             # to (8, 35) through statue gap
            ["Down"] * 2               # to transition at (8, 37)
        )
        if not run_path(path_area2, check_warp=True):
            return
        time.sleep(1.0)
        pos = get_pos()
        print("Arrived in Area 3 (West):", pos)

    # Check if we are in Area 3 (West)
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
        
        # Check coordinates and wait
        time.sleep(0.5)
        pos = get_pos()
        print("Final Position:", pos)

if __name__ == "__main__":
    main()
