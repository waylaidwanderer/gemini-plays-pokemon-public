import mgba
import time

def walk_to_drop_via_row6():
    print("Walking to balcony drop from (12, 5) via Row 6 in State B...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    pos = mgba.get_coordinates()
    print("Start position:", pos)
    
    # 1. Step Down to (12, 6)
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
    curr = mgba.get_coordinates()
    print("Position after Down:", curr)
    if curr['x'] != 12 or curr['y'] != 6:
        print("Failed to step Down to (12, 6)!")
        mgba.take_screenshot()
        return False
        
    # 2. Walk Right along row 6 to column 20
    for col in range(13, 21):
        print(f"At {mgba.get_coordinates()}. Moving Right to ({col}, 6)...")
        mgba.press_buttons(["Right"])
        time.sleep(0.4)
        
        curr = mgba.get_coordinates()
        if curr['x'] != col or curr['y'] != 6:
            print(f"BLOCKED at ({col}, 6)! Ended at {curr}")
            mgba.take_screenshot()
            return False
            
    # 3. Step Up to (20, 5)
    print("Stepping Up to (20, 5)...")
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    curr = mgba.get_coordinates()
    print("Position after Up:", curr)
    if curr['x'] != 20 or curr['y'] != 5:
        print("Failed to step Up to (20, 5)!")
        mgba.take_screenshot()
        return False
        
    # 4. Walk Right along row 5 to column 24
    for col in range(21, 25):
        print(f"At {mgba.get_coordinates()}. Moving Right to ({col}, 5)...")
        mgba.press_buttons(["Right"])
        time.sleep(0.4)
        
        curr = mgba.get_coordinates()
        if curr['x'] != col or curr['y'] != 5:
            print(f"BLOCKED at ({col}, 5)! Ended at {curr}")
            mgba.take_screenshot()
            return False
            
    # 5. Walk Down column 24 to row 14
    for row in range(6, 15):
        print(f"At {mgba.get_coordinates()}. Moving Down to (24, {row})...")
        mgba.press_buttons(["Down"])
        time.sleep(0.4)
        
        curr = mgba.get_coordinates()
        if curr['x'] != 24 or curr['y'] != row:
            print(f"BLOCKED at (24, {row})! Ended at {curr}")
            mgba.take_screenshot()
            return False
            
    # 6. Step Left to drop
    print("At balcony drop! Stepping Left to warp...")
    mgba.press_buttons(["Left"])
    time.sleep(2.0) # wait for warp
    
    final_pos = mgba.get_coordinates()
    print("Landed on 1F! Position:", final_pos)
    mgba.take_screenshot()
    return True

if __name__ == "__main__":
    walk_to_drop_via_row6()
