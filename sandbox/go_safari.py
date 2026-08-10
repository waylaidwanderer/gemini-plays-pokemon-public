import time
import bridge

print("Running go_safari.py - Realigning to Area 2 (North) and transitioning LEFT")

# Current position: (18, 18) inside Safari Zone Center.
# Step 1: Walk Right to Column 27
print("Walking Right to Column 27...")
for i in range(9): # 18 to 27 is 9 steps
    bridge.press_buttons(["Right"])
    time.sleep(0.6)
print(f"Coords after Right: {bridge.get_coordinates()}")

# Step 2: Walk Up to (27, 0)
print("Walking Up to (27, 0)...")
for i in range(18): # 18 to 0 is 18 steps
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
print(f"Coords after Up: {bridge.get_coordinates()}")

# Step 3: Walk Up 1 more to transition to Area 2 (North) at (9, 35)
print("Transitioning Up to Area 2 (North)...")
bridge.press_buttons(["Up"])
time.sleep(1.0)
coords = bridge.get_coordinates()
print(f"Coords after transition: {coords}")

# Step 4: From (9, 35), walk to (12, 33)
# To go from (9, 35) to (12, 33):
# - Walk Right 3 steps to (12, 35)
# - Walk Up 2 steps to (12, 33)
print("Walking to (12, 33)...")
for _ in range(3):
    bridge.press_buttons(["Right"])
    time.sleep(0.6)
for _ in range(2):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
print(f"Coords: {bridge.get_coordinates()}")

# Step 5: Walk Left from (12, 33) to transition to Area 3 (West)
print("Walking Left to transition to Area 3 (West)...")
for i in range(13): # 12 to 0, then 1 more to transition
    bridge.press_buttons(["Left"])
    time.sleep(0.6)
    c = bridge.get_coordinates()
    print(f"Step {i+1} Coords: {c}")
