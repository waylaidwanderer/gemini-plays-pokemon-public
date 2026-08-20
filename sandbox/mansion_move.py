import mgba
import time

def test_east_3f():
    print("Testing if (18, 8) or (19, 8) are walkable...")
    # Current position: (17, 7)
    
    # 1. Walk Right to (18, 7)
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
    pos = mgba.get_coordinates()
    print("At:", pos)
    
    # Try to walk Down to (18, 8)
    if pos['x'] == 18 and pos['y'] == 7:
        mgba.press_buttons(["Down"])
        time.sleep(0.4)
        pos2 = mgba.get_coordinates()
        print("Tried Down at 18: position is now:", pos2)
        if pos2['y'] == 8:
            print("Row 8 column 18 is WALKABLE!")
            mgba.take_screenshot()
            return
            
    # If we couldn't go Down at 18, we should be at (18, 7).
    # 2. Walk Right to (19, 7)
    pos = mgba.get_coordinates()
    if pos['x'] == 18 and pos['y'] == 7:
        mgba.press_buttons(["Right"])
        time.sleep(0.4)
        pos = mgba.get_coordinates()
        print("At:", pos)
        
    # Try to walk Down to (19, 8)
    if pos['x'] == 19 and pos['y'] == 7:
        mgba.press_buttons(["Down"])
        time.sleep(0.4)
        pos2 = mgba.get_coordinates()
        print("Tried Down at 19: position is now:", pos2)
        if pos2['y'] == 8:
            print("Row 8 column 19 is WALKABLE!")
            mgba.take_screenshot()
            return

    # If both are blocked, let's walk Right to (22, 7) and take a screenshot to explore
    pos = mgba.get_coordinates()
    print("Both blocked. Exploring further east from:", pos)
    if pos['y'] == 7:
        while pos['x'] < 22:
            mgba.press_buttons(["Right"])
            time.sleep(0.4)
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                print("Hit obstacle going Right at:", pos)
                break
            pos = new_pos
            print("At:", pos)
            
    mgba.take_screenshot()

test_east_3f()
