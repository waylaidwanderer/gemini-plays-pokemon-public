import mgba
import time

print("Opening Start menu...")
mgba.press_buttons(["Start"])
time.sleep(1.0) # Increased delay to be absolutely safe

print("Entering POKéMON menu...")
mgba.press_buttons(["A"])
time.sleep(1.0)

print("Selecting TRUFFLE...")
# Cursor in party menu is at GUSTY (3rd). Press Up once to go to TRUFFLE (2nd).
mgba.press_buttons(["Up", "sleep 200", "A"])
time.sleep(1.0)

print("Selecting CUT...")
# TRUFFLE's sub-menu opens pointing at DIG (1st). Press Down once to go to CUT (2nd).
mgba.press_buttons(["Down", "sleep 200", "A"])
time.sleep(2.0)

print("Done!")
