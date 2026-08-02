import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at: {pos}")

# Currently at (27, 8) on B2F
# 1. Walk Left to Column 25 (2 steps Left)
for _ in range(2):
    pos = move(["Left"])

# 2. Walk Down to Row 13 (5 steps Down)
for _ in range(5):
    pos = move(["Down"])

# 3. Walk Left to Column 21 (4 steps Left)
for _ in range(4):
    pos = move(["Left"])

# 4. Walk Up Column 21 to Row 8 (5 steps Up) to warp to B3F
print("Stepping onto B3F stairs at (21, 8)...")
for _ in range(5):
    pos = move(["Up"])

print("Finished movement. Current position:", mgba.get_coordinates())
mgba.take_screenshot()
