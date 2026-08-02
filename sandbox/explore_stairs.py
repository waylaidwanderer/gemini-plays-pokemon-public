import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting from: {pos}")

# We are at (19, 15) on B3F
# 1. Walk Up to (19, 10) (5 steps Up)
print("Walking up to Row 10...")
for _ in range(5):
    pos = move(["Up"])

# 2. Walk Left to (17, 10) through (18, 10) (2 steps Left)
print("Walking left to Column 17...")
for _ in range(2):
    pos = move(["Left"])

print("Final position:", mgba.get_coordinates())
mgba.take_screenshot()
