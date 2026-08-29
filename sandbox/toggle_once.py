import mgba
import time

def handle_battle_if_present():
    print("Checking/handling battle...")
    # Stand still and press A to advance any appeared text
    for _ in range(3):
        mgba.press_buttons(["A"])
        time.sleep(0.8)
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    # Select RUN (Down, Right, A)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    # Dismiss "Got away safely!"
    mgba.press_buttons(["B"])
    time.sleep(0.5)

def move_safe(step, target_x, target_y):
    pos_before = mgba.get_coordinates()
    print(f"Moving {step} from {pos_before} towards ({target_x}, {target_y})...")
    mgba.press_buttons([step])
    time.sleep(0.5)
    pos_after = mgba.get_coordinates()
    
    attempts = 0
    while (pos_after['x'] != target_x or pos_after['y'] != target_y) and attempts < 3:
        if pos_before == pos_after:
            print("Did not move. Attempting battle escape...")
            handle_battle_if_present()
        else:
            print(f"Moved but not to target. Current: {pos_after}. Retrying...")
            handle_battle_if_present()
            
        mgba.press_buttons([step])
        time.sleep(0.5)
        pos_after = mgba.get_coordinates()
        attempts += 1
        
    print(f"Finished step. Current position: {pos_after}")
    return pos_after

def execute_toggle_and_cross():
    # We are currently at (1, 10).
    # 1. Walk to (2, 12) facing Up via (2, 13) detour
    move_safe("Down", 1, 11)
    move_safe("Down", 1, 12)
    move_safe("Down", 1, 13)
    move_safe("Right", 2, 13)
    move_safe("Up", 2, 12)
    
    # 2. Verify position
    pos = mgba.get_coordinates()
    if pos['x'] != 2 or pos['y'] != 12:
        print(f"Error: Failed to reach (2, 12) facing Up. Current pos: {pos}")
        return
        
    # 3. Toggle switch ONCE
    print("At (2, 12) facing Up. Toggling switch once...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    print("Switch toggled to State B.")
    
    # 4. Walk to Row 6 Column 1
    # Move to (1, 12)
    move_safe("Left", 1, 12)
    
    # Walk UP Column 1 to Row 6 (through open gate at (1, 9)!)
    for y in [11, 10, 9, 8, 7, 6]:
        move_safe("Up", 1, y)
        
    print("Successfully reached (1, 6) in State B!")

execute_toggle_and_cross()
