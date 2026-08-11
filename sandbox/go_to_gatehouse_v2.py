import time
import bridge

print("Starting go_to_gatehouse_v2.py from (22, 14)...")

# Verify current position is (22, 14)
pos = bridge.get_coordinates()
print(f"Current coordinates outside: {pos}")
if pos != (22, 14):
    print("Warning: Not starting at (22, 14)!")

# Step 1: Walk Right 4 steps to Column 26
print("1. Walking RIGHT to Column 26...")
for _ in range(4):
    bridge.press_buttons(["Right"])
    time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos}")

# Step 2: Walk Up 5 steps to Row 9
print("2. Walking UP to Row 9...")
for _ in range(5):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos}")

# Step 3: Walk Left 7 steps to Column 19
print("3. Walking LEFT to Column 19...")
for _ in range(7):
    bridge.press_buttons(["Left"])
    time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos}")

# Step 4: Walk Up 1 step to Row 8
print("4. Walking UP to Row 8...")
bridge.press_buttons(["Up"])
time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos}")

# Step 5: Walk Right 18 steps to Column 37
print("5. Walking RIGHT to Column 37...")
for _ in range(18):
    bridge.press_buttons(["Right"])
    time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos}")

# Step 6: Walk Up 6 steps to Row 2
print("6. Walking UP to Row 2...")
for _ in range(6):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos}")

# Step 7: Walk Left 19 steps to Column 18 (verified gatehouse door column)
print("7. Walking LEFT to Column 18...")
for _ in range(19):
    bridge.press_buttons(["Left"])
    time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos}")

# Step 8: Walk Down 2 steps to Row 4
print("8. Walking DOWN to Row 4...")
for _ in range(2):
    bridge.press_buttons(["Down"])
    time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos}")

# Step 9: Walk Up 1 step to enter Gatehouse at (18, 3)
print("9. Entering Gatehouse...")
bridge.press_buttons(["Up"])
time.sleep(2.5) # Wait for map transition

pos = bridge.get_coordinates()
print(f"Coordinates inside Gatehouse: {pos}")
