import mgba
import time

def test_bottom_path():
    print("Navigating back to (12, 11) and testing bottom paths...")
    # Current position: (15, 7)
    
    # 1. Walk Left to (12, 7) (3 steps Left)
    for i in range(3):
        mgba.press_buttons(["Left"])
        time.sleep(0.4)
        print("At:", mgba.get_coordinates())
        
    # 2. Walk Down to (12, 11) (4 steps Down)
    for i in range(4):
        mgba.press_buttons(["Down"])
        time.sleep(0.4)
        print("At:", mgba.get_coordinates())
        
    # Now we are at (12, 11).
    # 3. Test walking Right to (13, 11)
    pos = mgba.get_coordinates()
    if pos['x'] == 12 and pos['y'] == 11:
        mgba.press_buttons(["Right"])
        time.sleep(0.4)
        pos2 = mgba.get_coordinates()
        print("Tried Right at (12, 11): position is now:", pos2)
        if pos2['x'] == 13:
            print("(13, 11) is WALKABLE!")
            mgba.take_screenshot()
            return
            
    # 4. If blocked, try going Down to (12, 12) then Right to (13, 12)
    pos = mgba.get_coordinates()
    if pos['x'] == 12 and pos['y'] == 11:
        mgba.press_buttons(["Down"])
        time.sleep(0.4)
        pos = mgba.get_coordinates()
        print("At:", pos)
        
    if pos['x'] == 12 and pos['y'] == 12:
        mgba.press_buttons(["Right"])
        time.sleep(0.4)
        pos2 = mgba.get_coordinates()
        print("Tried Right at (12, 12): position is now:", pos2)
        if pos2['x'] == 13:
            print("(13, 12) is WALKABLE!")
            # Try to walk Up to (13, 11)
            mgba.press_buttons(["Up"])
            time.sleep(0.4)
            pos3 = mgba.get_coordinates()
            print("Tried Up at (13, 12): position is now:", pos3)
            
    mgba.take_screenshot()

test_bottom_path()
