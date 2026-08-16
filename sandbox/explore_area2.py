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

print("Starting Area 2 exploration from (28, 11)...")

# 1. Try walking LEFT to Column 21 on Row 11
for i in range(8):
    curr = mgba.get_coordinates()
    if curr['x'] == 21:
        break
    success, pos = step("Left")
    if not success:
        print(f"Blocked Left at {curr}")
        break

# 2. Try walking DOWN Column 21 as far as we can to find the Southern corridor
print("Trying to walk DOWN Column 21...")
for i in range(15):
    curr = mgba.get_coordinates()
    success, pos = step("Down")
    if not success:
        print(f"Blocked DOWN at {curr}")
        break

# Let's see where we are
curr = mgba.get_coordinates()
print("Current position after walking Down:", curr)

# 3. If we are on some Row, let's try to walk LEFT or RIGHT to find the plateau or Area 3 transition
# Let's try to walk LEFT to Column 8
print("Trying to walk LEFT to Column 8...")
for i in range(15):
    curr = mgba.get_coordinates()
    if curr['x'] == 8:
        print("Reached Column 8!")
        break
    success, pos = step("Left")
    if not success:
        print(f"Blocked Left at {curr}")
        break

curr = mgba.get_coordinates()
print("Final exploration position:", curr)
mgba.take_screenshot()
