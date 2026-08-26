# Let's inspect our party Pokémon to see who has DIG!
# In Pokémon Blue, we can open the menu and look at the Pokémon,
# but we can also just run a script that opens the POKéMON menu, selects the first, second, etc.
# and check if DIG is an available field move.
# But wait! We can just write a script that opens the START menu, goes to POKéMON,
# and checks the moves.
# Actually, let's look at Progression_And_Party_Stats.md:
# "Slot 5: NIDORAN♀ (Nidoran-F) - Level 25."
# Wait, did Nidoran or Rattata learn DIG?
# Let's check if NIBBLES (Rattata) has DIG or if NIDORAN♀ has DIG.
# We can open the START menu, select POKéMON, and check the moves of each!
# But wait, let's write a python script to open the START menu, go to POKéMON, and press A on each slot to see if "DIG" is an option in the menu!
# If we stand on the overworld, we can do this safely.

import mgba
import time

print("Opening START menu...")
mgba.press_buttons(["Start"])
time.sleep(1.0)

# Move down to POKéMON (POKéMON is slot 2, after POKéDEX. Wait, do we have POKéDEX? Yes, so POKéMON is slot 2).
# Let's press Down once from POKéDEX to POKéMON.
# Let's verify by pressing Down and then A.
mgba.press_buttons(["Down", "sleep 200", "A"])
time.sleep(1.5)

# Now we are on the Pokémon Party list screen!
# Slot 1 is SHELLBY (Blastoise)
# Slot 2 is GUSTY (Pidgey)
# Slot 3 is NIBBLES (Rattata)
# Slot 4 is TESLA (Pikachu)
# Slot 5 is NIDORAN♀ (Nidoran-F)
# Let's check each slot by pressing A, and then looking at the options (like STATUS/SWITCH, or FIELD MOVES like CUT/DIG/FLY).
# If a Pokémon has DIG, it will show "DIG" at the top of the menu!
# Let's check Slot 3 (NIBBLES) first. Press Down twice to reach Slot 3, then press A.
print("Checking Slot 3 (NIBBLES)...")
mgba.press_buttons(["Down", "sleep 100", "Down", "sleep 100", "A"])
time.sleep(1.2)
mgba.take_screenshot() # We'll save and examine this later if needed

# Press B to go back
mgba.press_buttons(["B"])
time.sleep(0.8)

# Let's check Slot 5 (NIDORAN♀). From Slot 3, press Down twice to reach Slot 5, then press A.
print("Checking Slot 5 (NIDORAN♀)...")
mgba.press_buttons(["Down", "sleep 100", "Down", "sleep 100", "A"])
time.sleep(1.2)
mgba.take_screenshot()

# Press B to go back, and B again to close the Party menu, and B to close the START menu
mgba.press_buttons(["B", "sleep 400", "B", "sleep 400", "B"])
time.sleep(1.0)
print("Finished checking!")
