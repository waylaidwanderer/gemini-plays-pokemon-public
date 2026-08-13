# Complete robust script to retrieve the Gold Teeth using the plateau path from (2, 9)
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

    # Step 3: Run the verified path from (2, 9) to warp transition
    if pos[1] == 9 and pos[0] == 2:
        print("=== Step 3: Navigating to Warp Transition via Row 8 Gap ===")
        path_to_warp = (
            ["Up"] * 1 +       # to (2, 8)
            ["Left"] * 2 +     # to (0, 8) (going through Row 8 gap at 1, 8)
            ["Down"] * 5       # transition to Center (East Compartment) at (0, 13)
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
