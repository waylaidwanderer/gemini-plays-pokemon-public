import mgba
import time

def test_left_across_col9():
    print("Testing leftward passage across Column 9 for rows 4, 5, 6...")
    
    # We are currently at (10, 5) facing DOWN.
    
    # Test Row 5:
    mgba.press_buttons(["Left"]) # Turn Left
    time.sleep(0.1)
    mgba.press_buttons(["Left"]) # Step Left
    time.sleep(0.1)
    pos = mgba.get_coordinates()
    print(f"Position after trying Left on Row 5: {pos}")
    if pos['x'] == 9:
        print("Row 5 is OPEN!")
        mgba.press_buttons(["Right"]) # Step back
        time.sleep(0.1)
        
    # Walk Down to (10, 6)
    mgba.press_buttons(["Down"])
    time.sleep(0.1)
    print(f"Standing at: {mgba.get_coordinates()}")
    
    # Test Row 6:
    mgba.press_buttons(["Left"]) # Turn Left
    time.sleep(0.1)
    mgba.press_buttons(["Left"]) # Step Left
    time.sleep(0.1)
    pos = mgba.get_coordinates()
    print(f"Position after trying Left on Row 6: {pos}")
    if pos['x'] == 9:
        print("Row 6 is OPEN!")
        mgba.press_buttons(["Right"]) # Step back
        time.sleep(0.1)
        
    # Walk Up to (10, 4)
    mgba.press_buttons(["Up"])
    time.sleep(0.1)
    mgba.press_buttons(["Up"])
    time.sleep(0.1)
    print(f"Standing at: {mgba.get_coordinates()}")
    
    # Test Row 4:
    mgba.press_buttons(["Left"]) # Turn Left
    time.sleep(0.1)
    mgba.press_buttons(["Left"]) # Step Left
    time.sleep(0.1)
    pos = mgba.get_coordinates()
    print(f"Position after trying Left on Row 4: {pos}")
    if pos['x'] == 9:
        print("Row 4 is OPEN!")
        mgba.press_buttons(["Right"]) # Step back
        time.sleep(0.1)

test_left_across_col9()
