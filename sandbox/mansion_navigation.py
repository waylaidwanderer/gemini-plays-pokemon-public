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
            # We didn't move! Likely in a battle.
            print("Did not move. Attempting battle escape...")
            handle_battle_if_present()
        else:
            # We moved to some other position (maybe we got pushed back or got into a battle on that step)
            print(f"Moved but not to target. Current: {pos_after}. Retrying...")
            handle_battle_if_present()
            
        # Retry the step
        mgba.press_buttons([step])
        time.sleep(0.5)
        pos_after = mgba.get_coordinates()
        attempts += 1
        
    print(f"Finished step. Current position: {pos_after}")
    return pos_after

def navigate_and_drop():
    # 1. Dismiss "Got away safely!" text first
    print("Dismissing escape screen...")
    mgba.press_buttons(["B"])
    time.sleep(1.0)
    print(f"Current pos: {mgba.get_coordinates()}")
    
    # 2. From (2, 11) facing Down (or wherever, we walk Down to (2, 13)):
    # Step Down to (2, 12)
    move_safe("Down", 2, 12)
    # Step Down to (2, 13)
    move_safe("Down", 2, 13)
    
    # Step Up to (2, 12) (this turns us Up first, then steps Up)
    move_safe("Up", 2, 12)
    
    # Now we are at (2, 12) facing Up! Toggle the switch.
    print("At (2, 12) facing Up. Toggling switch...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    print("Switch toggled.")
    
    # 3. Walk straight UP Column 2 from (2, 12) to (2, 6)
    for y in [11, 10, 9, 8, 7, 6]:
        move_safe("Up", 2, y)
        
    # 4. Walk RIGHT on Row 6 to Column 21
    # From (2, 6) to (21, 6)
    for x in range(3, 22):
        move_safe("Right", x, 6)
        
    # 5. Walk LEFT 2 steps to (19, 6)
    move_safe("Left", 20, 6)
    move_safe("Left", 19, 6)
    
    # 6. Walk UP to Row 3 (19, 3)
    for y in [5, 4, 3]:
        move_safe("Up", 19, y)
        
    # 7. Walk RIGHT to Column 26 (26, 3)
    for x in range(20, 27):
        move_safe("Right", x, 3)
        
    # 8. Step Right or Down to fall through pitfall!
    print("Dropping through pitfall...")
    mgba.press_buttons(["Right"])
    time.sleep(1.0)
    mgba.press_buttons(["Down"])
    time.sleep(1.0)
    print(f"Final pos: {mgba.get_coordinates()}")

navigate_and_drop()
