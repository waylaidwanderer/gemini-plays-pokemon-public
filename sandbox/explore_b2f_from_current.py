import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at: {pos}")

# We are at (17, 5) on B2F.
# Let's try to walk Left to Column 12
for _ in range(5):
    pos = move(["Left"])

# Let's try to walk Down from Column 12
for _ in range(4):
    pos = move(["Down"])

print("Final position after exploration:", mgba.get_coordinates())
mgba.take_screenshot()
