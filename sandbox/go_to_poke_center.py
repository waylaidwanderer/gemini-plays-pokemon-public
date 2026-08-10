import time
import bridge

print("Running go_to_poke_center.py (dismissing CUT, walking to Center, entering, and opening PC)...")

# Step 1: Dismiss CUT
print("Dismissing CUT text box...")
bridge.press_buttons(["B"])
time.sleep(2.0) # Wait for animation and text box to clear completely
print(f"Coords after CUT: {bridge.get_coordinates()}")

# Step 2: Walk Down column 26 to row 14
print("Walking Down column 26 to row 14...")
for _ in range(2):
    bridge.press_buttons(["Down"])
    time.sleep(0.6)
print(f"Coords at (26, 14): {bridge.get_coordinates()}")

# Step 3: Walk Left along row 14 to column 22
print("Walking Left along row 14 to column 22...")
for _ in range(4):
    bridge.press_buttons(["Left"])
    time.sleep(0.6)
print(f"Coords at (22, 14): {bridge.get_coordinates()}")

# Step 4: Walk Down column 22 to row 21
print("Walking Down column 22 to row 21...")
for _ in range(7):
    bridge.press_buttons(["Down"])
    time.sleep(0.6)
print(f"Coords at (22, 21): {bridge.get_coordinates()}")

# Step 5: Walk Right along row 21 to column 24
print("Walking Right along row 21 to column 24...")
for _ in range(2):
    bridge.press_buttons(["Right"])
    time.sleep(0.6)
print(f"Coords at (24, 21): {bridge.get_coordinates()}")

# Step 6: Walk Down column 24 to row 27
print("Walking Down column 24 to row 27...")
for _ in range(6):
    bridge.press_buttons(["Down"])
    time.sleep(0.6)
print(f"Coords at (24, 27): {bridge.get_coordinates()}")

# Step 7: Walk Left along row 27 to column 19
print("Walking Left along row 27 to column 19...")
for _ in range(5):
    bridge.press_buttons(["Left"])
    time.sleep(0.6)
print(f"Coords in front of PC (19, 27): {bridge.get_coordinates()}")

# Step 8: Enter Pokémon Center
print("Entering Pokémon Center...")
bridge.press_buttons(["Up"])
time.sleep(2.0) # Wait for transition loading
print(f"Coords inside Pokémon Center: {bridge.get_coordinates()}")

# Step 9: Walk to the PC at (13, 4)
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

# Step 10: Access PC and open ITEM PC STORAGE
print("Accessing PC...")
bridge.press_buttons(["A"]) # Turn on PC
time.sleep(1.0)
bridge.press_buttons(["A"]) # Select "ACE's PC"
time.sleep(1.0)
bridge.press_buttons(["Down", "sleep 300", "A"]) # Select "ITEM STORAGE"
time.sleep(1.0)
bridge.press_buttons(["A"]) # Select "WITHDRAW ITEM"
time.sleep(2.0) # Wait for item list to display

print("PC storage menu opened successfully. Check the screen next turn!")
