import mgba
import time

pos_before = mgba.get_coordinates()
print("Starting probe from:", pos_before)

# Try to move Right to (3, 6)
mgba.press_buttons(["Right"])
time.sleep(0.6)

pos_after = mgba.get_coordinates()
if pos_before == pos_after:
    print("STATE_A: True (Blocked at (2, 6) trying to move Right)")
else:
    print("STATE_B: True (Moved to", pos_after, ")")
    # Walk back to (2, 6)
    mgba.press_buttons(["Left"])
    time.sleep(0.6)
    print("Coordinates restored:", mgba.get_coordinates())
