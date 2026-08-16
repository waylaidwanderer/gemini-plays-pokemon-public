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

print("Probing northern rows to cross Column 29...")
# We are currently at (17, 8).
# Walk to Column 20 Row 8 (open ground, grass-free)
for i in range(3):
    step("Right")

# Now try to walk UP on Column 20 as far as we can to Row 1
print("Walking UP Column 20...")
for i in range(10):
    curr = mgba.get_coordinates()
    if curr['y'] == 1:
        break
    success, pos = step("Up")
    if not success:
        print(f"Blocked UP at {curr}")
        break

# Now try to walk RIGHT along the current Row to Column 35!
curr = mgba.get_coordinates()
cy = curr['y']
print(f"At Row {cy}. Probing RIGHT...")
for i in range(20):
    curr = mgba.get_coordinates()
    if curr['x'] == 35:
        print("SUCCESS! Crossed Column 29!")
        break
    success, pos = step("Right")
    if not success:
        print(f"Blocked RIGHT at {curr}")
        break

mgba.take_screenshot()
