# Let's check the moves of NIBBLES and NIDORAN via their Status screens!
# We start with the START menu open, cursor on POKEMON.
import mgba
import time

# 1. Open POKEMON menu
print("Opening POKEMON menu...")
mgba.press_buttons(["A"])
time.sleep(1.2)

# 2. Go to Slot 3 (NIBBLES)
print("Navigating to Slot 3...")
mgba.press_buttons(["Down", "sleep 100", "Down", "sleep 100", "A"])
time.sleep(1.0)

# 3. Select STATS (first option is STATS/STATS screen)
print("Selecting STATS for Slot 3...")
mgba.press_buttons(["A"])
time.sleep(1.2)

# 4. Press A to flip to the second page of STATS (which lists the moves!)
print("Flipping to Slot 3 moves page...")
mgba.press_buttons(["A"])
time.sleep(1.2)
mgba.take_screenshot() # Save screenshot of Slot 3 moves

# 5. Press B to exit STATS, and B to exit submenu
mgba.press_buttons(["B", "sleep 400", "B"])
time.sleep(1.0)

# 6. Go to Slot 5 (NIDORAN). From Slot 3, press Down twice to Slot 5.
print("Navigating to Slot 5...")
mgba.press_buttons(["Down", "sleep 100", "Down", "sleep 100", "A"])
time.sleep(1.0)

# 7. Select STATS for Slot 5
print("Selecting STATS for Slot 5...")
mgba.press_buttons(["A"])
time.sleep(1.2)

# 8. Press A to flip to the second page of STATS
print("Flipping to Slot 5 moves page...")
mgba.press_buttons(["A"])
time.sleep(1.2)
mgba.take_screenshot() # Save screenshot of Slot 5 moves

# 9. Exit all menus safely
mgba.press_buttons(["B", "sleep 400", "B", "sleep 400", "B", "sleep 400", "B"])
time.sleep(1.0)
print("Done!")
