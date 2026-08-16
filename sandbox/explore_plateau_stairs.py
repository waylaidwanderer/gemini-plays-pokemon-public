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

print("Starting West Stairs exploration...")

# 1. Walk LEFT to Column 19 on Row 5
print("Walking LEFT to Column 19...")
for i in range(12):
    curr = mgba.get_coordinates()
    if curr['x'] == 19:
        break
    success, pos = step("Left")
    if not success:
        print(f"Blocked Left at {curr}")
        break

# 2. Walk DOWN Column 19 to Row 15
print("Walking DOWN Column 19 to Row 15...")
for i in range(12):
    curr = mgba.get_coordinates()
    if curr['y'] == 15:
        break
    success, pos = step("Down")
    if not success:
        print(f"Blocked Down at {curr}")
        break

# 3. Try walking RIGHT to climb the stairs at (20, 15)
print("Attempting to climb stairs by walking RIGHT...")
success, pos = step("Right")
if success:
    print("SUCCESSFULLY CLIMBED PLATeAU STAIRS! Position:", pos)
else:
    print("Stairs were BLOCKED.")

# Take screenshot to see where we are
mgba.take_screenshot()
