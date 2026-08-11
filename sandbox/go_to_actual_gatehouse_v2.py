import time
import bridge

print("Starting go_to_actual_gatehouse_v2.py...")

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

# Step 2: Face UP
print("2. Facing UP...")
bridge.press_buttons(["Up"])
time.sleep(0.6)

# Step 3: Use CUT on the bush at (26, 13)
print("3. Executing CUT menu sequence...")
# Menu sequence: Start -> A (POKéMON) -> Down (TRUFFLE) -> A -> Down (CUT) -> A -> A (dismiss text)
bridge.press_buttons([
    "Start", "sleep 500",
    "A", "sleep 1200",
    "Down", "sleep 500",
    "A", "sleep 1200",
    "Down", "sleep 500",
    "A", "sleep 3000",
    "A", "sleep 1000",
    "A", "sleep 1000"
])
time.sleep(1.5)

# Step 4: Walk UP 5 steps to Row 9
print("4. Walking UP 5 steps to Row 9...")
for _ in range(5):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos}")

# Step 5: Walk Right 11 steps to Column 37
print("5. Walking RIGHT 11 steps to Column 37...")
for _ in range(11):
    bridge.press_buttons(["Right"])
    time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos}")

# Step 6: Walk Up 7 steps to Row 2
print("6. Walking UP 7 steps to Row 2...")
for _ in range(7):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos}")

# Step 7: Walk Left 19 steps to Column 18
print("7. Walking LEFT 19 steps to Column 18...")
for _ in range(19):
    bridge.press_buttons(["Left"])
    time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos}")

# Step 8: Walk Down 1 step to enter Gatehouse at (18, 3)
print("8. Entering Safari Gatehouse...")
bridge.press_buttons(["Down"])
time.sleep(2.5) # Wait for map transition

pos = bridge.get_coordinates()
print(f"Coordinates inside Safari Gatehouse: {pos}")
