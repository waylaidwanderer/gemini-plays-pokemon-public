import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at: {pos}")

# Currently at (17, 8) in Celadon Game Corner
# 1. Walk Left 7 steps to Column 10
for _ in range(7):
    pos = move(["Left"])

# 2. Walk Up 3 steps to Row 5
for _ in range(3):
    pos = move(["Up"])

# 3. Walk Right 7 steps to Column 17
for _ in range(7):
    pos = move(["Right"])

# 4. Walk Up 1 step to Row 4 (secret stairs warp to B1F)
print("Stepping onto secret stairs...")
pos = move(["Up"])

print("Finished movement. Current position:", mgba.get_coordinates())
mgba.take_screenshot()
