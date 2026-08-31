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

def toggle_switch_at_2_5():
    print("Toggling northern switch at (2, 5) to State A...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    mgba.press_buttons(["B"])
    time.sleep(1.0)
    print("Northern switch toggled.")

def main():
    pos = mgba.get_coordinates()
    print("Initial position:", pos)
    
    # Path to northern switch stand position (2, 6) in State B
    path_to_switch = [
        (4, 11),
        (3, 11),
        (2, 11),
        (2, 10), (2, 9), (2, 8), (2, 7), (2, 6)
    ]
    
    start_idx = 0
    min_dist = 9999
    for i, target in enumerate(path_to_switch):
        dist = abs(target[0] - pos['x']) + abs(target[1] - pos['y'])
        if dist < min_dist:
            min_dist = dist
            start_idx = i
            
    print(f"Walking to northern switch from index {start_idx} (target: {path_to_switch[start_idx]})")
    for idx in range(start_idx, len(path_to_switch)):
        walk_to_target(path_to_switch[idx])
        
    pos = mgba.get_coordinates()
    if pos['x'] == 2 and pos['y'] == 6:
        toggle_switch_at_2_5()
        
        # Now walk to the balcony in State A
        print("Walking to the balcony drop in State A...")
        path_to_balcony = [
            # Walk UP to Row 2
            (2, 5), (2, 4), (2, 3), (2, 2),
            # Walk RIGHT along Row 2 to Column 12
            (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (9, 2), (10, 2), (11, 2), (12, 2),
            # Down Column 12 to Row 3
            (12, 3),
            # Right Row 3 to Column 23
            (13, 3), (14, 3), (15, 3), (16, 3), (17, 3), (18, 3), (19, 3), (20, 3), (21, 3), (22, 3), (23, 3),
            # Column 23 DOWN to Row 12
            (23, 4), (23, 5), (23, 6), (23, 7), (23, 8), (23, 9), (23, 10), (23, 11), (23, 12),
            # Row 12 Right to Column 24
            (24, 12),
            # Column 24 DOWN to Row 16
            (24, 13), (24, 14), (24, 15), (24, 16),
            # Row 16 Left to Column 21
            (23, 16), (22, 16), (21, 16),
            # Column 21 DOWN to Row 18
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
            
            # Warp check
            if abs(pos_after['x'] - pos_before['x']) + abs(pos_after['y'] - pos_before['y']) > 5:
                print(f"WARPED! From {pos_before} to {pos_after}. Map transition successful!")
                break
                
        print("Sequence complete. Final position:", mgba.get_coordinates())
    else:
        print("Failed to reach (2, 6). Current position:", pos)
        
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
