import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting B3F pathing from: {pos}")

# We are at (25, 6)
# 1. Walk Down to (25, 7)
pos = move(["Down"])

# 2. Walk Left to (19, 7) (6 steps Left)
for _ in range(6):
    pos = move(["Left"])

# 3. Walk Down to (19, 10) (3 steps Down)
for _ in range(3):
    pos = move(["Down"])

# 4. Walk Left to (17, 10) through the gap at (18, 10) (2 steps Left)
for _ in range(2):
    pos = move(["Left"])

print("Successfully reached Western Room at:", mgba.get_coordinates())
mgba.take_screenshot()
