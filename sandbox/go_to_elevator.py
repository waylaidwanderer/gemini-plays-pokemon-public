import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting position: {pos}")

# We are on B2F at (21, 9)
# Step 1: Walk Down to Row 14 (5 steps Down)
print("Walking down to Row 14...")
for _ in range(5):
    pos = move(["Down"])

# Step 2: Walk Right to Column 25 (4 steps Right)
print("Walking right to Column 25 through the gap at (23, 14)...")
for _ in range(4):
    pos = move(["Right"])

# Step 3: Walk Up 1 step into the B2F elevator warp at (25, 13)
print("Stepping into B2F elevator warp...")
pos = move(["Up"])

# Wait for map transition to Elevator
time.sleep(1)
pos = mgba.get_coordinates()
print(f"Position inside Elevator: {pos}")
mgba.take_screenshot()
