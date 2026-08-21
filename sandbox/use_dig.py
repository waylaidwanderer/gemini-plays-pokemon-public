import mgba
import time

print("Opening start menu...")
mgba.press_buttons(["Start"])
time.sleep(0.5)

print("Moving to POKéMON...")
mgba.press_buttons(["Down"])
time.sleep(0.2)

print("Opening POKéMON party menu...")
mgba.press_buttons(["A"])
time.sleep(1.0)

mgba.take_screenshot()
print("Screenshot taken of party menu!")
