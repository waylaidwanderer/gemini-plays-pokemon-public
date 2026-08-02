import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at B3F: {pos}")

# Currently at (27, 16)
# 1. Walk Down 2 steps to Row 18
for _ in range(2):
    pos = move(["Down"])

# 2. Walk Left along Row 18 to Column 19
# We need to walk from Column 27 to Column 19 (8 steps Left)
# We will check if we get blocked (e.g. at Column 21)
print("Walking Left along Row 18...")
for i in range(27, 19, -1):
    pos = move(["Left"])
    if pos['x'] != i - 1:
        print(f"Blocked at {pos} during Left movement along Row 18")
        break

# 3. If we successfully reached (19, 18), we should warp to B4F!
print("Final position after script:", mgba.get_coordinates())
mgba.take_screenshot()
