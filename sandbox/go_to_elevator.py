import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

# We are in the ITEMS menu at (25, 12).
# Let's close the menu by pressing B 3 times
print("Closing item menu...")
for _ in range(3):
    move(["B"])

# Let's verify we are back in the overworld at (25, 12)
pos = mgba.get_coordinates()
print(f"Overworld position: {pos}")

# Walk Down 2 steps to (25, 14)
print("Walking down to Row 14...")
for _ in range(2):
    pos = move(["Down"])

# Walk Left 1 step to (24, 14)
print("Walking left to Column 24...")
pos = move(["Left"])

# Walk Up 1 step to (24, 13) to warp into the elevator!
print("Stepping into LEFT elevator warp at (24, 13)...")
pos = move(["Up"])

# Wait for transition
time.sleep(1)
pos = mgba.get_coordinates()
print(f"Final position inside Elevator: {pos}")
mgba.take_screenshot()
