# Script to explore the southern ground level and reach (19, 26) to pick up the Gold Teeth
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
    bridge.press_buttons(["sleep 300"])
    
    new_pos = get_pos()
    if new_pos is None:
        handle_battle()
        return None
        
    if new_pos != pos:
        return new_pos
        
    # Check for battle transition
    bridge.press_buttons(["sleep 800"])
    new_pos = get_pos()
    if new_pos is None:
        handle_battle()
        return None
        
    print(f"Bumping/stuck at {pos} walking {direction}!")
    return pos

def run_path(path):
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
            idx += 1
    return True

def main():
    print("=== EXPLORING TO SOUTH PASSAGE ===")
    
    pos = get_pos()
    print(f"Starting at {pos}")
    if pos is None:
        handle_battle()
        pos = get_pos()
        if pos is None:
            return

    # Path from current (18, 24) to (21, 18)
    path_to_21_18 = (
        ["Right"] * 3 +   # to (21, 24)
        ["Up"] * 6        # to (21, 18)
    )
    if not run_path(path_to_21_18):
        return

    pos = get_pos()
    print(f"At {pos}, checking right movement...")
    
    # Let's walk right to column 25
    path_to_25_18 = ["Right"] * 4
    if not run_path(path_to_25_18):
        return

    pos = get_pos()
    print(f"At {pos}, trying to go DOWN Column 25...")
    
    # Try to go DOWN Column 25 as far as possible
    # Row 18 to Row 26 is 8 steps Down
    for i in range(8):
        pos = get_pos()
        if pos is None:
            handle_battle()
            continue
        print(f"Down Step {i}: At {pos}")
        new_pos = walk_step_robust("Down")
        if new_pos is None:
            continue
        if new_pos == pos:
            print(f"Blocked going Down at {pos}!")
            break

    pos = get_pos()
    print(f"Final Position after Down test: {pos}")
    
    # If we are at row 26, walk left to (19, 26)
    if pos is not None and pos[1] == 26:
        left_steps = pos[0] - 19
        path_to_teeth = ["Left"] * left_steps
        if run_path(path_to_teeth):
            pos = get_pos()
            print(f"Successfully reached {pos}! Facing UP to interact...")
            bridge.press_buttons(["Up", "sleep 200", "A", "sleep 1200"])
            bridge.press_buttons(["A", "sleep 1200"])
            print("Interaction complete.")

if __name__ == "__main__":
    main()
