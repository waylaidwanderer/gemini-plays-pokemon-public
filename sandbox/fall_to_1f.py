import mgba
import time

# Start at (19, 6) on 2F: Walk Right 4 steps to fall through the pit at (23, 6) to 1F
mgba.press_buttons(["Right", "Right", "Right", "Right"])
time.sleep(2.5) # Wait for fall animation and transition to 1F to complete

pos = mgba.get_coordinates()
print("Position after falling to 1F:", pos)
img_path = mgba.take_screenshot()
print("Saved screenshot on 1F:", img_path)
