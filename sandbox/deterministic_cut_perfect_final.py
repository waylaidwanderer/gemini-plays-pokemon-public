import mgba
import time

print("Exiting POKéMON menu...")
# Press B three times to get back to the overworld from "Move POKéMON where?"
for _ in range(3):
    mgba.press_buttons(["B"])
    time.sleep(0.5)

print("Opening Start menu...")
mgba.press_buttons(["Start"])
time.sleep(0.5)

print("Entering POKéMON menu...")
mgba.press_buttons(["A"])
time.sleep(1.0)

print("Selecting TRUFFLE deterministically...")
# Park at SHELLBY (top), then go Down 1 to TRUFFLE
buttons = []
for _ in range(10):
    buttons.extend(["Up", "sleep 100"])
buttons.extend(["Down", "sleep 100", "A"])
mgba.press_buttons(buttons)
time.sleep(1.0)

print("Selecting CUT deterministically...")
# Park at CUT (top), then press A directly!
buttons = []
for _ in range(10):
    buttons.extend(["Up", "sleep 100"])
buttons.extend(["A"])
mgba.press_buttons(buttons)
time.sleep(2.0)

print("Done!")
