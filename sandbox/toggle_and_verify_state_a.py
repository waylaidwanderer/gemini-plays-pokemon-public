import mgba
import time

# Stand at (2, 6) and face UP by pressing "Up" into the solid statue
print("Turning to face UP into the statue at (2, 5)...")
mgba.press_buttons(["Up"])
time.sleep(0.8)

# Full 4 A-press sequence with generous delays
for i in range(1, 5):
    print(f"Pressing A ({i}/4)...")
    mgba.press_buttons(["A"])
    time.sleep(2.0)

# Verify local state transition
print("Verifying State A is active...")
pos_before = mgba.get_coordinates()
print("Position before checking right movement:", pos_before)

mgba.press_buttons(["Right"])
time.sleep(0.6)

pos_after = mgba.get_coordinates()
print("Position after checking right movement:", pos_after)

if pos_before == pos_after:
    print("SUCCESS! State A is active (blocked from moving Right at (2, 6))!")
else:
    print("FAILED! Walked to", pos_after, ". We are still in State B.")
    # Walk back to (2, 6)
    mgba.press_buttons(["Left"])
    time.sleep(0.6)

mgba.take_screenshot()
