import time
import bridge

print("Running go_to_poke_center_v2.py from (25, 8)...")

# Step 1: Walk to (26, 9)
print("Walking to (26, 9)...")
bridge.press_buttons(["Down", "sleep 300", "Right"])
time.sleep(1.0)
coords = bridge.get_coordinates()
print(f"Coords at (26, 9): {coords}")

if coords != (26, 9):
    print("WARNING: Blocked on way to (26, 9). Trying to recover...")
    # Just in case, let's re-try
    bridge.press_buttons(["Down", "sleep 200", "Right"])
    time.sleep(1.0)
    coords = bridge.get_coordinates()
    print(f"Coords after recovery: {coords}")

# Step 2: Walk Down column 26 to row 14
print("Walking Down column 26 to row 14...")
for _ in range(5):
    bridge.press_buttons(["Down"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords at (26, 14): {coords}")

# Step 3: Walk Left along row 14 to column 22
print("Walking Left along row 14 to column 22...")
for _ in range(4):
    bridge.press_buttons(["Left"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords at (22, 14): {coords}")

# Step 4: Walk Down column 22 to row 21
print("Walking Down column 22 to row 21...")
for _ in range(7):
    bridge.press_buttons(["Down"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords at (22, 21): {coords}")

# Step 5: Walk Right along row 21 to column 24
print("Walking Right along row 21 to column 24...")
for _ in range(2):
    bridge.press_buttons(["Right"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords at (24, 21): {coords}")

# Step 6: Walk Down column 24 to row 27
print("Walking Down column 24 to row 27...")
for _ in range(6):
    bridge.press_buttons(["Down"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords at (24, 27): {coords}")

# Step 7: Walk Left along row 27 to column 19
print("Walking Left along row 27 to column 19...")
for _ in range(5):
    bridge.press_buttons(["Left"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords in front of PC (19, 27): {coords}")

# Step 8: Enter Pokémon Center
print("Entering Pokémon Center...")
bridge.press_buttons(["Up"])
time.sleep(2.0)
coords = bridge.get_coordinates()
print(f"Coords inside Pokémon Center: {coords}")

