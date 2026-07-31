import mgba
import time

# Get initial coordinates
pos = mgba.get_coordinates()
print(f"Initial Position: {pos}")

# Walk Right 5 steps from (12, 7) to (17, 7)
mgba.press_buttons(["Right", "Right", "Right", "Right", "Right"])
pos = mgba.get_coordinates()
print(f"After walking Right 5 steps: {pos}")

# Take a screenshot
screenshot_path = mgba.take_screenshot()
print(f"Screenshot taken: {screenshot_path}")

# Let's walk Right 4 more steps to see if the hallway continues
mgba.press_buttons(["Right", "Right", "Right", "Right"])
pos = mgba.get_coordinates()
print(f"After walking Right 4 more steps: {pos}")

# Take another screenshot
screenshot_path2 = mgba.take_screenshot()
print(f"Screenshot 2 taken: {screenshot_path2}")
