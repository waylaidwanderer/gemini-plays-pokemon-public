import time
import bridge

print("Starting go_inside_pc.py...")

# Check current coordinates
pos = bridge.get_coordinates()
print(f"Current overworld coordinates: {pos}")
if pos != (9, 32):
    print("Not at (9, 32)! Attempting to realign or exit.")

# Step 1: Walk to Column 8
print("Walking to Column 8...")
bridge.press_buttons(["Left"])
time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos}")

# Step 2: Walk Up through the ledge gap at Column 8 to Row 28
print("Walking UP to Row 28...")
for _ in range(4):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos}")

# Step 3: Walk Right to Column 19
print("Walking RIGHT to Column 19...")
for _ in range(11):
    bridge.press_buttons(["Right"])
    time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos}")

# Step 4: Walk Up to the Poké Center door
print("Walking UP to door...")
bridge.press_buttons(["Up"])
time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos}")

# Step 5: Enter Poké Center
print("Entering Pokémon Center...")
bridge.press_buttons(["Up"])
time.sleep(2.0) # Wait for transition loading

pos = bridge.get_coordinates()
print(f"Coordinates inside Pokémon Center: {pos}")

# Ensure we are inside (standard PC entrance is around (3, 7) or (3, 8))
if pos is not None and (pos[0] == 3 or pos[1] >= 7):
    print("Successfully entered Pokémon Center!")
    
    # Step 6: Walk to the PC
    # First, move up off the mat so we don't walk out
    print("Moving up off the entrance mat...")
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
    
    pos = bridge.get_coordinates()
    print(f"Coordinates: {pos}")
    
    # Walk Right to Column 13 (we are at Column 3, so 10 steps)
    print("Walking Right to Column 13...")
    for _ in range(10):
        bridge.press_buttons(["Right"])
        time.sleep(0.6)
    pos = bridge.get_coordinates()
    print(f"Coordinates: {pos}")
    
    # Walk Up to Row 4 (we should be at Row 6 or 7, so let's walk Up until we reach Row 4)
    if pos is not None:
        target_up = pos[1] - 4
        print(f"Walking UP {target_up} steps to Row 4...")
        for _ in range(target_up):
            bridge.press_buttons(["Up"])
            time.sleep(0.6)
            
    pos = bridge.get_coordinates()
    print(f"Final coordinates in front of PC: {pos}")
    
    # Step 7: Interact with PC
    print("Interacting with PC...")
    # Face UP and boot the PC
    bridge.press_buttons(["Up", "sleep 200", "A"])
    time.sleep(1.5)
    
    # Select BILL's PC
    print("Selecting BILL's PC...")
    bridge.press_buttons(["A"])
    time.sleep(1.5)
    
    # Select CHANGE BOX (4th option: Down, Down, Down, A)
    print("Selecting CHANGE BOX...")
    bridge.press_buttons(["Down", "sleep 200", "Down", "sleep 200", "Down", "sleep 200", "A"])
    time.sleep(1.5)
    
    # Choose BOX 2 (second option: Down, A)
    print("Choosing BOX 2...")
    bridge.press_buttons(["Down", "sleep 200", "A"])
    time.sleep(1.5)
    
    # Confirm switch on YES/NO prompt (YES is first option, so just press A!)
    print("Confirming YES to switch box...")
    bridge.press_buttons(["A"])
    time.sleep(2.0) # Wait for saving/switching text
    
    # Press A/B to dismiss potential saving screen text
    print("Dismissing text...")
    bridge.press_buttons(["A", "sleep 500", "A", "sleep 500", "B", "sleep 500", "B", "sleep 500", "B"])
    time.sleep(1.0)
    
    print("PC Box Switch Attempt Completed!")
else:
    print("Failed to enter Pokémon Center or unexpected coordinates.")
