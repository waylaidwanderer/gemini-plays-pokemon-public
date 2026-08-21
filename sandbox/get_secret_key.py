import mgba
import time

def direct_retrieve_key():
    print("Clearing battle and retrieving Secret Key directly...")
    
    # 1. Clear "Got away safely!" by pressing A
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    pos = mgba.get_coordinates()
    print(f"Overworld coordinate: {pos}")
    
    # 2. Walk Right to (10, 11)
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
                
    pos = mgba.get_coordinates()
    print(f"At bypass landing (10, 11): {pos}")
    
    # 3. Walk Up to (10, 6)
    curr_y = pos['y']
    steps_y = 6 - curr_y
    if steps_y > 0:
        for _ in range(steps_y):
            mgba.press_buttons(["Down"])
            time.sleep(0.05)
    elif steps_y < 0:
        for _ in range(-steps_y):
            mgba.press_buttons(["Up"])
            time.sleep(0.05)
            
    print(f"At Row 6 bypass: {mgba.get_coordinates()}")
    
    # 4. Turn Left and try to walk Left
    mgba.press_buttons(["Left"]) # Turn left
    time.sleep(0.1)
    mgba.press_buttons(["Left"]) # Step left
    time.sleep(0.1)
    
    pos = mgba.get_coordinates()
    if pos['x'] == 9:
        print("Row 6 is OPEN! Walking Left to Column 1...")
        for _ in range(8):
            mgba.press_buttons(["Left"])
            time.sleep(0.05)
        print(f"Bypassed Column 9 via Row 6. Coordinates: {mgba.get_coordinates()}")
        
        # Walk Up to (1, 4)
        for _ in range(2):
            mgba.press_buttons(["Up"])
            time.sleep(0.05)
        retrieve_key_at_1_4()
        return
        
    print("Row 6 is CLOSED. Trying Row 4...")
    # Walk Up 2 steps to (10, 4)
    for _ in range(2):
        mgba.press_buttons(["Up"])
        time.sleep(0.05)
    print(f"At Row 4 bypass (10, 4): {mgba.get_coordinates()}")
    
    mgba.press_buttons(["Left"]) # Turn left
    time.sleep(0.1)
    mgba.press_buttons(["Left"]) # Step left
    time.sleep(0.1)
    
    pos = mgba.get_coordinates()
    if pos['x'] == 9:
        print("Row 4 is OPEN! Walking Left to Column 1...")
        for _ in range(8):
            mgba.press_buttons(["Left"])
            time.sleep(0.05)
        retrieve_key_at_1_4()
        return
        
    print("CRITICAL ERROR: Both gates CLOSED! Switch state is desynchronized.")
    mgba.take_screenshot()

def retrieve_key_at_1_4():
    # Stand on (1, 4) and press A
    print("Picking up the Secret Key at (1, 4)...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    # Clear dialogue
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    print(f"Secret Key retrieved successfully! Current coordinates: {mgba.get_coordinates()}")
    scr = mgba.take_screenshot()
    print(f"Master screenshot: {scr}")

direct_retrieve_key()
