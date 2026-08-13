# Correct script to walk back across the plateau and retrieve the Gold Teeth from (6, 15) in Area 3 (West)
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
    print("=== RETRIEVING THE GOLD TEETH FROM AREA 3 (WEST) (19, 24) ===")
    
    pos = get_pos()
    print(f"Current Position: {pos}")
    if pos is None:
        handle_battle()
        pos = get_pos()
        if pos is None:
            return

    # Path from (6, 15) to (19, 24)
    if pos == (6, 15):
        print("=== Step 1: Navigating to Gold Teeth via Plateau ===")
        path = (
            ["Left"] * 3 +     # to (3, 15)
            ["Down"] * 5 +     # to (3, 20)
            ["Right"] * 3 +    # to (6, 20)
            ["Up"] * 4 +       # to (6, 16) (stairs onto plateau)
            ["Right"] * 15 +   # to (21, 16) (across plateau)
            ["Down"] * 2 +     # to (21, 18) (stairs off plateau)
            ["Down"] * 6 +     # to (21, 24)
            ["Left"] * 2       # to (19, 24)
        )
        if not run_path(path):
            return
            
        time.sleep(0.5)
        pos = get_pos()
        print("Standing in front of Gold Teeth at:", pos)
        
        # Face DOWN and pick them up!
        print("Picking up Gold Teeth...")
        bridge.press_buttons(["Down", "sleep 250"])
        bridge.press_buttons(["A", "sleep 1200", "A", "sleep 1200", "B", "sleep 500"])
        print("Gold Teeth retrieved successfully!")
        
        # Open bag to verify
        print("Opening BAG to verify...")
        bridge.press_buttons(["Start", "sleep 500", "Down", "Down", "A", "sleep 800"])
        print("BAG is open. Please verify Gold Teeth on next turn!")

if __name__ == "__main__":
    main()
