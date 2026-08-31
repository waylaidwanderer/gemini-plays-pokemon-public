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
    # Let's explore the western room (Columns 1-3, Rows 5-15) to find the Mewtwo statue switch!
    # We will walk UP Column 2 from Row 11 to Row 5, and UP Column 3 from Row 11 to Row 5.
    pos = mgba.get_coordinates()
    print("Initial position in room:", pos)
    
    path = [
        # Up Column 2 to Row 5
        (2, 11), (2, 10), (2, 9), (2, 8), (2, 7), (2, 6), (2, 5),
        # Right to Column 3 Row 5
        (3, 5),
        # Down Column 3 to Row 11
        (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (3, 11)
    ]
    
    # Let's dynamically walk and probe for statues (interactable blocks)
    for target in path:
        pos_before = mgba.get_coordinates()
        walk_to_target(target)
        
        # After reaching target, face UP, LEFT, RIGHT, DOWN and try to press A to see if we get a switch dialogue!
        # But we don't want to get stuck in dialogue. We'll do a quick check if a statue is visible.
        # Mewtwo statues usually look like a distinctive sprite or wall fixture.
        # Let's try to press A facing UP on each step to see if we trigger dialogue.
        # If we trigger dialogue, we press A 4 times to toggle the switch and clear the text box!
        print(f"Probing at {target}...")
        for direction in ["Up", "Left", "Right"]:
            mgba.press_buttons([direction])
            time.sleep(0.3)
            # Press A
            mgba.press_buttons(["A"])
            time.sleep(0.5)
            # Take a screenshot to check if dialogue opened (we can look at coordinates or just press B to clear)
            # If a dialogue opened, we will clear it by pressing A 3 more times, then B.
            mgba.press_buttons(["A", "A", "A", "B"])
            time.sleep(0.5)
            
    print("Finished room search. Final position:", mgba.get_coordinates())
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
