import mgba
import time

# 1. Close stats/switch menu
print("Closing stats menu...")
mgba.press_buttons(["B"])
time.sleep(1.0)

# 2. Close party menu to return to main battle menu
print("Closing party menu...")
mgba.press_buttons(["B"])
time.sleep(1.0)

# 3. Select RUN and press A (from PKMN, Down goes to RUN)
print("Selecting RUN...")
mgba.press_buttons(["Down", "sleep 250", "A"])
time.sleep(2.5)

# 4. Dismiss "Got away safely!" text
print("Dismissing escape text...")
mgba.press_buttons(["A"])
time.sleep(1.0)

print("Coordinates after escape:", mgba.get_coordinates())
