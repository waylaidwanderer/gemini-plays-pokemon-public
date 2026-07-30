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

# We start at (25, 27)
pos = get_stable_coords()
print(f"Starting position: {pos}")

# 1. Walk Left to Column 23
while pos['x'] > 23:
    mgba.press_buttons(["Left"])
    time.sleep(0.35)
    pos = get_stable_coords()

# 2. Walk Up to Row 22
while pos['y'] > 22:
    mgba.press_buttons(["Up"])
    time.sleep(0.35)
    pos = get_stable_coords()

print(f"Reached plaza corridor at: {pos}")

# 3. Walk Left to Column 10
while pos['x'] > 10:
    mgba.press_buttons(["Left"])
    time.sleep(0.35)
    pos = get_stable_coords()

print(f"Reached western side at: {pos}")

# Take a screenshot
scr = mgba.take_screenshot()
print(f"Screenshot at C10 saved at: {scr}")
