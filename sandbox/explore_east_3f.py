import mgba
import time

# Start at (10, 5) on 3F: Walk Right 4 steps to (14, 5)
mgba.press_buttons(["Right", "Right", "Right", "Right"])
time.sleep(1.2) # Wait for movement

pos = mgba.get_coordinates()
print("Position on 3F:", pos)
img_path = mgba.take_screenshot()
print("Saved screenshot on 3F:", img_path)
