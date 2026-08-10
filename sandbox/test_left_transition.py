import time
import bridge

print("Running test_left_transition.py")

# Walk Down to Row 36 from (6, 33)
print("Walking Down to Row 36...")
for i in range(3):
    bridge.press_buttons(["Down"])
    time.sleep(0.6)
print(f"Coords on Row 36: {bridge.get_coordinates()}")

# Walk Left along Row 36 to Column 0 to transition
print("Walking Left to transition to Area 3 (West)...")
for i in range(12): # Walk Left up to 12 times to make sure we transition
    bridge.press_buttons(["Left"])
    time.sleep(0.6)
    c = bridge.get_coordinates()
    print(f"Step {i+1} Coords: {c}")
