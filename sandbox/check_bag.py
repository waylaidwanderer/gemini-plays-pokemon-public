import mgba
import time

# Let's open the START menu, select ITEMS, and take a screenshot.
print("Opening Start Menu...")
mgba.press_buttons(["Start", "sleep 500", "Down", "sleep 200", "A", "sleep 1000"])

# Take a screenshot of the bag list
scr = mgba.take_screenshot()
print("Screenshot saved to:", scr)
