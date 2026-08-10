import time
import bridge

print("Running verify_pc_and_pack.py from Gatehouse (4, 3)...")

# Step 1: Walk out of Safari Gatehouse
print("Walking out of Safari Gatehouse...")
for _ in range(4):
    bridge.press_buttons(["Down"])
    time.sleep(0.6)

time.sleep(1.0) # Wait for warp transition
coords = bridge.get_coordinates()
print(f"Fuchsia City Coordinates: {coords}")

# Step 2: Walk to the Pokémon Center in Fuchsia City
# We start at (18, 4) or similar.
print("Walking DOWN to row 21...")
for _ in range(17):
    bridge.press_buttons(["Down"])
    time.sleep(0.6)
print(f"Intermediate Coords (row 21): {bridge.get_coordinates()}")

print("Walking RIGHT to column 24...")
for _ in range(6):
    bridge.press_buttons(["Right"])
    time.sleep(0.6)
print(f"Intermediate Coords (col 24): {bridge.get_coordinates()}")

print("Walking DOWN to row 28...")
for _ in range(7):
    bridge.press_buttons(["Down"])
    time.sleep(0.6)
print(f"Intermediate Coords (row 28): {bridge.get_coordinates()}")

print("Walking LEFT to column 19...")
for _ in range(5):
    bridge.press_buttons(["Left"])
    time.sleep(0.6)
print(f"Intermediate Coords (col 19): {bridge.get_coordinates()}")

print("Entering Pokémon Center...")
bridge.press_buttons(["Up"])
time.sleep(1.5) # Wait for map load

coords = bridge.get_coordinates()
print(f"Inside Pokémon Center Coordinates: {coords}")

# Step 3: Walk to the PC at (13, 4)
# From entrance mat at (3, 7):
# Walk UP to (3, 4) (3 steps)
# Walk RIGHT to (13, 4) (10 steps)
print("Walking to PC...")
for _ in range(3):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
for _ in range(10):
    bridge.press_buttons(["Right"])
    time.sleep(0.6)
print(f"PC facing position Coords: {bridge.get_coordinates()}")

# Step 4: Log in and check ITEM PC STORAGE
print("Accessing PC...")
bridge.press_buttons(["A"]) # Turn on PC
time.sleep(1.0)
bridge.press_buttons(["A"]) # Select "ACE's PC"
time.sleep(1.0)
bridge.press_buttons(["Down", "sleep 300", "A"]) # Select "ITEM STORAGE"
time.sleep(1.0)
bridge.press_buttons(["A"]) # Select "WITHDRAW ITEM"
time.sleep(1.5) # Wait for item list to display

print("PC storage menu opened successfully. Checking screen next turn!")
