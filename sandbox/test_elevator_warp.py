import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at: {pos}")

# Currently at (25, 8)
# Step 1: Walk Down to (25, 11)
for i in range(8, 11):
    pos = move(["Down"])

# Step 2: Walk Left to (24, 11)
pos = move(["Left"])

# Step 3: Walk Down into (24, 12)
pos = move(["Down"])

print("After step 3:", pos)
# Let's see if we warped to the elevator!
# Elevator map typically has coordinates like (x, y) around (1, 1) or (2, 2)
# If we warped, our coordinates will change significantly, or we will see map transition note.
mgba.take_screenshot()
