import time
import bridge

print("Running shortcut_to_area3.py (directly transitioning to Area 3 West)...")

# Current position: (13, 18) facing DOWN
# Step 1: Walk RIGHT to Column 14
print("Walking RIGHT to Column 14...")
bridge.press_buttons(["Right"])
time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords: {coords}")

# Step 2: Walk UP to Row 14
print("Walking UP to Row 14...")
for _ in range(4):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords: {coords}")

# Step 3: Walk LEFT to Column 0
print("Walking LEFT to Column 0...")
for _ in range(14):
    bridge.press_buttons(["Left"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords: {coords}")

# Step 4: Walk UP to Row 11
print("Walking UP to Row 11...")
for _ in range(3):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords in front of Area 3 West transition: {coords}")

# Step 5: Walk LEFT to transition to Area 3 West
print("Transitioning to Area 3 West...")
bridge.press_buttons(["Left"])
time.sleep(2.0) # Wait for map transition loading

coords = bridge.get_coordinates()
print(f"Coords inside Area 3 West: {coords}")

