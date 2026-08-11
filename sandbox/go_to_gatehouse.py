import time
import bridge

print("Starting go_to_gatehouse.py...")

# Verify start position (19, 28)
pos = bridge.get_coordinates()
print(f"Current coordinates: {pos}")
if pos != (19, 28):
    print("Warning: Not starting at (19, 28)!")

# Step 1: Walk Right to Column 24
print("Step 1: Walking Right to Column 24...")
for _ in range(5):
    bridge.press_buttons(["Right"])
    time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos}")

# Step 2: Walk Up to Row 21
print("Step 2: Walking Up to Row 21...")
for _ in range(7):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos}")

# Step 3: Walk Left to Column 22
print("Step 3: Walking Left to Column 22...")
for _ in range(2):
    bridge.press_buttons(["Left"])
    time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos}")

# Step 4: Walk Up to Row 14
print("Step 4: Walking Up to Row 14...")
for _ in range(7):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos}")

# Step 5: Walk Right to Column 26
print("Step 5: Walking Right to Column 26...")
for _ in range(4):
    bridge.press_buttons(["Right"])
    time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos} (should be (26, 14))")

# Step 6: Use CUT on the bush at (26, 13)
# We must stand at (26, 14) facing UP
print("Step 6: Facing UP and using CUT...")
bridge.press_buttons(["Up"])
time.sleep(0.6)

# Execute CUT menu sequence
# Menu: Start -> Down (PKMN) -> A -> Down (TRUFFLE) -> A -> A (CUT)
bridge.press_buttons([
    "Start", "sleep 300",
    "Down", "sleep 300",
    "A", "sleep 800",
    "Down", "sleep 300",
    "A", "sleep 800",
    "A", "sleep 2000"
])
time.sleep(1.0)

# Dismiss the "TRUFFLE hacked away with CUT!" or similar text
bridge.press_buttons(["A", "sleep 500", "A"])
time.sleep(1.5)

pos = bridge.get_coordinates()
print(f"Coordinates after CUT: {pos}")

# Step 7: Walk Up Column 26 to Row 9
print("Step 7: Walking UP to Row 9...")
for _ in range(5):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos}")

# Step 8: Walk Left to Column 19
print("Step 8: Walking Left to Column 19...")
for _ in range(7):
    bridge.press_buttons(["Left"])
    time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos}")

# Step 9: Walk Up to Row 8
print("Step 9: Walking Up to Row 8...")
bridge.press_buttons(["Up"])
time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos}")

# Step 10: Walk Right to Column 37
print("Step 10: Walking Right to Column 37...")
for _ in range(18):
    bridge.press_buttons(["Right"])
    time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos}")

# Step 11: Walk Up to Row 2
print("Step 11: Walking Up to Row 2...")
for _ in range(6):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos}")

# Step 12: Walk Left to Column 22
print("Step 12: Walking Left to Column 22...")
for _ in range(15):
    bridge.press_buttons(["Left"])
    time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos}")

# Step 13: Walk Down to Row 4
print("Step 13: Walking Down to Row 4...")
for _ in range(2):
    bridge.press_buttons(["Down"])
    time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos}")

# Step 14: Walk Up to enter Gatehouse
print("Step 14: Entering Gatehouse...")
bridge.press_buttons(["Up"])
time.sleep(2.5)

pos = bridge.get_coordinates()
print(f"Coordinates inside Gatehouse: {pos}")
