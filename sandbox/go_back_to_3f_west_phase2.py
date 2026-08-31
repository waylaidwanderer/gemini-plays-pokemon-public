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
    # Phase 2: Walk from (26, 2) to (3, 11) via Row 2 and Column 10
    path = [
        # Left Row 2 to Column 10
        (25, 2), (24, 2), (23, 2), (22, 2), (21, 2), (20, 2), (19, 2), (18, 2), (17, 2), (16, 2), (15, 2), (14, 2), (13, 2), (12, 2), (11, 2), (10, 2),
        # Down Column 10 to Row 11
        (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), (10, 10), (10, 11),
        # Left along Row 11 to Column 3
        (9, 11), (8, 11), (7, 11), (6, 11), (5, 11), (4, 11), (3, 11)
    ]
    
    print("Starting Phase 2: Walk to switch at (3, 11)...")
    for target in path:
        walk_to_target(target)
        
    print("Walk complete. Turning LEFT to face switch and toggling...")
    # Stand at (3, 11), face Left, press A 4 times
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
    # 4 A presses with enough delay for transitions
    for _ in range(4):
        mgba.press_buttons(["A"])
        time.sleep(0.5)
        
    print("Phase 2 complete! Switch toggled to State B. Current coordinates:", mgba.get_coordinates())
    # Take screenshot
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
