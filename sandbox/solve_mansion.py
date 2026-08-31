import mgba
import time

def flee_battle_safe():
    print("Wild battle detected! Fleeing safely...")
    # Clear battle text
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.2)
    # Move cursor to RUN (Down then Right)
    print("Selecting RUN...")
    mgba.press_buttons(["Down", "Right"])
    time.sleep(0.3)
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    # Dismiss "Got away safely!"
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.2)
    print("Fled battle safely.")

def get_dir(curr, target):
    if target[0] > curr['x']: return "Right"
    if target[0] < curr['x']: return "Left"
    if target[1] > curr['y']: return "Down"
    if target[1] < curr['y']: return "Up"
    return None

def walk_to_target(target):
    while True:
        pos = mgba.get_coordinates()
        if pos['x'] == target[0] and pos['y'] == target[1]:
            print(f"Reached target {target}")
            break
            
        direction = get_dir(pos, target)
        if not direction:
            break
            
        print(f"Current: ({pos['x']}, {pos['y']}) | Moving {direction} to target {target}")
        mgba.press_buttons([direction])
        time.sleep(0.5)
        
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            # We didn't move. Let's check for battle or block.
            print("No movement. Pressing B to dismiss potential menu/text.")
            mgba.press_buttons(["B"])
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                # Still no movement, try to flee
                flee_battle_safe()
                time.sleep(0.5)

def main():
    # Phase 1: Walk from current position (20, 16) back to switch at (3, 11) in State A
    path_to_switch = [
        # Right Row 16 to Column 26
        (21, 16), (22, 16), (23, 16), (24, 16), (25, 16), (26, 16),
        # Up Column 26 to Row 9
        (26, 15), (26, 14), (26, 13), (26, 12), (26, 11), (26, 10), (26, 9),
        # Right to Column 27 Row 9
        (27, 9),
        # Up Column 27 to Row 1
        (27, 8), (27, 7), (27, 6), (27, 5), (27, 4), (27, 3), (27, 2), (27, 1),
        # Left Row 1 to Column 12
        (26, 1), (25, 1), (24, 1), (23, 1), (22, 1), (21, 1), (20, 1), (19, 1), (18, 1), (17, 1), (16, 1), (15, 1), (14, 1), (13, 1), (12, 1),
        # Down Column 12 to Row 11
        (12, 2), (12, 3), (12, 4), (12, 5), (12, 6), (12, 7), (12, 8), (12, 9), (12, 10), (12, 11),
        # Left along Row 11 to Column 3
        (11, 11), (10, 11), (9, 11), (8, 11), (7, 11), (6, 11), (5, 11), (4, 11), (3, 11)
    ]
    
    print("PHASE 1: Walking back to switch in State A...")
    for target in path_to_switch:
        walk_to_target(target)
        
    # Phase 2: Toggle switch to State B
    walk_to_target((3, 11))
    print("PHASE 2: Turning Left and toggling switch to State B...")
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
    mgba.press_buttons(["A", "sleep 300", "A", "sleep 300", "A", "sleep 300", "A", "sleep 300"])
    time.sleep(1.0)
    
    # Phase 3: Walk to the balcony drop in State B
    path_to_balcony = [
        # Right Row 11 to Column 10
        (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11),
        # Down Column 10 to Row 16
        (10, 12), (10, 13), (10, 14), (10, 15), (10, 16),
        # Right Row 16 to Column 21 (open in State B!)
        (11, 16), (12, 16), (13, 16), (14, 16), (15, 16), (16, 16), (17, 16), (18, 16), (19, 16), (20, 16), (21, 16),
        # Down Column 21 to Row 18 (open in State B!)
        (21, 17), (21, 18),
        # Left Row 18 to Column 19 (balcony drop!)
        (20, 18), (19, 18),
        # Down on (19, 18) to trigger the fall
        (19, 19)
    ]
    
    print("PHASE 3: Walking to balcony drop in State B...")
    for target in path_to_balcony:
        pos_before = mgba.get_coordinates()
        walk_to_target(target)
        pos_after = mgba.get_coordinates()
        
        # Robust warp check: did our position change by more than 5 tiles in a single step?
        if abs(pos_after['x'] - pos_before['x']) + abs(pos_after['y'] - pos_before['y']) > 5:
            print(f"WARPED! From {pos_before} to {pos_after}. We fell through! Success!")
            break
            
    print("Finished path. Final position:", mgba.get_coordinates())
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
