import mgba
import time

def walk_to_drop():
    print("Walking to balcony drop from (12, 5) in State B...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    pos = mgba.get_coordinates()
    print("Start position:", pos)
    
    # We want to walk Right along row 5 to column 24
    for col in range(13, 25):
        print(f"At {mgba.get_coordinates()}. Moving Right to ({col}, 5)...")
        mgba.press_buttons(["Right"])
        time.sleep(0.4)
        
        # Check if we moved
        curr = mgba.get_coordinates()
        if curr['x'] != col or curr['y'] != 5:
            print(f"BLOCKED! Ended at {curr} instead of ({col}, 5)")
            mgba.take_screenshot()
            return False
            
    # Now walk Down column 24 to row 14
    for row in range(6, 15):
        print(f"At {mgba.get_coordinates()}. Moving Down to (24, {row})...")
        mgba.press_buttons(["Down"])
        time.sleep(0.4)
        
        curr = mgba.get_coordinates()
        if curr['x'] != 24 or curr['y'] != row:
            print(f"BLOCKED! Ended at {curr} instead of (24, {row})")
            mgba.take_screenshot()
            return False
            
    # Drop Left from (24, 14)
    print("At balcony drop! Stepping Left to warp...")
    mgba.press_buttons(["Left"])
    time.sleep(2.0) # wait for warp
    
    final_pos = mgba.get_coordinates()
    print("Landed on 1F! Position:", final_pos)
    mgba.take_screenshot()
    return True

if __name__ == "__main__":
    walk_to_drop()
