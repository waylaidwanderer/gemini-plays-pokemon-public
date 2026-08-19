import mgba
import time

# We are at (9, 9) on 2F.
# Let's walk to the stairs at (7, 10) to warp to 1F.
print("Walking to (7, 10) stairs...")
# Path from (9, 9): Left to (8, 9), Left to (7, 9), Down to (7, 10).
mgba.press_buttons(["Left", "sleep 300", "Left", "sleep 300", "Down", "sleep 1000"])

pos1 = mgba.get_coordinates()
print(f"Coordinates after first warp: {pos1}")
mgba.take_screenshot()
