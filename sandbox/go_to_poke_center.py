import time
import bridge

print("Running go_to_poke_center_v4.py from (16, 21)...")

# Step 1: Walk Right to Column 24
print("Walking Right to Column 24...")
for _ in range(8):
    bridge.press_buttons(["Right"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords: {coords}")

# Step 2: Walk Down Column 24 to row 31
print("Walking Down Column 24 to row 31...")
for _ in range(10):
    bridge.press_buttons(["Down"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords: {coords}")

# Step 3: Walk Right to Column 25
print("Walking Right to Column 25...")
bridge.press_buttons(["Right"])
time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords: {coords}")

# Step 4: Walk Down Column 25 to row 33
print("Walking Down Column 25 to row 33...")
for _ in range(2):
    bridge.press_buttons(["Down"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords: {coords}")

# Step 5: Walk Left along row 33 to column 19
print("Walking Left along row 33 to column 19...")
for _ in range(6):
    bridge.press_buttons(["Left"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords: {coords}")

# Step 6: Walk Up Column 19 to row 27
print("Walking Up Column 19 to row 27...")
for _ in range(6):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords in front of PC (19, 27): {coords}")

# Step 7: Enter Pokémon Center
print("Entering Pokémon Center...")
bridge.press_buttons(["Up"])
time.sleep(2.0)
coords = bridge.get_coordinates()
print(f"Coords inside Pokémon Center: {coords}")

