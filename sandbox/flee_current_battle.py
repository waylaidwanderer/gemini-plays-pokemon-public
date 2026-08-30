import mgba
import time

print("Clearing 'Wild PONYTA appeared!' text...")
mgba.press_buttons(["A"])
time.sleep(1.5)

print("Clearing summon text...")
mgba.press_buttons(["A"])
time.sleep(2.0)

print("Selecting RUN...")
mgba.press_buttons(["Down", "Right", "A"])
time.sleep(1.5)

print("Dismissing escape message...")
mgba.press_buttons(["B"])
time.sleep(0.8)

print("Current overworld position:", mgba.get_coordinates())
