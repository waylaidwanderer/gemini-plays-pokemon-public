import mgba
import time

def flee_battle_safe():
    print("Wild battle detected! Fleeing safely...")
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.2)
    print("Selecting RUN...")
    mgba.press_buttons(["Down", "Right"])
    time.sleep(0.3)
    mgba.press_buttons(["A"])
    time.sleep(1.5)
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
            print("No movement. Pressing B.")
            mgba.press_buttons(["B"])
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                flee_battle_safe()
                time.sleep(0.5)

def main():
    # We are currently at (5, 11) in State B on 3F West
    # Walk to the balcony drop in State B
    path = [
        # Walk RIGHT along Row 11 to Column 12
        (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11), (12, 11),
        # Walk UP Column 12 to Row 3
        (12, 10), (12, 9), (12, 8), (12, 7), (12, 6), (12, 5), (12, 4), (12, 3),
        # Walk RIGHT along Row 3 to Column 26 (passing through 21, 3)
        (13, 3), (14, 3), (15, 3), (16, 3), (17, 3), (18, 3), (19, 3), (20, 3), (21, 3), (22, 3), (23, 3), (24, 3), (25, 3), (26, 3),
        # Walk DOWN Column 26 to Row 16 (pitfall is covered in State B!)
        (26, 4), (26, 5), (26, 6), (26, 7), (26, 8), (26, 9), (26, 10), (26, 11), (26, 12), (26, 13), (26, 14), (26, 15), (26, 16),
        # Walk LEFT along Row 16 to Column 21
        (25, 16), (24, 16), (23, 16), (22, 16), (21, 16),
        # Walk DOWN Column 21 to Row 18 (gate at 21, 17 is open in State B!)
        (21, 17), (21, 18),
        # Walk LEFT along Row 18 to Column 19 (balcony drop!)
        (20, 18), (19, 18),
        # Walk DOWN on (19, 18) to trigger the fall
        (19, 19)
    ]
    
    print("Starting ultimate State B balcony route...")
    for target in path:
        pos_before = mgba.get_coordinates()
        walk_to_target(target)
        pos_after = mgba.get_coordinates()
        
        # Warp check: did our floor change drastically?
        if abs(pos_after['x'] - pos_before['x']) + abs(pos_after['y'] - pos_before['y']) > 5:
            print(f"WARPED! From {pos_before} to {pos_after}. We fell through!")
            break
            
    print("Finished path. Final position:", mgba.get_coordinates())
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
