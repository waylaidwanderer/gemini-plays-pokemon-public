import mgba
import time

# Start at (7, 3): Walk Left 2 steps, Up 2 steps to go onto the stairs at (5, 1)
mgba.press_buttons(["Left", "Left", "Up", "Up"])
time.sleep(1.2) # Wait for map transition

pos = mgba.get_coordinates()
print("Position on 3F:", pos)
img_path = mgba.take_screenshot()
print("Saved screenshot on 3F:", img_path)
