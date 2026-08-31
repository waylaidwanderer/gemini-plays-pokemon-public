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

def toggle_switch():
    print("Toggling switch with generous delays...")
    
    # Face left first just in case
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
    
    # 1. Interact
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    
    # 2. Page 2
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    
    # 3. Choose Yes
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    
    # 4. Page 3
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    
    # 5. Page 4
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    
    # 6. Clear residual
    mgba.press_buttons(["B"])
    time.sleep(1.0)
    print("Switch toggle sequence completed.")

def main():
    pos = mgba.get_coordinates()
    print("Initial position:", pos)
    
    # Path from current position (22, 16) to the switch stand position (3, 11) on 3F West in State B:
    path_to_switch = [
        # Row 16 Right to Column 24
        (23, 16), (24, 16),
        # Column 24 UP to Row 12
        (24, 15), (24, 14), (24, 13), (24, 12),
        # Row 12 Right to Column 26
        (25, 12), (26, 12),
        # Column 26 UP to Row 3
        (26, 11), (26, 10), (26, 9), (26, 8), (26, 7), (26, 6), (26, 5), (26, 4), (26, 3),
        # Row 3 Left to Column 12
        (25, 3), (24, 3), (23, 3), (22, 3), (21, 3), (20, 3), (19, 3), (18, 3), (17, 3), (16, 3), (15, 3), (14, 3), (13, 3), (12, 3),
        # Column 12 DOWN to Row 11
        (12, 4), (12, 5), (12, 6), (12, 7), (12, 8), (12, 9), (12, 10), (12, 11),
        # Row 11 Left to Column 3 (switch position is 2, 11 so we stand at 3, 11 facing Left)
        (11, 11), (10, 11), (9, 11), (8, 11), (7, 11), (6, 11), (5, 11), (4, 11), (3, 11)
    ]
    
    # Find start index in case we are already partially along the path
    start_idx = 0
    min_dist = 9999
    for i, target in enumerate(path_to_switch):
        dist = abs(target[0] - pos['x']) + abs(target[1] - pos['y'])
        if dist < min_dist:
            min_dist = dist
            start_idx = i
            
    print(f"Walking to switch from index {start_idx} (target: {path_to_switch[start_idx]})")
    for idx in range(start_idx, len(path_to_switch)):
        target = path_to_switch[idx]
        walk_to_target(target)
        
    pos = mgba.get_coordinates()
    if pos['x'] == 3 and pos['y'] == 11:
        print("Successfully reached switch stand position (3, 11). Toggling switch to State A...")
        toggle_switch()
        
        # Verify state: check if we are in State A now by walking the State A path to the balcony
        print("Walking to the balcony drop in State A...")
        path_to_balcony = [
            # Row 11 Right to Column 12
            (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11), (12, 11),
            # Column 12 UP to Row 3
            (12, 10), (12, 9), (12, 8), (12, 7), (12, 6), (12, 5), (12, 4), (12, 3),
            # Row 3 Right to Column 23
            (13, 3), (14, 3), (15, 3), (16, 3), (17, 3), (18, 3), (19, 3), (20, 3), (21, 3), (22, 3), (23, 3),
            # Column 23 DOWN to Row 12
            (23, 4), (23, 5), (23, 6), (23, 7), (23, 8), (23, 9), (23, 10), (23, 11), (23, 12),
            # Row 12 Right to Column 24
            (24, 12),
            # Column 24 DOWN to Row 16
            (24, 13), (24, 14), (24, 15), (24, 16),
            # Row 16 Left to Column 21
            (23, 16), (22, 16), (21, 16),
            # Column 21 DOWN to Row 18 (past open gate at 21, 17 in State A!)
            (21, 17), (21, 18),
            # Row 18 Left to Column 19
            (20, 18), (19, 18),
            # Step DOWN to trigger drop!
            (19, 19)
        ]
        
        for target in path_to_balcony:
            pos_before = mgba.get_coordinates()
            walk_to_target(target)
            pos_after = mgba.get_coordinates()
            
            # Warp check: did our floor change drastically?
            if abs(pos_after['x'] - pos_before['x']) + abs(pos_after['y'] - pos_before['y']) > 5:
                print(f"WARPED! From {pos_before} to {pos_after}. Map transition successful!")
                break
                
        print("Finished sequence. Final position:", mgba.get_coordinates())
    else:
        print("Failed to reach switch stand position. Current position:", pos)
        
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
