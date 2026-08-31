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
    # Phase 1: Walk from (21, 16) on 3F East to the switch at (3, 11) on 3F West
    # We are in State A, so the gate at (25, 13) is OPEN.
    path = [
        # Up Column 21 to Row 15
        (21, 15),
        # Right along Row 15 to Column 25
        (22, 15), (23, 15), (24, 15), (25, 15),
        # Up Column 25 past the open gate at (25, 13) to Row 12
        (25, 14), (25, 13), (25, 12),
        # Left along Row 12 to Column 21 (gate at Column 21 is open in State A)
        (24, 12), (23, 12), (22, 12), (21, 12),
        # Up Column 21 to Row 3
        (21, 11), (21, 10), (21, 9), (21, 8), (21, 7), (21, 6), (21, 5), (21, 4), (21, 3),
        # Left along Row 3 to Column 10
        (20, 3), (19, 3), (18, 3), (17, 3), (16, 3), (15, 3), (14, 3), (13, 3), (12, 3), (11, 3), (10, 3),
        # Down Column 10 to Row 11
        (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), (10, 10), (10, 11),
        # Left along Row 11 to Column 3 (right next to switch)
        (9, 11), (8, 11), (7, 11), (6, 11), (5, 11), (4, 11), (3, 11)
    ]
    
    pos = mgba.get_coordinates()
    print("Initial position:", pos)
    
    for target in path:
        walk_to_target(target)
        
    print("Reached switch area at (3, 11). Interacting with the switch...")
    # Stand at (3, 11) facing LEFT to interact with the Mewtwo statue at (2, 11)
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
    
    # Toggle switch to State B (requires exactly 4 A presses to clear text box)
    print("Toggling switch...")
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
    
    print("Toggled switch. Final position:", mgba.get_coordinates())
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
