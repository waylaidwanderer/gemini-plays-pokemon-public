import mgba
import time

def find_mansion():
    print("Dismissing gym door message...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    # 1. Walk Down to row 6
    for row in range(5, 7):
        mgba.press_buttons(["Down"])
        time.sleep(0.4)
        print("Position after Down:", mgba.get_coordinates())
        
    # 2. Walk Left to column 11
    for col in range(17, 10, -1):
        mgba.press_buttons(["Left"])
        time.sleep(0.4)
        print(f"Moved Left to column {col}:", mgba.get_coordinates())
        
    # 3. Walk Up column 11 to the top road (row 2 or 3)
    print("Walking Up column 11...")
    for row in range(5, 1, -1):
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        pos = mgba.get_coordinates()
        print(f"Moved Up to row {row}: {pos}")
        if pos['y'] != row:
            print("Blocked on Up!")
            break
            
    # 4. Walk Left as far as we can from our current northern row
    curr_pos = mgba.get_coordinates()
    print("Current position at top road:", curr_pos)
    
    print("Walking Left along northern road...")
    for col in range(curr_pos['x'] - 1, 0, -1):
        mgba.press_buttons(["Left"])
        time.sleep(0.4)
        curr = mgba.get_coordinates()
        print(f"Moved Left to column {col}: {curr}")
        
        # Check if we warped inside Pokemon Mansion 1F.
        # Mansion 1F y is usually around 27.
        if curr['y'] > 15:
            print("SUCCESS! Warp detected. Entered Pokemon Mansion 1F!")
            mgba.take_screenshot()
            return True
            
    # Take screenshot at the end of exploration
    print("Finished exploration. Coordinates:", mgba.get_coordinates())
    mgba.take_screenshot()
    return False

if __name__ == "__main__":
    find_mansion()
