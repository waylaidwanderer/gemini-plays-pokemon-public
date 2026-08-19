import mgba
import time

# We are at (12, 10) on 2F in State B.
# Let's walk UP column 12 to (12, 6), then RIGHT across column 13 to (15, 6).
print("Walking to (15, 6) on 2F...")
mgba.press_buttons(["Up", "sleep 300", "Up", "sleep 300", "Up", "sleep 300", "Up", "sleep 300",
                    "Right", "sleep 300", "Right", "sleep 300", "Right", "sleep 1000"])

pos = mgba.get_coordinates()
print(f"Coordinates: {pos}")

scr = mgba.take_screenshot()
print(f"Screenshot saved to: {scr}")
