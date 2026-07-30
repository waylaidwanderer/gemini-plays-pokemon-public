import mgba
import time

def get_stable_coords():
    pos1 = mgba.get_coordinates()
    time.sleep(0.1)
    pos2 = mgba.get_coordinates()
    while pos1 != pos2:
        pos1 = pos2
        time.sleep(0.1)
        pos2 = mgba.get_coordinates()
    return pos1

# We start at (10, 22)
pos = get_stable_coords()
print(f"Starting position: {pos}")

# 1. Walk Right to Column 22 on Row 22
while pos['x'] < 22:
    mgba.press_buttons(["Right"])
    time.sleep(0.35)
    pos = get_stable_coords()

print(f"Reached (22, 22): {pos}")

# 2. Walk Down to Row 28 on Column 22
while pos['y'] < 28:
    mgba.press_buttons(["Down"])
    time.sleep(0.35)
    pos = get_stable_coords()

print(f"Reached (22, 28): {pos}")

# 3. Walk Right to Column 26 on Row 28
while pos['x'] < 26:
    mgba.press_buttons(["Right"])
    time.sleep(0.35)
    pos = get_stable_coords()

print(f"Reached (26, 28): {pos}")

# 4. Press UP to enter the door at (26, 27)
print("Trying to enter door at (26, 27) by pressing UP...")
mgba.press_buttons(["Up"])
time.sleep(1.0) # wait for warp transition

pos_after = get_stable_coords()
print(f"Position after UP: {pos_after}")

# Take a screenshot inside
scr = mgba.take_screenshot()
print(f"Screenshot saved at: {scr}")
