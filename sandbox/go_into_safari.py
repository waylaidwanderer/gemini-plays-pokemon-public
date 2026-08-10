import time
import bridge

print("Consolidated go_into_safari.py (Fuchsia Bush -> Safari Zone)...")

# Step 1: Dismiss CUT
print("Dismissing CUT dialogue...")
bridge.press_buttons(["B"])
time.sleep(1.5) # Wait for animation to finish completely

coords = bridge.get_coordinates()
print(f"Coords after CUT: {coords}")

# Step 2: Walk UP column 26 to Row 9
print("Walking UP Column 26 to Row 9...")
for _ in range(5):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords at Row 9: {coords}")

# Step 3: Walk LEFT along Row 9 to Column 19
print("Walking LEFT along Row 9 to Column 19...")
for _ in range(7):
    bridge.press_buttons(["Left"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords at Column 19: {coords}")

# Step 4: Walk UP Column 19 to Row 8
print("Walking UP Column 19 to Row 8...")
bridge.press_buttons(["Up"])
time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords at Row 8: {coords}")

# Step 5: Walk RIGHT along Row 8 to Column 37
print("Walking RIGHT along Row 8 to Column 37...")
for _ in range(18):
    bridge.press_buttons(["Right"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords at Column 37: {coords}")

# Step 6: Walk UP Column 37 to Row 2
print("Walking UP Column 37 to Row 2...")
for _ in range(6):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords at Row 2: {coords}")

# Step 7: Walk LEFT along Row 2 to Column 22
print("Walking LEFT along Row 2 to Column 22...")
for _ in range(15):
    bridge.press_buttons(["Left"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords at Column 22: {coords}")

# Step 8: Walk DOWN Column 22 to Row 4
print("Walking DOWN Column 22 to Row 4...")
for _ in range(2):
    bridge.press_buttons(["Down"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords at Row 4: {coords}")

# Step 9: Walk UP to enter the Gatehouse
print("Entering Gatehouse...")
bridge.press_buttons(["Up"])
time.sleep(2.0) # Wait for transition loading

coords = bridge.get_coordinates()
print(f"Coords inside Gatehouse: {coords}")

# Step 10: Walk UP to talk to the clerk and pay 500
print("Walking UP to the clerk...")
for _ in range(2):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)

print("Going through dialogue to pay 500 and buy Safari Balls...")
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

# Step 11: Walk UP to enter the Safari Zone
print("Entering the Safari Zone with a fresh 500 steps!")
bridge.press_buttons(["Up"])
time.sleep(2.0) # Wait for transition load

coords = bridge.get_coordinates()
print(f"Final coordinates inside the Safari Zone: {coords}")

