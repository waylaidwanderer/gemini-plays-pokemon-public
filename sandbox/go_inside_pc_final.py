import time
import bridge

print("Starting go_inside_pc_final.py...")

# Check current coordinates (should be (8, 4))
pos = bridge.get_coordinates()
print(f"Current coordinates inside Pokémon Center: {pos}")
if pos != (8, 4):
    print("Not at (8, 4)! Realigning...")
    # But we should be at (8, 4) according to the GameState.

# Step 1: Walk Right to Column 13 along Row 4
print("Walking RIGHT to Column 13...")
for _ in range(5):
    bridge.press_buttons(["Right"])
    time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates: {pos}")

# Step 2: Interact with PC
if pos == (13, 4):
    print("Successfully reached the PC!")
    
    # Face UP and boot the PC
    print("Facing UP and booting PC...")
    bridge.press_buttons(["Up", "sleep 300", "A"])
    time.sleep(1.5)
    
    # Select BILL's PC
    print("Selecting BILL's PC...")
    bridge.press_buttons(["A"])
    time.sleep(1.5)
    
    # Select CHANGE BOX (4th option: Down, Down, Down, A)
    print("Selecting CHANGE BOX...")
    bridge.press_buttons(["Down", "sleep 300", "Down", "sleep 300", "Down", "sleep 300", "A"])
    time.sleep(1.5)
    
    # Choose BOX 2 (2nd option: Down, A)
    print("Choosing BOX 2...")
    bridge.press_buttons(["Down", "sleep 300", "A"])
    time.sleep(1.5)
    
    # Confirm switch on YES/NO prompt (YES is first option, so just press A!)
    # CRITICAL: DO NOT press Down! Press A to select YES.
    print("Confirming YES to switch box...")
    bridge.press_buttons(["A"])
    time.sleep(2.0) # Wait for saving/switching text
    
    # Dismiss saving text and close PC
    print("Dismissing text and closing PC...")
    bridge.press_buttons(["A", "sleep 500", "A", "sleep 500", "B", "sleep 500", "B", "sleep 500", "B"])
    time.sleep(1.0)
    
    pos = bridge.get_coordinates()
    print(f"Final coordinates after PC interaction: {pos}")
    print("PC Box Switch Completed Successfully!")
else:
    print("Failed to reach (13, 4) in front of PC.")
