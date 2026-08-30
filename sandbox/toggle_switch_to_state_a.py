import mgba
import time

def toggle_switch_from_front():
    print("Walking to (2, 6)...")
    # Move Down to (3, 6)
    mgba.press_buttons(["Down"])
    time.sleep(0.6)
    
    # Move Left to (2, 6)
    mgba.press_buttons(["Left"])
    time.sleep(0.6)
    
    # Verify we are at (2, 6)
    pos = mgba.get_coordinates()
    print(f"Current position: {pos}")
    if pos['x'] != 2 or pos['y'] != 6:
        print("Failed to reach (2, 6)!")
        mgba.take_screenshot()
        return False
    
    # Face UP
    print("Facing UP...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    # Interact and toggle
    print("Toggling switch...")
    # A-Press 1: Interacts
    mgba.press_buttons(["A"])
    time.sleep(2.0)
    
    # A-Press 2: YES/NO
    mgba.press_buttons(["A"])
    time.sleep(2.0)
    
    # A-Press 3: Select YES
    mgba.press_buttons(["A"])
    time.sleep(2.0)
    
    # A-Press 4: Close dialogue
    mgba.press_buttons(["A"])
    time.sleep(2.0)
    
    # Take screenshot
    mgba.take_screenshot()
    print("Toggle sequence completed.")
    return True

toggle_switch_from_front()
