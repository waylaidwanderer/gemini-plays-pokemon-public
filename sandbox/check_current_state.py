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
    # Currently at (3, 11) on 3F West.
    # Path to (2, 5) via Column 12 (clear of Row 9 wall and Row 8/9 rubble):
    path = [
        # Walk to Column 12 Row 11
        (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11), (12, 11),
        # Up Column 12 to Row 5 (avoiding Row 8 rubble on Columns 8-11)
        (12, 10), (12, 9), (12, 8), (12, 7), (12, 6), (12, 5),
        # Left along Row 5 to Column 2 (where switch is likely located)
        (11, 5), (10, 5), (9, 5), (8, 5), (7, 5), (6, 5), (5, 5), (4, 5), (3, 5), (2, 5)
    ]
    
    pos = mgba.get_coordinates()
    print("Initial position:", pos)
    
    for target in path:
        walk_to_target(target)
        
    print("Reached (2, 5). Facing UP to probe switch...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    print("Pressing A to interact with Mewtwo statue switch...")
    mgba.press_buttons(["A"])
    time.sleep(0.8)
    
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
