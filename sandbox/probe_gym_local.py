import mgba
import time
from PIL import Image

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

print("Starting exhaustive search for Giovanni in the upper-right room from current:", get_pos())

# We are at (18, 3)
# We will walk horizontally along Row 3 from Column 14 to Column 21
# and print coordinates plus take screenshots to find Giovanni

# 1. Walk Left to (14, 3)
pos = get_pos()
while pos[0] > 14:
    mgba.press_buttons(["Left"])
    time.sleep(0.55)
    pos = get_pos()
    print("Walked Left, position:", pos)

# Take screenshot at (14, 3)
mgba.take_screenshot()

# 2. Walk Right to (21, 3)
pos = get_pos()
while pos[0] < 21:
    mgba.press_buttons(["Right"])
    time.sleep(0.55)
    pos = get_pos()
    print("Walked Right, position:", pos)

# Take screenshot at (21, 3)
mgba.take_screenshot()

print("Search complete. Current Position:", get_pos())
