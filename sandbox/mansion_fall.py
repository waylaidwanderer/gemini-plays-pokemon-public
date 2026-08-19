import mgba
import time

# Current position is (22, 7) on 3F in State A.
# Let's walk UP to (22, 6), then RIGHT to (23, 6).
print("Starting sequence...")
mgba.press_buttons(["Up", "sleep 300", "Right", "sleep 1000"])

# Let's get coordinates after the fall.
pos = mgba.get_coordinates()
print(f"Coordinates after fall: {pos}")

# Take a screenshot to verify the landing spot.
scr = mgba.take_screenshot()
print(f"Screenshot saved to: {scr}")
