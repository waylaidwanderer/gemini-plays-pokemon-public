import mgba
import time

def toggle_and_retrieve_master():
    print("Clearing battle text and executing master B1F route...")
    
    # 1. Clear "Got away safely!" by pressing A
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    pos = mgba.get_coordinates()
    print(f"Overworld coordinate: {pos}")
    
    # We should be at (5, 11). Walk to (3, 11)
    if pos['x'] != 3:
        steps_x = 3 - pos['x']
        if steps_x > 0:
            for _ in range(steps_x):
                mgba.press_buttons(["Right"])
                time.sleep(0.05)
        elif steps_x < 0:
            for _ in range(-steps_x):
                mgba.press_buttons(["Left"])
                time.sleep(0.05)
                
    # Align to Row 11 if needed
    curr_y = mgba.get_coordinates()['y']
    if curr_y != 11:
        steps_y = 11 - curr_y
        if steps_y > 0:
            for _ in range(steps_y):
                mgba.press_buttons(["Down"])
                time.sleep(0.05)
        elif steps_y < 0:
            for _ in range(-steps_y):
                mgba.press_buttons(["Up"])
                time.sleep(0.05)
                
    print(f"At (3, 11) near switch: {mgba.get_coordinates()}")
    
    # 2. Walk Down to (3, 12)
    mgba.press_buttons(["Down"])
    time.sleep(0.05)
    
    # 3. Walk Left to (2, 12)
    mgba.press_buttons(["Left"])
    time.sleep(0.05)
    print(f"At (2, 12) directly below switch: {mgba.get_coordinates()}")
    
    # 4. Face UP (first Up press turns)
    mgba.press_buttons(["Up"])
    time.sleep(0.1)
    
    # 5. Toggle switch (A, A, B)
    print("Toggling B1F switch...")
    mgba.press_buttons(["A"])
    time.sleep(1.0) # Wait for prompt
    mgba.press_buttons(["A"])
    time.sleep(1.0) # Wait for confirmation "Who wouldn't?"
    mgba.press_buttons(["B"])
    time.sleep(1.0) # Close dialogue
    print("Switch successfully toggled!")
    
    # 6. Walk back to Column 10:
    # Walk Right to (3, 12)
    mgba.press_buttons(["Right"])
    time.sleep(0.05)
    # Walk Up to (3, 11)
    mgba.press_buttons(["Up"])
    time.sleep(0.05)
    # Walk Right to (10, 11)
    for _ in range(7):
        mgba.press_buttons(["Right"])
        time.sleep(0.05)
    print(f"Returned to bypass column (10, 11): {mgba.get_coordinates()}")
    
    # 7. Walk Up Column 10 to Row 6 (10, 6)
    # y = 11 to y = 6 is 5 steps Up.
    for _ in range(5):
        mgba.press_buttons(["Up"])
        time.sleep(0.05)
    print(f"At Row 6 bypass: {mgba.get_coordinates()}")
    
    # 8. Walk Left to (1, 6) through the OPEN Row 6 Column 9 gate!
    # Turn Left
    mgba.press_buttons(["Left"])
    time.sleep(0.1)
    # Step Left 9 times (to Column 1)
    for _ in range(9):
        mgba.press_buttons(["Left"])
        time.sleep(0.05)
    print(f"Bypassed Column 9 to West side: {mgba.get_coordinates()}")
    
    # 9. Walk Up to (1, 4)
    # y = 6 to y = 4 is 2 steps Up.
    for _ in range(2):
        mgba.press_buttons(["Up"])
        time.sleep(0.05)
    print(f"Arrived at Secret Key tile: {mgba.get_coordinates()}")
    
    # 10. Press A to pick up the Secret Key
    print("Retrieving Secret Key...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    # Confirm final state
    final_pos = mgba.get_coordinates()
    print(f"Final coordinates: {final_pos}")
    scr = mgba.take_screenshot()
    print(f"Master screenshot: {scr}")

toggle_and_retrieve_master()
