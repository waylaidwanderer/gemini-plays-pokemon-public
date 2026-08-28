import mgba
import time

print("Dismissing wild battle text...")
mgba.press_buttons(["B"])
time.sleep(1.0)
mgba.press_buttons(["B"])
time.sleep(1.0)

print("Selecting RUN...")
# In battle menu, Run is down-right or down-left?
# The battle menu has:
# FIGHT   BAG
# PKMN    RUN
# So RUN is Down-Right from FIGHT (top-left).
# Let's press Down, Right, A.
mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A"])
time.sleep(2.0)

# Dismiss run text
for i in range(5):
    mgba.press_buttons(["B"])
    time.sleep(0.4)

pos = mgba.get_coordinates()
print(f"Ended up at: {pos}")
mgba.take_screenshot()
