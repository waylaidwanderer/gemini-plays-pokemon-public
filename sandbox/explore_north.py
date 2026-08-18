import mgba
import time

# Walk Left, Up 4, Right 3, Up 3
mgba.press_buttons(["Left", "Up", "Up", "Up", "Up", "Right", "Right", "Right", "Up", "Up", "Up"])
time.sleep(2.0) # Wait for movement

pos = mgba.get_coordinates()
print("New position in north 2F:", pos)
img_path = mgba.take_screenshot()
print("Saved screenshot:", img_path)
