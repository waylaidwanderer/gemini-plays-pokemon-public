import mgba
import time

print("Current coordinates before moving:")
pos = mgba.get_coordinates()
print(pos)

# Let's take a single step UP to (5, 9) and see if we warp or what happens
print("Pressing Up...")
mgba.press_buttons(["Up", "sleep 1000"])

pos2 = mgba.get_coordinates()
print(f"Coordinates after Up: {pos2}")

scr = mgba.take_screenshot()
print(f"Screenshot saved to: {scr}")
