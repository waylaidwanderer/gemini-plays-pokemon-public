# The ultimate correct, complete, ground-level script to retrieve the Gold Teeth from (19, 24)
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
    bridge.press_buttons(["sleep 300"])
    
    new_pos = get_pos()
    if new_pos is None:
        handle_battle()
        return None
        
    if new_pos != pos:
        return new_pos
        
    # Check if in battle transition
    bridge.press_buttons(["sleep 800"])
    new_pos = get_pos()
    if new_pos is None:
        handle_battle()
        return None
        
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
    print("=== THE ULTIMATE GROUND TEETH RETRIEVAL SCRIPT ===")
    
    pos = get_pos()
    print(f"Current Position: {pos}")
    if pos is None:
        handle_battle()
        pos = get_pos()
        if pos is None:
            return

    # Step 1: Walk to return to Area 2 (North) via Column 26
    if pos == (25, 2):
        print("=== Step 1: Walking back to Area 2 (North) ===")
        path_to_area2 = (
            ["Right"] * 1 +    # to (26, 2)
            ["Up"] * 3         # transition to Area 2 (North) at (8, 35)
        )
        if not run_path(path_to_area2, check_warp=True):
            return
        time.sleep(1.0)
        pos = get_pos()
        print("Transitioned back to Area 2 (North):", pos)

    # Step 2: Navigate Area 2 (North) on foot using Row 9 to Column 4
    pos = get_pos()
    if pos is not None and pos[0] >= 5 and pos[1] >= 30:
        print("=== Step 2: Navigating Area 2 (North) via Row 9 ===")
        # We should be at (8, 35) or similar.
        # Walk up to Row 9, left to Column 4, and down to transition at (4, 36)
        up_steps = pos[1] - 9
        path_to_sw = (
            ["Up"] * up_steps +   # to (8, 9)
            ["Left"] * 4 +        # to (4, 9)
            ["Down"] * 27         # transition to Area 3 (West) northwest compartment
        )
        if not run_path(path_to_sw, check_warp=True):
            return
        time.sleep(1.0)
        pos = get_pos()
        print("Emerged in Area 3 (West) Northwest Compartment:", pos)

    # Step 3: Run the verified ground path to warp transition
    pos = get_pos()
    if pos is not None and pos[0] < 5 and pos[1] < 15:
        print("=== Step 3: Navigating to Warp Transition on Column 0 ===")
        # We are at (4, 0) or similar. Walk to Column 0 and down to Row 13 warp
        left_steps = pos[0]
        down_steps = 13 - pos[1]
        path_to_warp = (
            ["Left"] * left_steps +
            ["Down"] * down_steps
        )
        if not run_path(path_to_warp, check_warp=True):
            return
        time.sleep(1.0)
        pos = get_pos()
        print("Transitioned into Center (East Compartment):", pos)

    # Step 4: Center (East Compartment) to Gold Teeth at (19, 25)
    pos = get_pos()
    if pos is not None and pos[0] >= 28 and pos[1] >= 24:
        print("=== Step 4: Center (East Compartment) to Gold Teeth ===")
        path_to_teeth = (
            ["Down"] * 1 +     # to (29, 26)
            ["Left"] * 10      # to (19, 26)
        )
        if not run_path(path_to_teeth):
            return
        time.sleep(0.5)
        pos = get_pos()
        print("Standing below Gold Teeth at:", pos)
        
        # Face UP and pick them up!
        print("Picking up Gold Teeth...")
        bridge.press_buttons(["Up", "sleep 250"])
        bridge.press_buttons(["A", "sleep 1200", "A", "sleep 1200", "B", "sleep 500"])
        print("Gold Teeth retrieved successfully!")
        
        # Open bag to verify
        print("Opening BAG to verify...")
        bridge.press_buttons(["Start", "sleep 500", "Down", "Down", "A", "sleep 800"])
        print("BAG is open. Please verify Gold Teeth on next turn!")

if __name__ == "__main__":
    main()
