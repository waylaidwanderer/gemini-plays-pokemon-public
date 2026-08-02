import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at: {pos}")

# We are at (4, 15) in Celadon Game Corner.
# 1. Walk Down 2 steps to Row 17
for _ in range(2):
    pos = move(["Down"])

# 2. Walk Right 13 steps to Column 17
for _ in range(13):
    pos = move(["Right"])

# 3. Walk Up 13 steps to Row 4 (this should warp us back to B1F!)
for _ in range(13):
    pos = move(["Up"])

print("Finished movement. Current position:", mgba.get_coordinates())
mgba.take_screenshot()
