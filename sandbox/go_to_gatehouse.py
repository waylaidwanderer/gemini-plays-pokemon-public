import time
import bridge

print("Starting go_to_gatehouse.py from (18, 9)...")

# Verify current position
pos = bridge.get_coordinates()
print(f"Current coordinates: {pos}")
if pos != (18, 9):
    print("Warning: Not starting at (18, 9)!")

# Step 1: Walk RIGHT 8 steps to Column 26
print("1. Walking RIGHT 8 steps to Column 26...")
for _ in range(8):
    bridge.press_buttons(["Right"])
    time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos}")

# Step 2: Walk DOWN 5 steps to Row 14
print("2. Walking DOWN 5 steps to Row 14...")
for _ in range(5):
    bridge.press_buttons(["Down"])
    time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos}")

# Step 3: Walk LEFT 4 steps to Column 22
print("3. Walking LEFT 4 steps to Column 22...")
for _ in range(4):
    bridge.press_buttons(["Left"])
    time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos}")

# Step 4: Walk UP 1 step to enter Gatehouse at (22, 13)
print("4. Entering Gatehouse...")
bridge.press_buttons(["Up"])
time.sleep(2.5) # Wait for map transition

pos = bridge.get_coordinates()
print(f"Coordinates inside Gatehouse: {pos}")
