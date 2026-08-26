import mgba
import time

def walk_step(direction, expected_coords):
    mgba.press_buttons([direction])
    time.sleep(0.4)
    pos = mgba.get_coordinates()
    if pos == expected_coords:
        return True
    return False

def run_steps(steps):
    for d, c in steps:
        if not walk_step(d, c):
            return False
    return True

# Walk to (2, 12) facing UP
pos = mgba.get_coordinates()
print("Starting position:", pos)
if pos == {"x": 2, "y": 11}:
    run_steps([
        ("Down", {"x": 2, "y": 12}),
        ("Down", {"x": 2, "y": 13}),
        ("Up", {"x": 2, "y": 12}),
    ])

# Step 1: Press A once (should open "A secret switch!")
mgba.press_buttons(["A"])
time.sleep(1.5)
scr1 = mgba.take_screenshot()
print("Screenshot 1:", scr1)

# Step 2: Press A second time (should open YES/NO menu)
mgba.press_buttons(["A"])
time.sleep(1.5)
scr2 = mgba.take_screenshot()
print("Screenshot 2:", scr2)

# Step 3: Press A third time (should select YES and show "Who wouldn't!")
mgba.press_buttons(["A"])
time.sleep(1.5)
scr3 = mgba.take_screenshot()
print("Screenshot 3:", scr3)

# Step 4: Press A fourth time (should close dialogue and return to overworld)
mgba.press_buttons(["A"])
time.sleep(1.5)
scr4 = mgba.take_screenshot()
print("Screenshot 4:", scr4)
