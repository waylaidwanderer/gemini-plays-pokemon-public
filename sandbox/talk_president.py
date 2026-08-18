import mgba
import time

# Current position is (7, 9)
# Move to (7, 10)
print("Moving Down to (7, 10)...")
mgba.press_buttons(["Down"])
time.sleep(0.3)

# Move to (6, 10)
print("Moving Left to (6, 10)...")
mgba.press_buttons(["Left"])
time.sleep(0.3)

# Face UP and speak
print("Facing UP to (6, 9) and pressing A...")
mgba.press_buttons(["Up"])
time.sleep(0.3)
mgba.press_buttons(["A"])
time.sleep(0.5)

screenshot_file = mgba.take_screenshot()
print(f"Screenshot taken: {screenshot_file}")
