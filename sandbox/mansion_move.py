import mgba
import time

# We are at (2, 12) on 3F in State B.
# Path to 3F pit:
# 1. Right 10 times -> (12, 12)
# 2. Up 5 times -> (12, 7)
# 3. Right 9 times -> (21, 7)
# 4. Up 3 times -> (21, 4)
# 5. Right 2 times -> (23, 4)
# 6. Down 2 times -> (23, 6) [pit that falls to 1F]

path = []
for _ in range(10):
    path.append("Right")
    path.append("sleep 100")
for _ in range(5):
    path.append("Up")
    path.append("sleep 100")
for _ in range(9):
    path.append("Right")
    path.append("sleep 100")
for _ in range(3):
    path.append("Up")
    path.append("sleep 100")
for _ in range(2):
    path.append("Right")
    path.append("sleep 100")
for _ in range(2):
    path.append("Down")
    path.append("sleep 100")

print("Executing path to 3F pit at (23, 6)...")
mgba.press_buttons(path)

pos = mgba.get_coordinates()
print(f"Coordinates: {pos}")

scr = mgba.take_screenshot()
print(f"Screenshot saved to: {scr}")
