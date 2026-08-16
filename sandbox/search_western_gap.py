import mgba
import time

def escape_battle():
    print("Encountered a battle! Attempting to escape...")
    for _ in range(6):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    for _ in range(6):
        mgba.press_buttons(["B"])
        time.sleep(0.1)

def step(direction):
    curr = mgba.get_coordinates()
    cx, cy = curr['x'], curr['y']
    mgba.press_buttons([direction])
    time.sleep(0.45)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == cx and new_pos['y'] == cy:
        escape_battle()
        time.sleep(0.5)
        after = mgba.get_coordinates()
        if after['x'] == cx and after['y'] == cy:
            return False, (cx, cy)
        return True, (after['x'], after['y'])
    return True, (new_pos['x'], new_pos['y'])

print("Probing RIGHT along Row 4...")
# We are currently at (8, 5). Walk UP to (8, 4).
step("Up")

while True:
    curr = mgba.get_coordinates()
    cx, cy = curr['x'], curr['y']
    print(f"At ({cx}, {cy}). Trying to walk Right...")
    
    success_right, pos_right = step("Right")
    if not success_right:
        print(f"Column {cx+1} is BLOCKED.")
        # If blocked Right, try walking UP
        print("Trying to go UP...")
        success_up, pos_up = step("Up")
        if not success_up:
            print("Blocked UP too! Let's try DOWN.")
            success_down, pos_down = step("Down")
            if not success_down:
                print("Completely blocked in all directions!")
                break
    else:
        print(f"Moved successfully to {pos_right}")
        # At the new column, check if we can walk DOWN
        print("Checking if we can walk DOWN from here...")
        success_d, pos_d = step("Down")
        if success_d:
            print(f"Found DOWN path at Column {pos_right[0]}! Reached {pos_d}")
            # Walk back UP
            step("Up")

print("Probing complete.")
mgba.take_screenshot()
