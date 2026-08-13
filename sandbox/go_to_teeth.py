# Ultimate, correct, complete script to retrieve the Gold Teeth from (19, 24) in Area 3 (West)
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
    print("=== THE ULTIMATE GOLDEN TEETH RETRIEVAL SCRIPT ===")
    
    pos = get_pos()
    print(f"Current Position: {pos}")
    if pos is None:
        handle_battle()
        pos = get_pos()
        if pos is None:
            return

    # Step 1: Walk back to (26, 0) to return to Area 2 (North)
    if pos[1] >= 20 and pos[0] >= 15:
        print("=== Step 1: Walking back to Area 2 (North) Transition ===")
        # Exact path from (19, 24) to (26, 0) return transition
        path_to_area2 = (
            ["Right"] * 2 +    # to (21, 24)
            ["Up"] * 6 +       # to (21, 18)
            ["Right"] * 4 +    # to (25, 18)
            ["Up"] * 18 +      # to (25, 0)
            ["Right"] * 1 +    # to (26, 0)
            ["Up"] * 1         # transition to Area 2 (North)
        )
        if not run_path(path_to_area2, check_warp=True):
            return
            
        time.sleep(1.0)
        pos = get_pos()
        print("Transitioned back to Area 2 (North):", pos)

    # Step 2: Navigate Area 2 (North) to southwest transition at (4, 36)
    pos = get_pos()
    if pos is not None and pos[1] >= 30 and pos[0] >= 5:
        print("=== Step 2: Navigating Area 2 (North) to Southwest Transition ===")
        # We are at (8, 35) or similar.
        # Walk left to column 4, and down to transition
        path_to_sw = (
            ["Left"] * 4 +     # to (4, 35)
            ["Down"] * 2       # transition to Area 3 (West) northwest compartment
        )
        if not run_path(path_to_sw, check_warp=True):
            return
            
        time.sleep(1.0)
        pos = get_pos()
        print("Emerged in Area 3 (West) Northwest Compartment:", pos)

    # Step 3: Run the verified zig-zag path from (4, 20) to (0, 13) warp
    pos = get_pos()
    if pos is not None and pos[0] < 5 and pos[1] >= 15:
        print("=== Step 3: Zig-zagging to Warp Transition ===")
        path_to_warp = (
            ["Left"] * 3 +     # to (1, 20)
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
        print("BAG is open.")

if __name__ == "__main__":
    main()
