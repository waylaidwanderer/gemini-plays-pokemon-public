import mgba
import time

# We are at (2, 12) facing UP, with "A secret switch!" on screen.
# Let's advance the dialogue and select YES to press the switch.
print("Toggling switch...")
mgba.press_buttons(["A", "sleep 300", "A", "sleep 300", "A", "sleep 1000"])

pos = mgba.get_coordinates()
print(f"Coordinates after switch toggle: {pos}")

scr = mgba.take_screenshot()
print(f"Screenshot saved to: {scr}")
