import mgba
import time

print("Fleeing battle...")
# 1. Clear "Wild PONYTA appeared!" text
mgba.press_buttons(["B"])
time.sleep(1.0)

# 2. Press Down, Right, A to RUN
mgba.press_buttons(["Down", "Right", "A"])
time.sleep(2.0)

# 3. Clear "Got away safely!" text
mgba.press_buttons(["B"])
time.sleep(1.0)

pos = mgba.get_coordinates()
print("Current Position after fleeing:", pos)
mgba.take_screenshot()
