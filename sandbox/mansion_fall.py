import mgba
import time

# We are at (2, 12) on 3F, in State B.
# Path to 3F pit:
# 1. Right 10 times -> (12, 12)
# 2. Up 5 times -> (12, 7)
# 3. Right 10 times -> (22, 7)
# 4. Up -> (22, 6)
# 5. Left -> (21, 6)
# 6. Up -> (21, 5) [open gate in State B]
# 7. Up -> (21, 4)
# 8. Right 3 times -> (24, 4)
# 9. Down -> (24, 5) [pit that falls to 2F]

path = []
for _ in range(10):
    path.append("Right")
for _ in range(5):
    path.append("Up")
for _ in range(10):
    path.append("Right")
path.append("Up")
path.append("Left")
path.append("Up")
path.append("Up")
for _ in range(3):
    path.append("Right")
path.append("Down")

print("Executing path to fall through 3F pit...")
mgba.press_buttons(path)

# Print final coordinates to verify where we land
pos = mgba.get_coordinates()
print(f"Coordinates after fall: {pos}")

# Take screenshot to verify
scr = mgba.take_screenshot()
print(f"Screenshot saved to: {scr}")
