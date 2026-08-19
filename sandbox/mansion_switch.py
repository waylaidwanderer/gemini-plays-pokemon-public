import mgba
import time

# We are at (3, 11) facing Left.
# Let's walk to (2, 12) to face UP towards the statue at (2, 11) and toggle it.
print("Walking to switch...")
mgba.press_buttons(["Down", "sleep 300", "Left", "sleep 300", "Up", "sleep 300", "A", "sleep 1000"])

pos = mgba.get_coordinates()
print(f"Coordinates: {pos}")

scr = mgba.take_screenshot()
print(f"Screenshot saved to: {scr}")
