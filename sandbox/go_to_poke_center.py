import time
import bridge

print("Running go_to_poke_center_v5.py from (25, 30)...")

# Step 1: Walk to (24, 21)
print("Walking to (24, 21)...")
bridge.press_buttons(["Down", "sleep 300", "Left", "sleep 300"])
for _ in range(10):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords at (24, 21): {coords}")

# Step 2: Walk Left along row 21 to column 11
print("Walking Left along row 21 to column 11...")
for _ in range(13):
    bridge.press_buttons(["Left"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords at (11, 21): {coords}")

# Step 3: Walk Down column 11 to row 28
print("Walking Down column 11 to row 28...")
for _ in range(7):
    bridge.press_buttons(["Down"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords at (11, 28): {coords}")

# Step 4: Walk Right along row 28 to column 19
print("Walking Right along row 28 to column 19...")
for _ in range(8):
    bridge.press_buttons(["Right"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords at (19, 28): {coords}")

# Step 5: Enter Pokémon Center
print("Entering Pokémon Center...")
bridge.press_buttons(["Up"])
time.sleep(2.0)
coords = bridge.get_coordinates()
print(f"Coords inside Pokémon Center: {coords}")

