import time
import bridge

print("Running go_into_safari.py (Fuchsia overworld -> Safari Zone)...")

# Current position: (22, 8) facing UP
# Step 1: Walk UP 2 steps to Row 6
print("Walking UP to Row 6...")
for _ in range(2):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords: {coords}")

# Step 2: Walk LEFT 3 steps to Column 19
print("Walking LEFT to Column 19...")
for _ in range(3):
    bridge.press_buttons(["Left"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords: {coords}")

# Step 3: Walk UP 2 steps to enter Gatehouse (warp)
print("Entering Gatehouse...")
for _ in range(2):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
time.sleep(2.0) # Wait for map transition loading

coords = bridge.get_coordinates()
print(f"Coords inside Gatehouse: {coords}")

# Step 4: Walk UP 2 steps to the clerk
print("Walking UP to the clerk...")
for _ in range(2):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)

print("Paying 500 and buying Safari Balls...")
# Dialogue box 1: Welcome message
bridge.press_buttons(["A"])
time.sleep(0.6)

# Select YES to join the hunt (default)
bridge.press_buttons(["A"])
time.sleep(0.6)

# Dialogue box 2: That'll be 500
bridge.press_buttons(["A"])
time.sleep(0.6)

# Dialogue box 3: Received 30 balls
bridge.press_buttons(["A"])
time.sleep(0.6)

# Dialogue box 4: We'll call you on the PA
bridge.press_buttons(["A"])
time.sleep(0.6)

# Dialogue box 5: Best of luck!
bridge.press_buttons(["A"])
time.sleep(1.2) # Wait for textbox to close completely

# Step 5: Walk UP to enter the Safari Zone Center
print("Entering the Safari Zone with a fresh 500 steps!")
bridge.press_buttons(["Up"])
time.sleep(2.0) # Wait for transition load

coords = bridge.get_coordinates()
print(f"Final coordinates inside Safari Zone Center: {coords}")

