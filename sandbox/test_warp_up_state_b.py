import mgba
import time

def get_state():
    pos = mgba.get_coordinates()
    print("Current position:", pos)
    return pos

# Clear the "Got away safely!" text
print("Dismissing text...")
mgba.press_buttons(["B"])
time.sleep(1.0)
pos = get_state()

# 1. Walk LEFT along Row 6 to Column 12
if pos["y"] == 6 and pos["x"] > 12:
    print("Walking LEFT along Row 6 to Column 12...")
    steps_left = []
    for x in range(pos["x"] - 1, 11, -1):
        steps_left.append(("Left", {"x": x, "y": 6}))
    for d, c in steps_left:
        mgba.press_buttons([d])
        time.sleep(0.4)
    pos = get_state()

# 2. Walk DOWN Column 12 to Row 11
if pos == {"x": 12, "y": 6}:
    print("Walking DOWN Column 12 to Row 11...")
    steps_down = []
    for y in range(7, 12):
        steps_down.append(("Down", {"x": 12, "y": y}))
    for d, c in steps_down:
        mgba.press_buttons([d])
        time.sleep(0.4)
    pos = get_state()

# 3. Walk LEFT to (7, 11)
if pos == {"x": 12, "y": 11}:
    print("Walking LEFT along Row 11 to (7, 11)...")
    steps_left_11 = []
    for x in range(11, 6, -1):
        steps_left_11.append(("Left", {"x": x, "y": 11}))
    for d, c in steps_left_11:
        mgba.press_buttons([d])
        time.sleep(0.4)
    pos = get_state()

# 4. Step UP onto stairs at (7, 10) to warp UP to 3F West
if pos == {"x": 7, "y": 11}:
    print("Stepping UP onto stairs to warp UP to 3F West...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)
    pos = get_state()
