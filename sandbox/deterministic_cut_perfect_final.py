import mgba
import time

print("Opening Start menu...")
mgba.press_buttons(["Start"])
time.sleep(0.5)

print("Entering POKéMON menu...")
mgba.press_buttons(["A"])
time.sleep(1.0)

print("Selecting TRUFFLE...")
mgba.press_buttons(["A"])
time.sleep(1.0)

print("Selecting CUT...")
# Sub-menu doesn't wrap. Park at top (DIG), then Down 1 to CUT
buttons = []
for _ in range(10):
    buttons.extend(["Up", "sleep 100"])
buttons.extend(["Down", "sleep 100", "A"])
mgba.press_buttons(buttons)
time.sleep(2.0)

print("Done!")
