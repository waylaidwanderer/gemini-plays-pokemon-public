import time
import bridge

print("Starting go_to_actual_gatehouse_v3.py...")

# Verify starting coordinates are (17, 24)
pos = bridge.get_coordinates()
print(f"Current coordinates outside: {pos}")
if pos != (17, 24):
    print("Warning: Not starting at (17, 24)!")

# Step 1: Walk to Column 22 Row 23
print("1. Walking to Column 22 Row 23...")
bridge.press_buttons(["Up"])
time.sleep(0.6)

for _ in range(5):
    bridge.press_buttons(["Right"])
    time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos} (should be (22, 23))")

# Step 2: Walk UP Column 22 to Row 14
print("2. Walking UP Column 22 to Row 14...")
for _ in range(9):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos} (should be (22, 14))")

# Step 3: Walk Right to Column 26
print("3. Walking RIGHT to Column 26...")
for _ in range(4):
    bridge.press_buttons(["Right"])
    time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos} (should be (26, 14))")

# Step 4: Use CUT on the bush at (26, 13)
print("4. Executing CUT menu sequence...")
bridge.press_buttons(["Up"])
time.sleep(0.6)

# Deterministic CUT menu sequence:
bridge.press_buttons(["Start"])
time.sleep(0.5)

for _ in range(10):
    bridge.press_buttons(["Up"])
    time.sleep(0.1)
time.sleep(0.3)

bridge.press_buttons(["Down"])
time.sleep(0.3)

bridge.press_buttons(["A"])
time.sleep(1.2)

# Select TRUFFLE (Down from SHELLBY)
bridge.press_buttons(["Down"])
time.sleep(0.5)
bridge.press_buttons(["A"])
time.sleep(1.2)

# Select CUT (Down from DIG)
bridge.press_buttons(["Down"])
time.sleep(0.5)

# Execute CUT
bridge.press_buttons(["A"])
time.sleep(3.0)

# Dismiss dialogue
bridge.press_buttons(["A"])
time.sleep(1.0)
bridge.press_buttons(["A"])
time.sleep(1.0)

# Step 5: Walk UP 5 steps to Row 9
print("5. Walking UP 5 steps to Row 9...")
for _ in range(5):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos} (should be (26, 9))")

# Step 6: Walk Right 11 steps to Column 37
print("6. Walking RIGHT 11 steps to Column 37...")
for _ in range(11):
    bridge.press_buttons(["Right"])
    time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos} (should be (37, 9))")

# Step 7: Walk Up 7 steps to Row 2
print("7. Walking UP 7 steps to Row 2...")
for _ in range(7):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos} (should be (37, 2))")

# Step 8: Walk Left 19 steps to Column 18
print("8. Walking LEFT 19 steps to Column 18...")
for _ in range(19):
    bridge.press_buttons(["Left"])
    time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos} (should be (18, 2))")

# Step 9: Walk Down 1 step to enter Gatehouse at (18, 3)
print("9. Entering Safari Gatehouse...")
bridge.press_buttons(["Down"])
time.sleep(2.5) # Wait for map transition

pos = bridge.get_coordinates()
print(f"Coordinates inside Safari Gatehouse: {pos}")
