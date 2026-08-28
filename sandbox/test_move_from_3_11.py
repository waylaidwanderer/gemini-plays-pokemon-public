import mgba
import time

print("Starting position:", mgba.get_coordinates())
# Ensure menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

# Move down, left
mgba.press_buttons(["Down"])
time.sleep(0.5)
print("Position after Down:", mgba.get_coordinates())

mgba.press_buttons(["Left"])
time.sleep(0.5)
print("Position after Left:", mgba.get_coordinates())

screenshot_file = mgba.take_screenshot()
print("Screenshot saved to:", screenshot_file)
