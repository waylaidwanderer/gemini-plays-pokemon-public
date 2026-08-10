import time
import bridge

print("Running go_to_gatehouse.py from (2, 11)...")

# Current position: (2, 11) facing LEFT
# Step 1: Walk LEFT to Column 1
print("1. Walking LEFT to Column 1...")
bridge.press_buttons(["Left"])
time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords: {coords}")

# Step 2: Walk DOWN to Row 14
print("2. Walking DOWN to Row 14...")
for _ in range(3):
    bridge.press_buttons(["Down"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords: {coords}")

# Step 3: Walk RIGHT to Column 26
print("3. Walking RIGHT to Column 26...")
for _ in range(25):
    bridge.press_buttons(["Right"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords: {coords}")

# Step 4: Walk UP Column 26 to Row 9
print("4. Walking UP Column 26 to Row 9...")
for _ in range(5):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords: {coords}")

# Step 5: Walk LEFT to Column 19
print("5. Walking LEFT along Row 9 to Column 19...")
for _ in range(7):
    bridge.press_buttons(["Left"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords: {coords}")

# Step 6: Walk UP to Row 8
print("6. Walking UP Column 19 to Row 8...")
bridge.press_buttons(["Up"])
time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords: {coords}")

# Step 7: Walk RIGHT to Column 37
print("7. Walking RIGHT along Row 8/9 to Column 37...")
for _ in range(18):
    bridge.press_buttons(["Right"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords: {coords}")

# Step 8: Walk UP Column 37 to Row 2
print("8. Walking UP Column 37 to Row 2...")
for _ in range(6):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords: {coords}")

# Step 9: Walk LEFT along Row 2 to Column 22
print("9. Walking LEFT along Row 2 to Column 22...")
for _ in range(15):
    bridge.press_buttons(["Left"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords: {coords}")

# Step 10: Walk DOWN Column 22 to Row 4
print("10. Walking DOWN Column 22 to Row 4...")
for _ in range(2):
    bridge.press_buttons(["Down"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords: {coords}")

# Step 11: Walk UP to enter Gatehouse
print("11. Entering Gatehouse...")
bridge.press_buttons(["Up"])
time.sleep(2.0) # Wait for transition loading

coords = bridge.get_coordinates()
print(f"Coords inside Gatehouse: {coords}")

