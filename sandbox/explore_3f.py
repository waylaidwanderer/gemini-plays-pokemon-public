import mgba
import time

# Start at (5, 2) on 3F: Walk Down 3 steps, Right 5 steps to (10, 5)
mgba.press_buttons(["Down", "Down", "Down", "Right", "Right", "Right", "Right", "Right"])
time.sleep(1.5)

pos = mgba.get_coordinates()
print("Position on 3F:", pos)
img_path = mgba.take_screenshot()
print("Saved screenshot on 3F:", img_path)
