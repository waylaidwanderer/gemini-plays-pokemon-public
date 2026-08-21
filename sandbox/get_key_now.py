import mgba
import time

def clear_and_get_key():
    print("Clearing battle text and trying to walk up Column 1 to the Secret Key...")
    
    # 1. Clear battle text
    mgba.press_buttons(["B"])
    time.sleep(1.0)
    
    pos = mgba.get_coordinates()
    print(f"Position in overworld: {pos}")
    
    # We should be at (4, 13)
    # 2. Walk Left to Column 1
    for step in range(1, 5):
        mgba.press_buttons(["Left"])
        time.sleep(0.5)
        new_pos = mgba.get_coordinates()
        print(f"Step {step} Left: {new_pos}")
        if new_pos == pos:
            print(f"Blocked at {pos} on step {step} Left!")
            break
        pos = new_pos
        
    # We should be at (1, 13)
    # 3. Walk Up Column 1 as far as possible
    print("Walking Up Column 1...")
    for step in range(1, 11):
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        new_pos = mgba.get_coordinates()
        print(f"Step {step} UP: {new_pos}")
        if new_pos == pos:
            print(f"Blocked at {pos} on step {step} UP!")
            break
        pos = new_pos
        
    # Check if we are at (1, 4) or (1, 5)
    current_pos = mgba.get_coordinates()
    print(f"Current position: {current_pos}")
    
    if current_pos == {'x': 1, 'y': 4}:
        print("At (1, 4)! Pressing A to get the Secret Key...")
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        # Clear dialogue
        mgba.press_buttons(["B"])
        time.sleep(0.5)
        mgba.press_buttons(["B"])
        time.sleep(0.5)
        print("Done!")
    elif current_pos == {'x': 1, 'y': 5}:
        print("At (1, 5)! Facing UP and pressing A to get the Secret Key...")
        mgba.press_buttons(["Up", "A"])
        time.sleep(1.0)
        # Clear dialogue
        mgba.press_buttons(["B"])
        time.sleep(0.5)
        mgba.press_buttons(["B"])
        time.sleep(0.5)
        print("Done!")
    else:
        print("Could not reach Secret Key position directly via Column 1.")
        
    scr = mgba.take_screenshot()
    print(f"Screenshot at end: {scr}")

clear_and_get_key()
