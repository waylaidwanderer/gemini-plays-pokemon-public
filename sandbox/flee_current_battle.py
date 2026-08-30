import mgba
import time

print("Fleeing battle with proper sleep delays between buttons...")

# 1. Clear any text or make sure menu is ready
mgba.press_buttons(["B"])
time.sleep(0.8)

# 2. Press Down, sleep, Right, sleep, A to RUN
mgba.press_buttons(["Down", "sleep 300", "Right", "sleep 300", "A"])
time.sleep(2.0)

# 3. Dismiss "Got away safely!" text
mgba.press_buttons(["B"])
time.sleep(1.0)

print("Coordinates:", mgba.get_coordinates())
mgba.take_screenshot()
