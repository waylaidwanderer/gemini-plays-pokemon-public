# Complete robust script to retrieve the Gold Teeth using the plateau path from (6, 31) in Area 2 (North)
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
    print("=== THE ULTIMATE GOLDEN TEETH PLATEAU RETRIEVAL SCRIPT ===")
    
    pos = get_pos()
    print(f"Current Position: {pos}")
    if pos is None:
        handle_battle()
        pos = get_pos()
        if pos is None:
            return

    # Step 1: Walk from (6, 31) to transition to Area 3 (West) at (26, 0)
    if pos[1] >= 30 and pos[0] >= 5 and pos[0] <= 10:
        print("=== Step 1: Walking to Area 3 (West) Transition ===")
        # Walk to Column 8, down to Row 35, and down to transition
        right_steps = 8 - pos[0]
        path_to_area3 = (
            ["Right"] * right_steps +
            ["Down"] * 4 +     # to (8, 35)
            ["Down"] * 1       # transition to Area 3 (West) at (26, 0)
        )
        if not run_path(path_to_area3, check_warp=True):
            return
            
        time.sleep(1.0)
        pos = get_pos()
        print("Transitioned back to Area 3 (West):", pos)

    # Step 2: Navigate Area 3 (West) across the plateau to the west ground level
    pos = get_pos()
    if pos is not None and pos[0] >= 15 and pos[1] <= 15:
        print("=== Step 2: Navigating Area 3 (West) to West Ground Level ===")
        # Assuming we are at (26, 0)
        path_across_plateau = (
            ["Left"] * 1 +     # to (25, 0)
            ["Down"] * 18 +    # to (25, 18)
            ["Left"] * 4 +     # to (21, 18)
            ["Up"] * 2 +       # to (21, 16) (stairs onto plateau)
            ["Left"] * 15 +    # to (6, 16) (across plateau)
            ["Down"] * 4 +     # to (6, 20) (stairs off plateau)
            ["Left"] * 5       # to (1, 20)
        )
        if not run_path(path_across_plateau):
            return
        pos = get_pos()
        print("Arrived on West Ground Level:", pos)

    # Step 3: Run the verified zig-zag path to warp transition
    pos = get_pos()
    if pos is not None and pos[0] < 5 and pos[1] >= 15:
        print("=== Step 3: Zig-zagging to Warp Transition ===")
        path_to_warp = (
            ["Up"] * 2 +       # to (1, 18)
            ["Right"] * 2 +    # to (3, 18) (zig)
            ["Up"] * 5 +       # to (3, 13) (climb onto Row 13 bridge!)
            ["Left"] * 3       # to (0, 13) warp transition
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
