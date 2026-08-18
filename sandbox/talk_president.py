import mgba
import time

# We start at (6, 9)
# Move UP to (6, 7)
print("Moving Up to (6, 8)...")
mgba.press_buttons(["Up"])
time.sleep(0.3)

print("Moving Up to (6, 7)...")
mgba.press_buttons(["Up"])
time.sleep(0.3)

# Face RIGHT and speak
print("Facing RIGHT and pressing A...")
mgba.press_buttons(["Right"])
time.sleep(0.3)
mgba.press_buttons(["A"])
time.sleep(0.5)

screenshot_file = mgba.take_screenshot()
print(f"Screenshot taken: {screenshot_file}")
