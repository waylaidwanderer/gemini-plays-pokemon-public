import mgba
import time

def clear_battle_and_get_key_master():
    print("Clearing battle and starting master Secret Key retrieval...")
    
    # 1. Clear battle text "Got away safely!" by pressing A
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # Get current overworld coordinate (should be near (7, 11))
    pos = mgba.get_coordinates()
    print(f"Overworld coordinate: {pos}")
    
    # 2. Walk to the bypass column at x=10, row 11: (10, 11)
    if pos['x'] != 10:
        steps = 10 - pos['x']
        if steps > 0:
            for _ in range(steps):
                mgba.press_buttons(["Right"])
                time.sleep(0.05)
        elif steps < 0:
            for _ in range(-steps):
                mgba.press_buttons(["Left"])
                time.sleep(0.05)
                
    # Align to y=11
    curr_y = mgba.get_coordinates()['y']
    steps_y = 11 - curr_y
    if steps_y > 0:
        for _ in range(steps_y):
            mgba.press_buttons(["Down"])
            time.sleep(0.05)
    elif steps_y < 0:
        for _ in range(-steps_y):
            mgba.press_buttons(["Up"])
            time.sleep(0.05)
            
    print(f"Arrived at bypass landing: {mgba.get_coordinates()}")
    
    # Let's check which state we are in by testing Row 4 and Row 6 on Column 9.
    # We will test Row 6 first, then Row 4.
    
    # Test Row 6:
    # Walk Up to (10, 6)
    for _ in range(5):
        mgba.press_buttons(["Up"])
        time.sleep(0.05)
    print(f"At Row 6 bypass: {mgba.get_coordinates()}")
    
    # Turn Left (first Left press turns in place)
    mgba.press_buttons(["Left"])
    time.sleep(0.1)
    # Try to step Left
    mgba.press_buttons(["Left"])
    time.sleep(0.1)
    
    pos = mgba.get_coordinates()
    if pos['x'] == 9:
        print("Row 6 gate is OPEN! We are in the correct state (State B or similar).")
        # Walk Left to (1, 6)
        for _ in range(8): # We are at x=9, need to walk to x=1
            mgba.press_buttons(["Left"])
            time.sleep(0.05)
        print(f"Bypassed Column 9 via Row 6. Coordinates: {mgba.get_coordinates()}")
        
        # Walk Up to (1, 4)
        for _ in range(2):
            mgba.press_buttons(["Up"])
            time.sleep(0.05)
        print(f"Arrived at Secret Key: {mgba.get_coordinates()}")
        retrieve_key_and_exit()
        return

    print("Row 6 gate is CLOSED. Testing Row 4...")
    # Since we got blocked at (10, 6), let's walk Up to (10, 4)
    # (10, 6) to (10, 4) is 2 steps Up.
    for _ in range(2):
        mgba.press_buttons(["Up"])
        time.sleep(0.05)
    print(f"At Row 4 bypass: {mgba.get_coordinates()}")
    
    # Turn Left (first Left press turns in place)
    mgba.press_buttons(["Left"])
    time.sleep(0.1)
    # Try to step Left
    mgba.press_buttons(["Left"])
    time.sleep(0.1)
    
    pos = mgba.get_coordinates()
    if pos['x'] == 9:
        print("Row 4 gate is OPEN! We are in the correct state (State A or similar).")
        # Walk Left to (1, 4)
        for _ in range(8): # We are at x=9, need to walk to x=1
            mgba.press_buttons(["Left"])
            time.sleep(0.05)
        print(f"Arrived at Secret Key via Row 4. Coordinates: {mgba.get_coordinates()}")
        retrieve_key_and_exit()
        return

    print("Both gates are CLOSED! We must toggle the switch at (2, 11) to open them.")
    # Walk back to (10, 11) from (10, 4)
    for _ in range(7):
        mgba.press_buttons(["Down"])
        time.sleep(0.05)
    print(f"Returned to Row 11: {mgba.get_coordinates()}")
    
    # Walk Left to (3, 11)
    for _ in range(7):
        mgba.press_buttons(["Left"])
        time.sleep(0.05)
    print(f"At switch: {mgba.get_coordinates()}")
    
    # Toggle switch with highly robust sleeps
    print("Toggling switch...")
    mgba.press_buttons(["A"])
    time.sleep(1.0) # Wait for text box to fully render
    mgba.press_buttons(["A"])
    time.sleep(1.0) # Wait for confirmation text "Who wouldn't?"
    mgba.press_buttons(["B"])
    time.sleep(1.0) # Close dialogue
    print("Switch toggled!")
    
    # Walk Right to (10, 11)
    for _ in range(7):
        mgba.press_buttons(["Right"])
        time.sleep(0.05)
    print(f"Returned to bypass Column 10: {mgba.get_coordinates()}")
    
    # Since we toggled, the open gate has swapped! Let's test Row 6 first now.
    # Walk Up to (10, 6)
    for _ in range(5):
        mgba.press_buttons(["Up"])
        time.sleep(0.05)
    print(f"At Row 6 bypass: {mgba.get_coordinates()}")
    
    # Turn Left
    mgba.press_buttons(["Left"])
    time.sleep(0.1)
    # Step Left
    mgba.press_buttons(["Left"])
    time.sleep(0.1)
    
    pos = mgba.get_coordinates()
    if pos['x'] == 9:
        print("Row 6 gate is now OPEN after toggle!")
        # Walk Left to (1, 6)
        for _ in range(8):
            mgba.press_buttons(["Left"])
            time.sleep(0.05)
        # Walk Up to (1, 4)
        for _ in range(2):
            mgba.press_buttons(["Up"])
            time.sleep(0.05)
        print(f"Arrived at Secret Key: {mgba.get_coordinates()}")
        retrieve_key_and_exit()
        return
        
    # If Row 6 is still closed, try Row 4
    print("Row 6 gate is still closed, trying Row 4 after toggle...")
    for _ in range(2):
        mgba.press_buttons(["Up"])
        time.sleep(0.05)
    # Turn Left
    mgba.press_buttons(["Left"])
    time.sleep(0.1)
    # Step Left
    mgba.press_buttons(["Left"])
    time.sleep(0.1)
    
    pos = mgba.get_coordinates()
    if pos['x'] == 9:
        print("Row 4 gate is now OPEN after toggle!")
        # Walk Left to (1, 4)
        for _ in range(8):
            mgba.press_buttons(["Left"])
            time.sleep(0.05)
        print(f"Arrived at Secret Key: {mgba.get_coordinates()}")
        retrieve_key_and_exit()
        return
        
    print("CRITICAL: Both gates remain CLOSED even after toggle. Something is wrong.")
    mgba.take_screenshot()

def retrieve_key_and_exit():
    # Stand at (1, 4) and pick up Secret Key
    print("Attempting to retrieve Secret Key at (1, 4)...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    # Dismiss any text box
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    print(f"Key retrieved! Current position: {mgba.get_coordinates()}")
    scr = mgba.take_screenshot()
    print(f"Final master screenshot: {scr}")

clear_battle_and_get_key_master()
