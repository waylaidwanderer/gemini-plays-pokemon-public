import time
import bridge

print("Starting go_to_pc_inside.py...")

# Check current coordinates
pos = bridge.get_coordinates()
print(f"Current coordinates inside Pokémon Center: {pos}")
if pos != (5, 7):
    print("Not at (5, 7)! Realigning to (5, 7)...")
    # If we are somewhere else, let's find out where we are
    # But we should be at (5, 7) based on Game State.

# Step 1: Walk Up to Row 5 (beige floor tiles)
print("Walking UP to Row 5...")
bridge.press_buttons(["Up"])
time.sleep(0.6)
bridge.press_buttons(["Up"])
time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates after walking UP: {pos}")

# Step 2: Walk Right to Column 13
if pos is not None:
    steps_right = 13 - pos[0]
    print(f"Walking RIGHT {steps_right} steps to Column 13...")
    for _ in range(steps_right):
        bridge.press_buttons(["Right"])
        time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates after walking RIGHT: {pos}")

# Step 3: Walk Up to Row 4 (in front of PC)
if pos is not None:
    steps_up = pos[1] - 4
    print(f"Walking UP {steps_up} steps to Row 4...")
    for _ in range(steps_up):
        bridge.press_buttons(["Up"])
        time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates in front of PC: {pos}")

# Step 4: Interact with PC and change box to BOX 2
if pos == (13, 4):
    print("In front of PC! Starting interaction...")
    # Turn UP to face PC (pressing Up once) and press A to boot PC
    bridge.press_buttons(["Up", "sleep 300", "A"])
    time.sleep(1.5)
    
    # Choose BILL's PC (1st option)
    print("Selecting BILL's PC...")
    bridge.press_buttons(["A"])
    time.sleep(1.5)
    
    # Choose CHANGE BOX (4th option: Down, Down, Down, A)
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
    
    # Let's verify we are still at (13, 4)
    pos = bridge.get_coordinates()
    print(f"Final coordinates after PC interaction: {pos}")
else:
    print("Failed to reach (13, 4) in front of PC.")
