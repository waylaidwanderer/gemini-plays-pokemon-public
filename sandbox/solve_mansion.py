import mgba
import time

def flee_battle_safe():
    print("Wild battle detected! Fleeing safely...")
    time.sleep(1.0)
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.2)
    print("Pressing Down and Right to select RUN...")
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
            # Check if in battle or blocked
            print("No movement. Pressing B to dismiss potential menu/text.")
            mgba.press_buttons(["B"])
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                # Still no movement, try to flee
                flee_battle_safe()
                time.sleep(0.5)

def main():
    # If currently in battle or on end-battle screen, let's flee or dismiss it
    # But wait, we are currently in the overworld at (10, 16) facing RIGHT on Turn 70073!
    # Let's define our exact coordinate path to the balcony in State A
    path = [
        # Up Column 10 to Row 11
        (10, 15), (10, 14), (10, 13), (10, 12), (10, 11),
        # Right to Column 12 Row 11
        (11, 11), (12, 11),
        # Up Column 12 to Row 1
        (12, 10), (12, 9), (12, 8), (12, 7), (12, 6), (12, 5), (12, 4), (12, 3), (12, 2), (12, 1),
        # Right along Row 1 to Column 27
        (13, 1), (14, 1), (15, 1), (16, 1), (17, 1), (18, 1), (19, 1), (20, 1), (21, 1), (22, 1),
        (23, 1), (24, 1), (25, 1), (26, 1), (27, 1),
        # Down Column 27 to Row 9
        (27, 2), (27, 3), (27, 4), (27, 5), (27, 6), (27, 7), (27, 8), (27, 9),
        # Left to Column 26 Row 9
        (26, 9),
        # Down Column 26 to Row 16
        (26, 10), (26, 11), (26, 12), (26, 13), (26, 14), (26, 15), (26, 16),
        # Left along Row 16 to Column 21
        (25, 16), (24, 16), (23, 16), (22, 16), (21, 16),
        # Down Column 21 to Row 18
        (21, 17), (21, 18),
        # Left along Row 18 to Column 19 (balcony drop!)
        (20, 18), (19, 18),
        # Down on (19, 18) to trigger the fall
        (19, 19)
    ]
    
    print("Starting ultimate State A balcony drop solution...")
    for target in path:
        pos = mgba.get_coordinates()
        # If coordinates changed drastically, we fell through to B1F West!
        dist = abs(target[0] - pos['x']) + abs(target[1] - pos['y'])
        if dist > 5:
            print("WARPED! We fell through to B1F West! Success!")
            break
        walk_to_target(target)
        
    print("Finished path. Final position:", mgba.get_coordinates())
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
