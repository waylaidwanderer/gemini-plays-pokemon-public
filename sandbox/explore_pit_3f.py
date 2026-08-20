import mgba
import time

def main():
    print("Exploring surrounding tiles of (24, 5) to find the pit on 3F...")
    
    # We are currently at (24, 5). Let's check coordinates.
    pos = mgba.get_coordinates()
    print("Start position:", pos)
    
    # 1. Try walking to (24, 6) (Down)
    print("Testing (24, 6) (Down)...")
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    pos_test = mgba.get_coordinates()
    print("Position:", pos_test)
    if pos_test['x'] != 24 or pos_test['y'] != 6:
        # We fell or warped!
        print("FELL THROUGH PIT! Landing position:", pos_test)
        mgba.take_screenshot()
        return
        
    # Walk back UP to (24, 5)
    print("Walking back Up to (24, 5)...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    # 2. Try walking to (25, 5) (Right)
    print("Testing (25, 5) (Right)...")
    mgba.press_buttons(["Right"])
    time.sleep(0.5)
    pos_test = mgba.get_coordinates()
    print("Position:", pos_test)
    if pos_test['x'] != 25 or pos_test['y'] != 5:
        print("FELL THROUGH PIT! Landing position:", pos_test)
        mgba.take_screenshot()
        return
        
    # Walk back Left to (24, 5)
    print("Walking back Left to (24, 5)...")
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
    
    # 3. Try walking to (23, 5) (Left)
    print("Testing (23, 5) (Left)...")
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
    pos_test = mgba.get_coordinates()
    print("Position:", pos_test)
    if pos_test['x'] != 23 or pos_test['y'] != 5:
        print("FELL THROUGH PIT! Landing position:", pos_test)
        mgba.take_screenshot()
        return
        
    # Walk back Right to (24, 5)
    print("Walking back Right to (24, 5)...")
    mgba.press_buttons(["Right"])
    time.sleep(0.5)
    
    print("No pit found immediately adjacent to (24, 5).")
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
