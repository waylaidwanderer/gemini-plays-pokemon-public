import mgba
import time

pos_start = mgba.get_coordinates()
print(f"Start coordinates: ({pos_start['x']}, {pos_start['y']})")

# Move Right to (11, 6)
mgba.press_buttons(["Right"])
time.sleep(0.3)
pos_1 = mgba.get_coordinates()
print(f"After Right: ({pos_1['x']}, {pos_1['y']})")

# Move Up to (11, 5)
mgba.press_buttons(["Up"])
time.sleep(0.3)
pos_2 = mgba.get_coordinates()
print(f"After Up: ({pos_2['x']}, {pos_2['y']})")

screenshot_file = mgba.take_screenshot()
print(f"Screenshot taken: {screenshot_file}")
