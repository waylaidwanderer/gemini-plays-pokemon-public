import mgba
import time

# Let's open the START menu, go to POKéMON, and inspect the screen
mgba.press_buttons(["Start", "sleep 500", "Down", "A", "sleep 500"])
time.sleep(1.5)

screenshot_file = mgba.take_screenshot()
print(f"Party menu opened. Screenshot saved as {screenshot_file}")
