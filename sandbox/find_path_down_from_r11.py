import mgba
import time

def escape_battle():
    print("Encountered a battle! Escape sequence...")
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

print("--- PROBING DOWNWARD PASSAGES FROM ROW 11 ---")
# Currently at (23, 11).
# We will step Right to Column 24, 25, 26, 27, and at each column try to step Down to Row 12.

for col in range(23, 28):
    # Walk to Column col on Row 11
    print(f"Moving to Column {col} Row 11...")
    # Since we are currently at some column, we either step Left or Right to reach col
    while True:
        curr = mgba.get_coordinates()
        cx, cy = curr['x'], curr['y']
        if cx == col:
            break
        elif cx < col:
            success, pos = step("Right")
            if not success:
                print(f"Blocked moving Right at ({cx}, {cy})")
                break
        else:
            success, pos = step("Left")
            if not success:
                print(f"Blocked moving Left at ({cx}, {cy})")
                break
                
    # Now try to step Down onto Row 12
    curr = mgba.get_coordinates()
    cx, cy = curr['x'], curr['y']
    if cx == col:
        print(f"At Column {col}, trying to step DOWN...")
        success_down, pos_down = step("Down")
        if success_down and pos_down[1] == 12:
            print(f"SUCCESS! Walked DOWN at Column {col}")
            # Step back UP to Row 11 to continue probing
            step("Up")
        else:
            print(f"Column {col} Row 12 is BLOCKED")

mgba.take_screenshot()
