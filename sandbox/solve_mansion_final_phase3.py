import mgba
import time

def flee_battle_safe():
    print("Wild battle detected! Fleeing safely...")
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    print("Selecting RUN...")
    mgba.press_buttons(["Down", "Right"])
    time.sleep(0.2)
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
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
            print("No movement. Pressing B.")
            mgba.press_buttons(["B"])
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                flee_battle_safe()
                time.sleep(0.5)

def main():
    # Currently at (22, 3) on 3F East in State B.
    # Phase 1: Walk to the Mewtwo switch at (2, 5) on 3F West
    path_to_switch = [
        # Walk RIGHT along Row 16 to Column 24
        (22, 16), (23, 16), (24, 16),
        # Walk UP Column 24 to Row 12 (bypassing closed gate at 25, 13)
        (24, 15), (24, 14), (24, 13), (24, 12),
        # Walk RIGHT along Row 12 to Column 26
        (25, 12), (26, 12),
        # Walk UP Column 26 to Row 3
        (26, 11), (26, 10), (26, 9), (26, 8), (26, 7), (26, 6), (26, 5), (26, 4), (26, 3),
        # Walk LEFT along Row 3 to Column 12
        (25, 3), (24, 3), (23, 3), (22, 3), (21, 3), (20, 3), (19, 3), (18, 3), (17, 3), (16, 3), (15, 3), (14, 3), (13, 3), (12, 3),
        # Walk UP Column 12 to Row 2
        (12, 2),
        # Walk LEFT along Row 2 to Column 2
        (11, 2), (10, 2), (9, 2), (8, 2), (7, 2), (6, 2), (5, 2), (4, 2), (3, 2), (2, 2),
        # Walk DOWN Column 2 to Row 5 (Mewtwo switch statue at 2, 5)
        (2, 3), (2, 4), (2, 5)
    ]
    
    # Phase 2: From (2, 5) in State A, walk to the balcony drop at (19, 18)
    path_to_balcony = [
        # Walk UP Column 2 to Row 2
        (2, 4), (2, 3), (2, 2),
        # Walk RIGHT along Row 2 to Column 10
        (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (9, 2), (10, 2),
        # Walk DOWN Column 10 to Row 3
        (10, 3),
        # Walk RIGHT along Row 3 to Column 21
        (11, 3), (12, 3), (13, 3), (14, 3), (15, 3), (16, 3), (17, 3), (18, 3), (19, 3), (20, 3), (21, 3),
        # Walk DOWN Column 21 to Row 18 (both gates at 21, 5 and 21, 17 are open in State A!)
        (21, 4), (21, 5), (21, 6), (21, 7), (21, 8), (21, 9), (21, 10), (21, 11), (21, 12), (21, 13), (21, 14), (21, 15), (21, 16), (21, 17), (21, 18),
        # Walk LEFT along Row 18 to Column 19 (balcony drop!)
        (20, 18), (19, 18),
        # Step DOWN to trigger drop!
        (19, 19)
    ]
    
    pos = mgba.get_coordinates()
    print("Initial position:", pos)
    
    # Dynamically find starting index in path_to_switch
    start_idx = 0
    min_dist = 9999
    for i, target in enumerate(path_to_switch):
        dist = abs(target[0] - pos['x']) + abs(target[1] - pos['y'])
        if dist < min_dist:
            min_dist = dist
            start_idx = i
            
    # Execution of Phase 1
    print(f"Walking to switch starting from index {start_idx} (target: {path_to_switch[start_idx]})...")
    for idx in range(start_idx, len(path_to_switch)):
        walk_to_target(path_to_switch[idx])
        
    print("Reached switch at (2, 5). Facing UP...")
    walk_to_target((2, 5))
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    
    # Toggle switch to State A (requires exactly 4 A presses to clear text box)
    print("Toggling switch to State A...")
    mgba.press_buttons(["A"])
    time.sleep(0.4)
    mgba.press_buttons(["A"])
    time.sleep(0.4)
    mgba.press_buttons(["A"])
    time.sleep(0.4)
    mgba.press_buttons(["A"])
    time.sleep(0.8)
    
    # Clear any residual menus
    mgba.press_buttons(["B"])
    time.sleep(0.4)
    
    # Execution of Phase 2
    print("Walking to balcony drop at (19, 18) in State A...")
    for target in path_to_balcony:
        pos_before = mgba.get_coordinates()
        walk_to_target(target)
        pos_after = mgba.get_coordinates()
        
        # Warp check: did our floor change drastically?
        if abs(pos_after['x'] - pos_before['x']) + abs(pos_after['y'] - pos_before['y']) > 5:
            print(f"WARPED! From {pos_before} to {pos_after}. Map transition successful!")
            break
            
    print("Finished path. Final position:", mgba.get_coordinates())
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
