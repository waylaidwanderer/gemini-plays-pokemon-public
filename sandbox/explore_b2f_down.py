import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at: {pos}")

# Current position is (9, 15) on B2F
# 1. Walk Down 2 steps to (9, 17)
for _ in range(2):
    pos = move(["Down"])

# 2. Walk Left 4 steps to (5, 17)
for _ in range(4):
    pos = move(["Left"])

# 3. Walk Up 2 steps to (5, 15)
# This is the staircase block!
for _ in range(2):
    pos = move(["Up"])

print("Finished movement. Current position:", mgba.get_coordinates())
mgba.take_screenshot()
