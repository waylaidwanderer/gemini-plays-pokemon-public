import time
import bridge

print("Running go_to_poke_center_v6.py from (9, 32)...")

# Step 1: Walk UP 2 steps to row 30
print("Walking UP 2 steps to row 30...")
for _ in range(2):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords at row 30: {coords}")

# Step 2: Walk RIGHT 10 steps to column 19
print("Walking RIGHT 10 steps to column 19...")
for _ in range(10):
    bridge.press_buttons(["Right"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords at (19, 30): {coords}")

# Step 3: Enter Pokémon Center (UP 3 steps to 19, 27)
print("Entering Pokémon Center...")
for _ in range(3):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
time.sleep(2.0) # Wait for transition loading
coords = bridge.get_coordinates()
print(f"Coords inside Pokémon Center: {coords}")

# Step 4: Walk to the PC at (13, 4)
# From entrance mat at (3, 7):
# Walk UP to (3, 4) (3 steps)
# Walk RIGHT to (13, 4) (10 steps)
print("Walking to the PC...")
for _ in range(3):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
for _ in range(10):
    bridge.press_buttons(["Right"])
    time.sleep(0.6)
print(f"PC facing position Coords: {bridge.get_coordinates()}")

# Step 5: Access PC and open ITEM PC STORAGE
print("Accessing PC...")
bridge.press_buttons(["A"]) # Turn on PC
time.sleep(1.0)
bridge.press_buttons(["A"]) # Select "ACE's PC"
time.sleep(1.0)
bridge.press_buttons(["Down", "sleep 300", "A"]) # Select "ITEM STORAGE"
time.sleep(1.0)
bridge.press_buttons(["A"]) # Select "WITHDRAW ITEM"
time.sleep(2.0) # Wait for item list to display

print("PC storage menu opened successfully. Checking screen next turn!")
