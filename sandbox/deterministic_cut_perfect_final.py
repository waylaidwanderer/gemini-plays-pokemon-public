import mgba
import time

print("Turning DOWN to face the cuttable bush...")
mgba.press_buttons(["Down"])
time.sleep(0.5)

print("Opening Start menu...")
mgba.press_buttons(["Start"])
time.sleep(1.0)

print("Entering POKéMON menu...")
mgba.press_buttons(["A"])
time.sleep(1.0)

print("Selecting TRUFFLE...")
mgba.press_buttons(["Up", "sleep 200", "A"])
time.sleep(1.0)

print("Selecting CUT...")
mgba.press_buttons(["Down", "sleep 200", "A"])
time.sleep(2.0)

print("Done!")
