import mgba
import time

# We are at (7, 10) on 2F facing UP.
# Let's walk Left 2 times onto the staircase at (5, 10) and see if we warp to 3F!
print("Stepping onto (5, 10) stairs from the East side...")
mgba.press_buttons(["Left", "sleep 300", "Left", "sleep 1000"])

pos = mgba.get_coordinates()
print(f"Coordinates: {pos}")

scr = mgba.take_screenshot()
print(f"Screenshot saved to: {scr}")
