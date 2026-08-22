import mgba
import time

# Use DIG to escape from the Mansion to Cinnabar Island outside (State A)
print("Opening Start Menu...")
mgba.press_buttons(["Start"])
time.sleep(0.8)

print("Selecting PKMN...")
mgba.press_buttons(["Down", "A"])
time.sleep(1.0)

print("Selecting TRUFFLE (6th PKMN)...")
# TRUFFLE is 6th in our party, so press Down 5 times from top slot
for _ in range(5):
    mgba.press_buttons(["Down"])
    time.sleep(0.1)
mgba.press_buttons(["A"])
time.sleep(0.8)

print("Selecting DIG...")
# TRUFFLE's option 1 is DIG, so press A
mgba.press_buttons(["A"])
time.sleep(1.0)

print("Confirming DIG...")
mgba.press_buttons(["A"])
time.sleep(4.0)

print("Warped outside Cinnabar Island! Final position:", mgba.get_coordinates())
mgba.take_screenshot()
