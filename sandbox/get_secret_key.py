import mgba
import time

def master_retrieve_key():
    print("Clearing battle text and starting master search for Secret Key...")
    
    # 1. Clear "Got away safely!" by pressing A
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    pos = mgba.get_coordinates()
    print(f"Overworld coordinate: {pos}")
    
    # Align to x=10, y=6 (bypass column entry)
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
                
    curr_y = mgba.get_coordinates()['y']
    steps_y = 6 - curr_y
    if steps_y > 0:
        for _ in range(steps_y):
            mgba.press_buttons(["Down"])
            time.sleep(0.05)
    elif steps_y < 0:
        for _ in range(-steps_y):
            mgba.press_buttons(["Up"])
            time.sleep(0.05)
            
    print(f"Aligned at bypass column entry (10, 6): {mgba.get_coordinates()}")
    
    # Let's test Row 6 first
    print("Testing Row 6...")
    mgba.press_buttons(["Left"]) # Turn left
    time.sleep(0.1)
    mgba.press_buttons(["Left"]) # Step left
    time.sleep(0.1)
    
    pos = mgba.get_coordinates()
    if pos['x'] == 9:
        print("Row 6 is OPEN! (State B). Moving to retrieve Secret Key...")
        # Walk Left to (1, 6)
        for _ in range(8):
            mgba.press_buttons(["Left"])
            time.sleep(0.05)
        # Walk Up to (1, 4)
        for _ in range(2):
            mgba.press_buttons(["Up"])
            time.sleep(0.05)
        retrieve_key_at_1_4()
        return
        
    print("Row 6 is CLOSED. Testing Row 4...")
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
        print("Row 4 is OPEN! (State A). Moving to retrieve Secret Key...")
        # Walk Left to (1, 4)
        for _ in range(8):
            mgba.press_buttons(["Left"])
            time.sleep(0.05)
        retrieve_key_at_1_4()
        return
        
    print("Both gates CLOSED! We must walk to B1F Mewtwo statue and toggle.")
    # Walk Down to (10, 12) via Row 12 (bypassing statue)
    # Currently at (10, 4) or similar. Walk to (10, 11)
    curr_y = mgba.get_coordinates()['y']
    for _ in range(11 - curr_y):
        mgba.press_buttons(["Down"])
        time.sleep(0.05)
    # Down to row 12
    mgba.press_buttons(["Down"])
    time.sleep(0.05)
    print(f"At (10, 12) for bypass: {mgba.get_coordinates()}")
    
    # Walk Left along Row 12 to (2, 12)
    for _ in range(8):
        mgba.press_buttons(["Left"])
        time.sleep(0.05)
    print(f"At (2, 12) below switch: {mgba.get_coordinates()}")
    
    # Face UP to interact with switch
    mgba.press_buttons(["Up"])
    time.sleep(0.1)
    
    # Toggle switch with robust delays
    print("Interacting with switch...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["B"])
    time.sleep(1.0)
    print("Switch toggled!")
    
    # Walk back to Column 10 along Row 12
    for _ in range(8):
        mgba.press_buttons(["Right"])
        time.sleep(0.05)
    print(f"Returned to (10, 12): {mgba.get_coordinates()}")
    
    # Walk Up to Row 11
    mgba.press_buttons(["Up"])
    time.sleep(0.05)
    print(f"Returned to Row 11: {mgba.get_coordinates()}")
    
    # Now let's test Row 6 again since state has swapped!
    for _ in range(5):
        mgba.press_buttons(["Up"])
        time.sleep(0.05)
    print(f"At Row 6 bypass: {mgba.get_coordinates()}")
    
    mgba.press_buttons(["Left"]) # Turn left
    time.sleep(0.1)
    mgba.press_buttons(["Left"]) # Step left
    time.sleep(0.1)
    
    pos = mgba.get_coordinates()
    if pos['x'] == 9:
        print("Row 6 is OPEN after toggle! Moving to retrieve Secret Key...")
        for _ in range(8):
            mgba.press_buttons(["Left"])
            time.sleep(0.05)
        for _ in range(2):
            mgba.press_buttons(["Up"])
            time.sleep(0.05)
        retrieve_key_at_1_4()
        return
        
    # Try Row 4 after toggle
    print("Row 6 still closed after toggle, trying Row 4...")
    for _ in range(2):
        mgba.press_buttons(["Up"])
        time.sleep(0.05)
    mgba.press_buttons(["Left"])
    time.sleep(0.1)
    mgba.press_buttons(["Left"])
    time.sleep(0.1)
    
    pos = mgba.get_coordinates()
    if pos['x'] == 9:
        print("Row 4 is OPEN after toggle! Moving to retrieve Secret Key...")
        for _ in range(8):
            mgba.press_buttons(["Left"])
            time.sleep(0.05)
        retrieve_key_at_1_4()
        return
        
    print("CRITICAL ERROR: Neither gate is open even after toggle!")
    mgba.take_screenshot()

def retrieve_key_at_1_4():
    print("Picking up the Secret Key...")
    # Stand on (1, 4) and press A
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

master_retrieve_key()
