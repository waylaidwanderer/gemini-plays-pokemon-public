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

# Current position is (30, 28) on the overworld.
# We want to go to (28, 19) to find the real Game Corner door!
# Path:
# 1. Walk Left to Column 22 on Row 28
# 2. Walk Up to Row 22 on Column 22
# 3. Walk Left to Column 16 on Row 22
# 4. Walk Up to Row 19 on Column 16
# 5. Walk Right to Column 28 on Row 19
# 6. Try to walk Up to enter the door at (28, 19)

pos = get_stable_coords()
print(f"Starting position: {pos}")

# 1. Walk Left to Column 22
while pos['x'] > 22:
    mgba.press_buttons(["Left"])
    time.sleep(0.35)
    pos = get_stable_coords()

print(f"Reached column 22: {pos}")

# 2. Walk Up to Row 22
while pos['y'] > 22:
    mgba.press_buttons(["Up"])
    time.sleep(0.35)
    pos = get_stable_coords()

print(f"Reached row 22: {pos}")

# 3. Walk Left to Column 16
while pos['x'] > 16:
    mgba.press_buttons(["Left"])
    time.sleep(0.35)
    pos = get_stable_coords()

print(f"Reached column 16: {pos}")

# 4. Walk Up to Row 19
while pos['y'] > 19:
    mgba.press_buttons(["Up"])
    time.sleep(0.35)
    pos = get_stable_coords()

print(f"Reached row 19: {pos}")

# 5. Walk Right to Column 28
while pos['x'] < 28:
    mgba.press_buttons(["Right"])
    time.sleep(0.35)
    pos = get_stable_coords()

print(f"At ({pos['x']}, {pos['y']}), trying UP to enter the Game Corner...")

# 6. Try UP to warp into the Game Corner!
mgba.press_buttons(["Up"])
time.sleep(1.2)

pos_after = get_stable_coords()
print(f"Coordinates after entering: {pos_after}")

scr = mgba.take_screenshot()
print(f"Screenshot inside saved at: {scr}")
