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

# Walk to (2, 12)
pos = mgba.get_coordinates()
print("Starting position:", pos)
if pos == {"x": 7, "y": 10}:
    run_steps([
        ("Down", {"x": 7, "y": 11}),
        ("Down", {"x": 7, "y": 12}),
        ("Down", {"x": 7, "y": 13}),
        ("Left", {"x": 6, "y": 13}),
        ("Left", {"x": 5, "y": 13}),
        ("Left", {"x": 4, "y": 13}),
        ("Left", {"x": 3, "y": 13}),
        ("Left", {"x": 2, "y": 13}),
        ("Up", {"x": 2, "y": 12}),
    ])

# Face UP
mgba.press_buttons(["Up"])
time.sleep(0.5)

# Press A once and capture
mgba.press_buttons(["A"])
time.sleep(1.0)
scr1 = mgba.take_screenshot()
print("Screenshot after 1st A:", scr1)

# Press A second time and capture
mgba.press_buttons(["A"])
time.sleep(1.0)
scr2 = mgba.take_screenshot()
print("Screenshot after 2nd A:", scr2)

# Press A third time and capture
mgba.press_buttons(["A"])
time.sleep(1.0)
scr3 = mgba.take_screenshot()
print("Screenshot after 3rd A:", scr3)

# Press A fourth time and capture
mgba.press_buttons(["A"])
time.sleep(1.0)
scr4 = mgba.take_screenshot()
print("Screenshot after 4th A:", scr4)
