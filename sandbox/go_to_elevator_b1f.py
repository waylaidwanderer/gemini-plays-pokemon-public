import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at: {pos}")

# Currently at (24, 9)
# Step 1: Walk Right to Column 28
# We need to move from 24 to 28 (4 steps Right)
for _ in range(4):
    pos = move(["Right"])

# Step 2: Walk Down Column 28 to Row 15
# We need to move from 9 to 15 (6 steps Down)
for _ in range(6):
    pos = move(["Down"])

# Step 3: Walk Left to Column 24
# We need to move from 28 to 24 (4 steps Left)
for _ in range(4):
    pos = move(["Left"])

# Step 4: Walk UP to enter the elevator doors at (24, 14)
print("Entering elevator doors at (24, 14)...")
pos = move(["Up"])

print("Final position after script:", mgba.get_coordinates())
mgba.take_screenshot()
