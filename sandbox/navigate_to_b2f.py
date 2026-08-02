import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at: {pos}")

# Current position is (26, 9) on B1F
# 1. Walk Left to Column 25
pos = move(["Left"])

# 2. Walk Up Column 25 to Row 5
# We need to move from 9 to 5 (4 steps Up)
for _ in range(4):
    pos = move(["Up"])

# 3. Walk Left to Column 20
# We need to move from 25 to 20 (5 steps Left)
for _ in range(5):
    pos = move(["Left"])

# 4. Walk Up Column 20 to Row 2
# We need to move from 5 to 2 (3 steps Up)
for _ in range(3):
    pos = move(["Up"])

# 5. Walk Right to Column 23 (this should hit the stairs at 23, 2 and warp to B2F)
# We need to move from 20 to 23 (3 steps Right)
for _ in range(3):
    pos = move(["Right"])

print("Finished. Final position:", mgba.get_coordinates())
mgba.take_screenshot()
