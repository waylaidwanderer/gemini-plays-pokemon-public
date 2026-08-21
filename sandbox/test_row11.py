import mgba
import time

def test_routes():
    print("Testing B1F Column 9 gates on rows 4 and 6...")
    
    # We are currently at (3, 10). Let's go to (10, 11) first.
    # 1. Walk Down to (3, 11)
    mgba.press_buttons(["Down"])
    time.sleep(0.05)
    # 2. Walk Right to (10, 11)
    for _ in range(7):
        mgba.press_buttons(["Right"])
        time.sleep(0.05)
    print(f"Reached coordinates: {mgba.get_coordinates()}")
    
    # Test Row 6 first:
    # Walk Up to (10, 6)
    for _ in range(5):
        mgba.press_buttons(["Up"])
        time.sleep(0.05)
    print(f"At Row 6: {mgba.get_coordinates()}")
    
    # Try to go Left
    mgba.press_buttons(["Left"])
    time.sleep(0.05)
    pos_row6 = mgba.get_coordinates()
    print(f"Coordinates after trying Left on Row 6: {pos_row6}")
    
    if pos_row6['x'] < 10:
        print("Row 6 on Column 9 is OPEN!")
        # Walk Left to (1, 6)
        while mgba.get_coordinates()['x'] > 1:
            mgba.press_buttons(["Left"])
            time.sleep(0.05)
        # Walk Up to (1, 4)
        while mgba.get_coordinates()['y'] > 4:
            mgba.press_buttons(["Up"])
            time.sleep(0.05)
        print(f"Arrived at Target: {mgba.get_coordinates()}")
    else:
        print("Row 6 on Column 9 is CLOSED! Trying Row 4...")
        # Walk Up to (10, 4)
        for _ in range(2):
            mgba.press_buttons(["Up"])
            time.sleep(0.05)
        print(f"At Row 4: {mgba.get_coordinates()}")
        
        # Try to go Left
        mgba.press_buttons(["Left"])
        time.sleep(0.05)
        pos_row4 = mgba.get_coordinates()
        print(f"Coordinates after trying Left on Row 4: {pos_row4}")
        
        if pos_row4['x'] < 10:
            print("Row 4 on Column 9 is OPEN!")
            # Walk Left to (1, 4)
            while mgba.get_coordinates()['x'] > 1:
                mgba.press_buttons(["Left"])
                time.sleep(0.05)
            # Walk Down/Up to (1, 4) if needed (should already be at y=4)
            print(f"Arrived at Target: {mgba.get_coordinates()}")
        else:
            print("Row 4 on Column 9 is ALSO CLOSED!")

    # Take screenshot of final position
    scr = mgba.take_screenshot()
    print(f"Screenshot taken: {scr}")

test_routes()
