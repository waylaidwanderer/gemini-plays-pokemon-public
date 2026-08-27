import mgba
import time

def check_pos():
    pos = mgba.get_coordinates()
    print("Current position:", pos)
    return pos

# Ensure menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

pos = check_pos()

# We are at (3, 11).
# 1. Test (5, 10) by walking onto it from (5, 11)
print("Testing (5, 10) by walking UP from (5, 11)...")
mgba.press_buttons(["Right", "sleep 450", "Right", "sleep 450", "Up"])
time.sleep(2.0)
pos = check_pos()

# If we didn't warp, we are at (5, 10). Walk DOWN back to (5, 11)
if pos == {"x": 5, "y": 10}:
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    pos = check_pos()

# 2. Test (6, 10) by walking UP from (6, 11)
if pos == {"x": 5, "y": 11}:
    print("Testing (6, 10) by walking UP from (6, 11)...")
    mgba.press_buttons(["Right", "sleep 450", "Up"])
    time.sleep(2.0)
    pos = check_pos()

# If we didn't warp, we are at (6, 10). Walk DOWN back to (6, 11)
if pos == {"x": 6, "y": 10}:
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    pos = check_pos()

# 3. Test (7, 10) by walking UP from (7, 11)
if pos == {"x": 6, "y": 11}:
    print("Testing (7, 10) by walking UP from (7, 11)...")
    mgba.press_buttons(["Right", "sleep 450", "Up"])
    time.sleep(2.0)
    pos = check_pos()

# If we didn't warp, we are at (7, 10). Walk DOWN back to (7, 11)
if pos == {"x": 7, "y": 10}:
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    pos = check_pos()

# 4. Test (8, 10) by walking UP from (8, 11)
if pos == {"x": 7, "y": 11}:
    print("Testing (8, 10) by walking UP from (8, 11)...")
    mgba.press_buttons(["Right", "sleep 450", "Up"])
    time.sleep(2.0)
    pos = check_pos()

mgba.take_screenshot()
