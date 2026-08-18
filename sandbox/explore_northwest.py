import mgba
import time

# From (11, 6): Walk Up, Left 4, Up 2 to (7, 3)
mgba.press_buttons(["Up", "Left", "Left", "Left", "Left", "Up", "Up"])
time.sleep(1.5)

pos = mgba.get_coordinates()
print("Position in northwest room:", pos)
img_path = mgba.take_screenshot()
print("Saved screenshot:", img_path)
