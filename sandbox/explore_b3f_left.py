import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at: {pos}")

# Currently at (27, 18) on B3F
# 1. Walk Up Column 27 to Row 7 (11 steps Up)
for _ in range(11):
    pos = move(["Up"])

# 2. Walk Left along Row 7 to Column 20 (7 steps Left)
for _ in range(7):
    pos = move(["Left"])

# 3. Walk Down Column 20 to Row 11 (4 steps Down)
for _ in range(4):
    pos = move(["Down"])

# 4. Walk Left to Column 18 (2 steps Left)
for _ in range(2):
    pos = move(["Left"])

print("Successfully reached Left Room at:", mgba.get_coordinates())
mgba.take_screenshot()
