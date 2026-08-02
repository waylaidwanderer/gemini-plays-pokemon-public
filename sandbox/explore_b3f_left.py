import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at: {pos}")

# Currently at (22, 18) on B3F
# 1. Walk Up Column 22 to Row 12 (6 steps Up)
for _ in range(6):
    pos = move(["Up"])

# 2. Walk Right to Column 25 (3 steps Right)
for _ in range(3):
    pos = move(["Right"])

# 3. Walk Up Column 25 to Row 7 (5 steps Up)
for _ in range(5):
    pos = move(["Up"])

# 4. Walk Left along Row 7 to Column 18 (7 steps Left)
for _ in range(7):
    pos = move(["Left"])

# 5. Walk Down Column 18 to Row 11 (4 steps Down)
for _ in range(4):
    pos = move(["Down"])

print("Successfully reached Left Room at:", mgba.get_coordinates())
mgba.take_screenshot()
