import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at: {pos}")

# Current position is (12, 5) on B2F
# 1. Walk Left to Column 11
pos = move(["Left"])

# 2. Walk Down Column 11 to Row 15
# We need to move from 5 to 15 (10 steps Down)
for _ in range(10):
    pos = move(["Down"])

# 3. Walk Left to Column 5
# We need to move from 11 to 5 (6 steps Left)
for _ in range(6):
    pos = move(["Left"])

# 4. Walk Down to trigger the stairs to B3F (at (5, 15) going Down)
pos = move(["Down"])

print("Finished movement. Current position:", mgba.get_coordinates())
mgba.take_screenshot()
