import mgba
import time

# Start at (14, 6) on B1F: Walk Left 4 steps, Up 3 steps to (10, 3)
mgba.press_buttons(["Left", "Left", "Left", "Left", "Up", "Up", "Up"])
time.sleep(1.5) # Wait for movement

pos = mgba.get_coordinates()
print("Position on B1F:", pos)
img_path = mgba.take_screenshot()
print("Saved screenshot on B1F:", img_path)
