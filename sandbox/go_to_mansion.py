import mgba
import time

def find_mansion():
    print("Walking to column 15 from (8, 12)...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    # 1. Walk Right from (8, 12) to (15, 12)
    for col in range(9, 16):
        mgba.press_buttons(["Right"])
        time.sleep(0.4)
        pos = mgba.get_coordinates()
        print(f"Moved Right to column {col}. Current pos: {pos}")
        if pos['x'] != col:
            print("Blocked on Right!")
            mgba.take_screenshot()
            return False
            
    # 2. Walk Up column 15 to row 3
    print("Walking Up column 15...")
    for row in range(11, 2, -1):
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        pos = mgba.get_coordinates()
        print(f"Moved Up to row {row}. Current pos: {pos}")
        if pos['y'] != row:
            print("Blocked on Up!")
            mgba.take_screenshot()
            return False
            
    # 3. Walk Left to find Mansion entrance
    # Mansion is around (2, 3) or (2, 4). Walk Left to column 2
    print("Walking Left to find Mansion...")
    for col in range(14, 1, -1):
        mgba.press_buttons(["Left"])
        time.sleep(0.4)
        curr = mgba.get_coordinates()
        print(f"Moved Left to column {col}. Current pos: {curr}")
        
        # Check if we warped inside Pokemon Mansion 1F.
        # Mansion 1F has different coordinates (y is usually 27 at the entrance)
        if curr['y'] > 15:
            print("SUCCESS! Warp detected. Entered Pokemon Mansion 1F!")
            mgba.take_screenshot()
            return True
            
    # Take screenshot at the end if no warp occurred
    print("Finished path. Checking position:")
    mgba.take_screenshot()
    return False

if __name__ == "__main__":
    find_mansion()
