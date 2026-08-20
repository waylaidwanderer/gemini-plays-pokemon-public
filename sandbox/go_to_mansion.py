import mgba
import time

def enter_mansion_real():
    print("Exiting Pokemon Lab lobby...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    # 1. Walk Down to exit Lab
    mgba.press_buttons(["Down"])
    time.sleep(1.5) # Wait for warp outside to (15, 12)
    
    pos = mgba.get_coordinates()
    print("Outside Pokemon Lab. Overworld position:", pos)
    
    # 2. Walk Right to column 19
    for col in range(16, 20):
        print(f"Moving Right to column {col}...")
        mgba.press_buttons(["Right"])
        time.sleep(0.4)
        print("Position:", mgba.get_coordinates())
        
    # 3. Walk Up column 19 to row 4
    print("Walking Up column 19 to row 4...")
    for row in range(11, 3, -1):
        print(f"Moving Up to row {row}...")
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        print("Position:", mgba.get_coordinates())
        
    # 4. Walk Left along row 4 to column 2
    print("Walking Left to northwest corner...")
    for col in range(18, 1, -1):
        print(f"Moving Left to column {col}...")
        mgba.press_buttons(["Left"])
        time.sleep(0.4)
        curr = mgba.get_coordinates()
        print("Position:", curr)
        
        # Check if we warped inside Pokemon Mansion 1F
        if curr['y'] > 15:
            print("SUCCESS! Warp detected. Entered Pokemon Mansion 1F!")
            mgba.take_screenshot()
            return True
            
    # Try one final Up step at column 2 row 4/3 just in case of door alignment
    print("Trying final Up step to enter...")
    mgba.press_buttons(["Up"])
    time.sleep(1.5)
    
    final_pos = mgba.get_coordinates()
    print("Final position:", final_pos)
    mgba.take_screenshot()
    return final_pos['y'] > 15

if __name__ == "__main__":
    enter_mansion_real()
