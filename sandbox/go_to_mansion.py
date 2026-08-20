import mgba
import time

def go_to_mansion():
    print("Exiting Pokemon Lab first...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    # Walk Down to exit Lab
    for row in range(4, 9):
        print(f"Moving Down to row {row} inside Lab...")
        mgba.press_buttons(["Down"])
        time.sleep(0.4)
        
    time.sleep(2.0) # Wait for warp to Cinnabar Island overworld
    
    pos = mgba.get_coordinates()
    print("Outside Pokemon Lab. Overworld position:", pos)
    
    # 2. Walk Down to (6, 11) to clear the door
    print("Stepping Down to clear the door...")
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
    print("Position:", mgba.get_coordinates())
    
    # 3. Walk Left to column 2
    for col in range(5, 1, -1):
        print(f"Moving Left to column {col}...")
        mgba.press_buttons(["Left"])
        time.sleep(0.4)
        print("Position:", mgba.get_coordinates())
        
    # 4. Walk Up column 2 to the northwest corner
    print("Walking Up column 2 to find Mansion entrance...")
    for row in range(10, 2, -1):
        print(f"Moving Up to row {row}...")
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        curr = mgba.get_coordinates()
        print("Position:", curr)
        
        # Check if we warped to Pokemon Mansion 1F.
        # Mansion 1F coordinates are different from Cinnabar Island overworld (height/width differs, and start pos is around column 8-10, row 27).
        # We can detect if the position changed to something like row 27.
        if curr['y'] > 15:
            print("Successfully warped inside Pokemon Mansion!")
            mgba.take_screenshot()
            return True
            
    # Take screenshot at the end
    print("Final overworld position:", mgba.get_coordinates())
    mgba.take_screenshot()
    return False

if __name__ == "__main__":
    go_to_mansion()
