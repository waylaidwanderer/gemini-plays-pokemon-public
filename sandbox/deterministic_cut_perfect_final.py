import mgba
import time

print("Clearing textbox...")
mgba.press_buttons(["B"])
time.sleep(0.5)

print("Turning RIGHT to face the bush...")
mgba.press_buttons(["Right"])
time.sleep(0.5)

print("Opening Start menu...")
mgba.press_buttons(["Start"])
time.sleep(0.5)

print("Entering POKéMON menu...")
mgba.press_buttons(["A"])
time.sleep(1.0)

print("Selecting TRUFFLE...")
mgba.press_buttons(["A"])
time.sleep(1.0)

print("Using CUT...")
mgba.press_buttons(["A"])
time.sleep(2.0)

print("Done!")
