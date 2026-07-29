import mgba
import time

print("Exiting POKéMON menu...")
# Press B three times to get back to the overworld from "There isn't anything to CUT!"
for _ in range(3):
    mgba.press_buttons(["B"])
    time.sleep(0.5)

print("Turning DOWN to face the cuttable bush...")
# Press Down once in the overworld to face DOWN.
mgba.press_buttons(["Down"])
time.sleep(0.5)

print("Opening Start menu...")
mgba.press_buttons(["Start"])
time.sleep(0.5)

print("Entering POKéMON menu...")
# Start menu cursor points to POKéMON since we just exited from it.
mgba.press_buttons(["A"])
time.sleep(1.0)

print("Selecting TRUFFLE...")
# Cursor in party menu is at GUSTY (3rd). Press Up once to go to TRUFFLE (2nd).
mgba.press_buttons(["Up", "sleep 100", "A"])
time.sleep(1.0)

print("Selecting CUT...")
# TRUFFLE's sub-menu opens pointing at DIG (1st). Press Down once to go to CUT (2nd).
mgba.press_buttons(["Down", "sleep 100", "A"])
time.sleep(2.0)

print("Done!")
