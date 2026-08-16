import mgba
import time

print("--- EXITING GATEHOUSE AND GOING TO FUCHSIA CITY ---")

def get_pos():
    return mgba.get_coordinates()

# Current position is (4, 0) with "Did you get a / good haul?" on screen.
# 1. Clear clerk's dialogue
print("Clearing clerk's dialogue...")
mgba.press_buttons(["A"])
time.sleep(1.0)
mgba.press_buttons(["A"])
time.sleep(1.0)
mgba.press_buttons(["A"])
time.sleep(1.0)

# 2. Walk to the exit at (3, 5):
# - Walk Down 3 steps to (4, 3)
# - Walk Left 1 step to (3, 3)
# - Walk Down 2 steps to (3, 5) (warp)
print("Walking to exit...")
mgba.press_buttons(["Down", "sleep 350", "Down", "sleep 350", "Down"])
time.sleep(1.0)
mgba.press_buttons(["Left"])
time.sleep(1.0)
mgba.press_buttons(["Down", "sleep 350", "Down"])
time.sleep(2.0) # wait for transition

print("Position after transition:", get_pos())
mgba.take_screenshot()
