import mgba
import time

print("Fleeing from the battle step-by-step...")
# 1. Dismiss "No PP left for this move!"
mgba.press_buttons(["B"])
time.sleep(0.5)

# 2. Exit move list to main menu
mgba.press_buttons(["B"])
time.sleep(0.5)

# 3. Select RUN (which is at bottom-right)
# In the battle menu:
# Top-Left: FIGHT, Bottom-Left: PKMN
# Top-Right: ITEM, Bottom-Right: RUN
# From FIGHT, pressing Down goes to PKMN, then Right goes to RUN.
# Let's press Down then Right.
mgba.press_buttons(["Down", "Right"])
time.sleep(0.5)

# 4. Press A to run
mgba.press_buttons(["A"])
time.sleep(1.5)

# 5. Dismiss any potential text
for _ in range(5):
    mgba.press_buttons(["B"])
    time.sleep(0.2)

print("Flee script completed.")
