import mgba
import time

# We are at (12, 11) on 2F in State B.
# Let's walk UP to (12, 10), then Right 3 times to (15, 10).
print("Walking to (15, 10) on 2F...")
mgba.press_buttons(["Up", "sleep 300", "Right", "sleep 300", "Right", "sleep 300", "Right", "sleep 1000"])

pos = mgba.get_coordinates()
print(f"Coordinates: {pos}")

scr = mgba.take_screenshot()
print(f"Screenshot saved to: {scr}")
