import mgba
import time

# We are at (22, 6) facing UP on 3F.
# Let's press Right and see if we fall!
print("Pressing Right...")
mgba.press_buttons(["Right", "sleep 1000"])

pos = mgba.get_coordinates()
print(f"Coordinates after Right: {pos}")

scr = mgba.take_screenshot()
print(f"Screenshot saved to: {scr}")
