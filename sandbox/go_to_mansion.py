import mgba
import time

def explore_and_find_mansion():
    print("Walking Right to column 11 from (4, 10)...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    # 1. Walk Right to column 11
    for col in range(5, 12):
        print(f"Moving Right to column {col}...")
        mgba.press_buttons(["Right"])
        time.sleep(0.4)
        pos = mgba.get_coordinates()
        print("Position:", pos)
        if pos['x'] != col:
            print("Blocked on Right!")
            mgba.take_screenshot()
            break
            
    # 2. Walk Up column 11 to the northern road
    # Let's try walking Up to row 3
    print("Walking Up column 11...")
    for row in range(9, 2, -1):
        print(f"Moving Up to row {row}...")
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        pos = mgba.get_coordinates()
        print("Position:", pos)
        if pos['y'] != row:
            print("Blocked on Up!")
            mgba.take_screenshot()
            break
            
    # 3. Walk Left to find Mansion entrance
    # The Mansion is on the northwest. Let's walk Left along row 3 or 4
    print("Walking Left to find Mansion entrance...")
    for col in range(10, 1, -1):
        print(f"Moving Left to column {col}...")
        mgba.press_buttons(["Left"])
        time.sleep(0.4)
        curr = mgba.get_coordinates()
        print("Position:", curr)
        
        # Check if we warped to Pokemon Mansion 1F.
        # Inside Mansion 1F, the coordinates are different (e.g. row > 20).
        if curr['y'] > 15:
            print("Successfully entered Pokemon Mansion!")
            mgba.take_screenshot()
            return True
            
    # Take screenshot at the end
    print("Final overworld position:", mgba.get_coordinates())
    mgba.take_screenshot()
    return False

if __name__ == "__main__":
    explore_and_find_mansion()
