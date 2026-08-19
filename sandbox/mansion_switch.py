import mgba
import time

# Current position is (22, 6) on 3F.
# Let's walk back to the 3F Mewtwo switch at (2, 11).
# Path:
# 1. Down to (22, 7)
# 2. Left 10 times to (12, 7)
# 3. Down 4 times to (12, 11)
# 4. Left 10 times to (2, 11)
# 5. Down to (2, 12)
# 6. Face UP (Up) and press A to toggle switch to State B!

path = []
path.append("Down")  # -> (22, 7)
for _ in range(10):
    path.append("Left")  # -> (12, 7)
for _ in range(4):
    path.append("Down")  # -> (12, 11)
for _ in range(10):
    path.append("Left")  # -> (2, 11)
path.append("Down")  # -> (2, 12)
path.append("Up")    # Turn UP to face the statue at (2, 11)
path.append("A")     # Toggle switch to State B

print("Executing path to switch...")
mgba.press_buttons(path)

# Print final coordinates to verify
pos = mgba.get_coordinates()
print(f"Coordinates after path: {pos}")

# Take screenshot to verify
scr = mgba.take_screenshot()
print(f"Screenshot saved to: {scr}")
