import mgba
import time

def get_secret_key():
    print("Executing master route to retrieve Secret Key...")
    
    # Current position is (10, 5)
    # 1. Walk Down to (10, 11)
    for _ in range(6):
        mgba.press_buttons(["Down"])
        time.sleep(0.05)
    print(f"Reached coordinates after Down: {mgba.get_coordinates()}")
    
    # 2. Walk Left to (3, 11)
    for _ in range(7):
        mgba.press_buttons(["Left"])
        time.sleep(0.05)
    print(f"Reached coordinates after Left: {mgba.get_coordinates()}")
    
    # 3. Toggle Switch to State B
    print("Toggling switch...")
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    print("Switch toggled!")
    
    # 4. Try Column 6 first
    print("Attempting Column 6 path...")
    # Walk Right to (6, 11)
    for _ in range(3):
        mgba.press_buttons(["Right"])
        time.sleep(0.05)
    print(f"Standing at: {mgba.get_coordinates()}")
    
    # Walk Up Column 6 to row 4
    for _ in range(7):
        mgba.press_buttons(["Up"])
        time.sleep(0.05)
    pos = mgba.get_coordinates()
    print(f"Coordinates after Column 6 Up: {pos}")
    
    if pos['y'] <= 5:
        print("Column 6 path is OPEN!")
    else:
        print("Column 6 path was blocked, trying Column 4...")
        # Walk back down to row 11 if needed, then to Column 4
        # Since we got blocked, let's just go Down to row 11
        while mgba.get_coordinates()['y'] < 11:
            mgba.press_buttons(["Down"])
            time.sleep(0.05)
        # Walk to Column 4
        curr_x = mgba.get_coordinates()['x']
        steps = curr_x - 4
        if steps > 0:
            for _ in range(steps):
                mgba.press_buttons(["Left"])
                time.sleep(0.05)
        elif steps < 0:
            for _ in range(-steps):
                mgba.press_buttons(["Right"])
                time.sleep(0.05)
        print(f"Standing at: {mgba.get_coordinates()}")
        
        # Walk Up Column 4 to row 4
        for _ in range(7):
            mgba.press_buttons(["Up"])
            time.sleep(0.05)
        pos = mgba.get_coordinates()
        print(f"Coordinates after Column 4 Up: {pos}")
        
    # We should now be in the north area on row 4 or 5
    # Walk to (1, 4)
    # Walk Left to Column 1
    curr_x = mgba.get_coordinates()['x']
    steps = curr_x - 1
    for _ in range(steps):
        mgba.press_buttons(["Left"])
        time.sleep(0.05)
    # Walk to row 4
    curr_y = mgba.get_coordinates()['y']
    steps_y = curr_y - 4
    if steps_y > 0:
        for _ in range(steps_y):
            mgba.press_buttons(["Up"])
            time.sleep(0.05)
    elif steps_y < 0:
        for _ in range(-steps_y):
            mgba.press_buttons(["Down"])
            time.sleep(0.05)
            
    print(f"Arrived at Target coordinates: {mgba.get_coordinates()}")
    
    # Press A to pick up the Secret Key
    print("Attempting to retrieve Secret Key...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    # Press B to clear any text box that appeared
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    print(f"Final coordinates: {mgba.get_coordinates()}")
    scr = mgba.take_screenshot()
    print(f"Screenshot taken: {scr}")

get_secret_key()
