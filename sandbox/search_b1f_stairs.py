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
    # Currently at (27, 12).
    # Let's systematically test every tile in the southeast area of 1F East.
    # The area is Rows 12-16, Columns 25-28.
    # We will walk on:
    # 1. (28, 12)
    # 2. (26, 12), (25, 12)
    # 3. (25, 13), (25, 14), (25, 15), (25, 16)
    # 4. (26, 16), (27, 16), (28, 16)
    # 5. (28, 15), (28, 14)
    # 6. (27, 14), (27, 15)
    # 7. (26, 15), (26, 14)
    
    test_tiles = [
        (28, 12),
        (27, 12),
        (26, 12),
        (25, 12),
        (25, 13),
        (25, 14),
        (26, 14),
        (27, 14),
        (28, 14),
        (28, 15),
        (27, 15),
        (26, 15),
        (25, 15),
        (25, 16),
        (26, 16),
        (27, 16),
        (28, 16)
    ]
    
    print("Initial position:", mgba.get_coordinates())
    
    for target in test_tiles:
        pos_before = mgba.get_coordinates()
        # If the target is blocked (like we already know some wall/rubble), walk_to_target will try and then recover or continue
        try:
            walk_to_target(target)
        except Exception as e:
            print(f"Error walking to {target}: {e}")
            
        pos_after = mgba.get_coordinates()
        print(f"Stood on {pos_after} (tried to reach {target})")
        
        # Warp check: did our coordinates change drastically?
        if abs(pos_after['x'] - pos_before['x']) + abs(pos_after['y'] - pos_before['y']) > 5:
            print(f"WARPED! From {pos_before} to {pos_after}. Map transition successful!")
            break
            
    print("Search finished. Current position:", mgba.get_coordinates())
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
