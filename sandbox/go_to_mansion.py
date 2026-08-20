import mgba
import time

def walk_to_mansion():
    print("Walking to Pokemon Mansion from Pokemon Center at (11, 12)...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    # 1. Walk Left to column 2
    # From (11, 12), walk Left to column 2
    for col in range(10, 1, -1):
        mgba.press_buttons(["Left"])
        time.sleep(0.4)
        pos = mgba.get_coordinates()
        print(f"Moved Left to column {col}. Current pos: {pos}")
        if pos['x'] != col:
            print("Blocked or walked into something! Adjusting...")
            mgba.take_screenshot()
            break
            
    # 2. From column 2, walk Up to row 3
    print("Walking Up column 2...")
    for row in range(11, 2, -1):
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        pos = mgba.get_coordinates()
        print(f"Moved Up to row {row}. Current pos: {pos}")
        if pos['y'] != row:
            print("Blocked or walked into something! Adjusting...")
            mgba.take_screenshot()
            break
            
    # Take screenshot at the northwest corner
    print("Arrived at northwest corner. Checking surroundings...")
    mgba.take_screenshot()

if __name__ == "__main__":
    walk_to_mansion()
