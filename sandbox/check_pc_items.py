import time
import bridge

print("Starting automated check of PC items from Safari Zone...")

# Step 1: Run out of steps inside the Safari Zone
print("Mashing UP and DOWN to run out of steps...")
steps_expelled = False
for i in range(350): # We have about 275 steps remaining
    # Alternate Up and Down to pace around
    direction = "Up" if i % 2 == 0 else "Down"
    bridge.press_buttons([direction])
    time.sleep(0.05) # Press quickly since we just want to burn steps
    
    # Check if we were warped back to the Gatehouse
    # Gatehouse coordinates are typically x=4, y=3 or x=3, y=5
    coords = bridge.get_coordinates()
    if coords is not None and coords[1] < 10 and coords[0] < 10:
        print(f"Expelled from Safari Zone! Coordinates: {coords}")
        steps_expelled = True
        break

if not steps_expelled:
    print("WARNING: Did not detect expulsion. Trying a few more buttons.")
    for i in range(100):
        direction = "Up" if i % 2 == 0 else "Down"
        bridge.press_buttons([direction])
        time.sleep(0.05)

# Wait a moment for any residual dialogs or warp animations to clear
time.sleep(2.0)
coords = bridge.get_coordinates()
print(f"Current Coordinates: {coords}")

# Press B multiple times to clear any "Good haul? Come again!" text box
print("Dismissing Gatehouse dialogue...")
for _ in range(3):
    bridge.press_buttons(["B"])
    time.sleep(0.4)

# Step 2: Walk out of the Safari Gatehouse
print("Walking out of Safari Gatehouse...")
# Walk Down to exit. From (4,3) we go Down to (4,5) and Down 1 more to warp to Fuchsia City
for _ in range(4):
    bridge.press_buttons(["Down"])
    time.sleep(0.6)

time.sleep(1.0) # Wait for warp transition
coords = bridge.get_coordinates()
print(f"Fuchsia City Coordinates: {coords}")

# Step 3: Walk to the Pokémon Center in Fuchsia City
# - We start at around (18, 4) or (19, 4).
# - Walk DOWN to (18, 21) (17 steps)
# - Walk RIGHT to (24, 21) (6 steps)
# - Walk DOWN to (24, 28) (7 steps)
# - Walk LEFT to (19, 28) (5 steps)
# - Walk UP to (19, 27) (1 step) to enter Center
print("Walking to Pokémon Center...")
for _ in range(17):
    bridge.press_buttons(["Down"])
    time.sleep(0.6)
print(f"Intermediate Coords: {bridge.get_coordinates()}")

for _ in range(6):
    bridge.press_buttons(["Right"])
    time.sleep(0.6)
print(f"Intermediate Coords: {bridge.get_coordinates()}")

for _ in range(7):
    bridge.press_buttons(["Down"])
    time.sleep(0.6)
print(f"Intermediate Coords: {bridge.get_coordinates()}")

for _ in range(5):
    bridge.press_buttons(["Left"])
    time.sleep(0.6)
print(f"Intermediate Coords: {bridge.get_coordinates()}")

print("Entering Pokémon Center...")
bridge.press_buttons(["Up"])
time.sleep(1.5) # Wait for map load

coords = bridge.get_coordinates()
print(f"Inside Pokémon Center Coordinates: {coords}")

# Step 4: Walk to the PC at (13, 4)
# - From entrance mat at (3, 7):
# - Walk UP to (3, 4) (3 steps)
# - Walk RIGHT to (13, 4) (10 steps)
print("Walking to PC...")
for _ in range(3):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
for _ in range(10):
    bridge.press_buttons(["Right"])
    time.sleep(0.6)
print(f"PC facing position Coords: {bridge.get_coordinates()}")

# Step 5: Log in and check ITEM PC STORAGE
print("Accessing PC...")
bridge.press_buttons(["A"]) # Turn on PC
time.sleep(0.8)
bridge.press_buttons(["A"]) # Select "ACE's PC"
time.sleep(0.8)
bridge.press_buttons(["Down", "sleep 200", "A"]) # Select "ITEM STORAGE"
time.sleep(0.8)
bridge.press_buttons(["A"]) # Select "WITHDRAW ITEM"
time.sleep(1.5) # Wait for item list to display

print("PC storage menu opened successfully. Checking screen next turn!")
