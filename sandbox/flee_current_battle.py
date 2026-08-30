import mgba
import time

print("Dismissing 'No PP Left...' text...")
mgba.press_buttons(["B"])
time.sleep(1.0)

print("Returning to main battle menu...")
mgba.press_buttons(["B"])
time.sleep(1.0)

print("Selecting RUN...")
mgba.press_buttons(["Down", "Right", "A"])
time.sleep(1.5)

print("Dismissing escape message...")
mgba.press_buttons(["B"])
time.sleep(0.8)

print("Position after escape:", mgba.get_coordinates())
