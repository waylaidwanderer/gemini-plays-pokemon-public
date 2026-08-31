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
    # Currently at (23, 8).
    # Path: Down Column 23 to Row 14, Left Row 14 to Column 21, Up Column 21 to Row 5 (testing for stairs!)
    path = [
        # Down Column 23 to Row 14
        (23, 9), (23, 10), (23, 11), (23, 12), (23, 13), (23, 14),
        # Left Row 14 to Column 21
        (22, 14), (21, 14),
        # Up Column 21 to Row 5
        (21, 13), (21, 12), (21, 11), (21, 10), (21, 9), (21, 8), (21, 7), (21, 6), (21, 5)
    ]
    
    print("Initial position:", mgba.get_coordinates())
    
    for target in path:
        pos_before = mgba.get_coordinates()
        walk_to_target(target)
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
