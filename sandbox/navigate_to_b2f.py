import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at: {pos}")

# Current position is (24, 15) on B1F
# 1. Walk Right to Column 28
for _ in range(4):
    pos = move(["Right"])

# 2. Walk Up Column 28 to Row 9
for _ in range(6):
    pos = move(["Up"])

# 3. Walk Left to Column 20
for _ in range(8):
    pos = move(["Left"])

# 4. Walk Up Column 20 to Row 5
for _ in range(4):
    pos = move(["Up"])

# 5. Walk Right to Column 23
for _ in range(3):
    pos = move(["Right"])

# 6. Walk Up to Row 2 (this should hit the stairs and warp to B2F)
for _ in range(3):
    pos = move(["Up"])

print("Finished moving. Current position:", mgba.get_coordinates())
mgba.take_screenshot()
