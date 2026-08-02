import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at: {pos}")

# Currently at (28, 15) on B1F
# 1. Walk Up Column 28 to Row 9 (6 steps Up)
for _ in range(6):
    pos = move(["Up"])

# 2. Walk Left to Column 25 (3 steps Left)
for _ in range(3):
    pos = move(["Left"])

# 3. Walk Up Column 25 to Row 5 (4 steps Up)
for _ in range(4):
    pos = move(["Up"])

# 4. Walk Left to Column 23 (2 steps Left)
for _ in range(2):
    pos = move(["Left"])

# 5. Walk Up Column 23 to Row 2 (3 steps Up) to warp to B2F
print("Stepping onto B2F stairs at (23, 2)...")
for _ in range(3):
    pos = move(["Up"])

print("Finished movement. Current position:", mgba.get_coordinates())
mgba.take_screenshot()
