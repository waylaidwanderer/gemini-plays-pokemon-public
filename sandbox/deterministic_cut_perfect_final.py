import mgba
import time

print("Exiting POKéMON menu...")
# Press B three times to get back to the overworld from "There isn't anything to CUT!"
for _ in range(3):
    mgba.press_buttons(["B"])
    time.sleep(0.5)

print("Turning DOWN to face the cuttable bush...")
# Press Down once in the overworld. Since (40, 11) is blocked by the bush,
# we will bump and remain at (40, 10), but we will now be facing DOWN.
mgba.press_buttons(["Down"])
time.sleep(0.5)

print("Opening Start menu...")
mgba.press_buttons(["Start"])
time.sleep(0.5)

print("Entering POKéMON menu...")
# Start menu cursor points to POKéMON since we just exited from it.
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
# Park at DIG (top), then go Down 1 to CUT
buttons = []
for _ in range(10):
    buttons.extend(["Up", "sleep 100"])
buttons.extend(["Down", "sleep 100", "A"])
mgba.press_buttons(buttons)
time.sleep(2.0)

print("Done!")
