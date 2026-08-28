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

# We are at (5, 10) on 1F West.
# Let's try walking UP first
print("Stepping UP to (5, 9)...")
mgba.press_buttons(["Up"])
time.sleep(1.5)
pos = check_pos()

# If we didn't warp, walk back DOWN to (5, 10)
if pos == {"x": 5, "y": 9}:
    print("Walking DOWN back to (5, 10)...")
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    pos = check_pos()

# Let's try walking DOWN to (5, 11)
if pos == {"x": 5, "y": 10}:
    print("Walking DOWN to (5, 11)...")
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    pos = check_pos()

# Now walk UP onto (5, 10) to see if it warps
if pos == {"x": 5, "y": 11}:
    print("Stepping UP onto (5, 10)...")
    mgba.press_buttons(["Up"])
    time.sleep(1.5)
    pos = check_pos()

# If we still didn't warp and are on (5, 10), try walking LEFT to (4, 10)
if pos == {"x": 5, "y": 10}:
    print("Walking LEFT to (4, 10)...")
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
    pos = check_pos()

# Now walk RIGHT onto (5, 10)
if pos == {"x": 4, "y": 10}:
    print("Stepping RIGHT onto (5, 10)...")
    mgba.press_buttons(["Right"])
    time.sleep(1.5)
    pos = check_pos()

mgba.take_screenshot()
