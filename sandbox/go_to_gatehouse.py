import time
import bridge

print("Starting go_to_gatehouse.py from (18, 13)...")

# Verify current position
pos = bridge.get_coordinates()
print(f"Current coordinates: {pos}")
if pos != (18, 13):
    print("Warning: Not starting at (18, 13)!")

# Step 1: Walk UP 4 steps to Row 9
print("1. Walking UP 4 steps to Row 9...")
for _ in range(4):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos}")

# Step 2: Walk RIGHT 6 steps to Column 24
print("2. Walking RIGHT 6 steps to Column 24...")
for _ in range(6):
    bridge.press_buttons(["Right"])
    time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos}")

# Step 3: Walk DOWN 5 steps to Row 14
print("3. Walking DOWN 5 steps to Row 14...")
for _ in range(5):
    bridge.press_buttons(["Down"])
    time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos}")

# Step 4: Walk LEFT 2 steps to Column 22
print("4. Walking LEFT 2 steps to Column 22...")
for _ in range(2):
    bridge.press_buttons(["Left"])
    time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos}")

# Step 5: Walk UP 1 step to enter Gatehouse
print("5. Entering Gatehouse...")
bridge.press_buttons(["Up"])
time.sleep(2.5) # Wait for map transition

pos = bridge.get_coordinates()
print(f"Coordinates inside Gatehouse: {pos}")
