import mgba
import time

print("Advancing text...")
mgba.press_buttons(["A"])
time.sleep(1.5)

print("Selecting RUN...")
# Down, Right, A
mgba.press_buttons(["Down", "Right", "A"])
time.sleep(1.5)

print("Dismissing escape message...")
mgba.press_buttons(["B"])
time.sleep(0.8)

print("Position after escape:", mgba.get_coordinates())
