import mgba
import time

# Start at (18, 4) on B1F: Walk Down 2 steps, Left 4 steps to (14, 6)
mgba.press_buttons(["Down", "Down", "Left", "Left", "Left", "Left"])
time.sleep(1.5) # Wait for movement

pos = mgba.get_coordinates()
print("Position on B1F:", pos)
img_path = mgba.take_screenshot()
print("Saved screenshot on B1F:", img_path)
