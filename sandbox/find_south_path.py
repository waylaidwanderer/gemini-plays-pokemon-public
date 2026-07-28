import mgba
import time

def explore_path():
    print("Starting pathfinding script from current position...")
    pos = mgba.get_coordinates()
    print(f"Starting Coords: {pos}")
    
    # We want to search columns to the right first (up to x=35)
    # We are at x=21, y=27 (or whatever current y is, let's make sure we are on row 27)
    # If we are not on row 27, let's navigate to row 27 first.
    if pos['y'] != 27:
        print(f"Error: Expected to be on row 27, but we are at {pos}")
        return

    # Let's search from x=21 to x=35
    for target_x in range(21, 36):
        # Move to target_x on row 27
        current_pos = mgba.get_coordinates()
        dx = target_x - current_pos['x']
        if dx > 0:
            for _ in range(dx):
                mgba.press_buttons(["Right"])
                time.sleep(0.3)
        
        current_pos = mgba.get_coordinates()
        if current_pos['x'] != target_x:
            print(f"Blocked going Right at x={current_pos['x']}. Stopping rightward search.")
            break
            
        print(f"At x={target_x}, y=27. Testing Down...")
        # Try to walk Down 2 steps
        mgba.press_buttons(["Down"])
        time.sleep(0.3)
        test_pos = mgba.get_coordinates()
        if test_pos['y'] > 27:
            print(f"SUCCESS! Found path Down at x={target_x}. Position: {test_pos}")
            # Try to walk one more step Down to be secure
            mgba.press_buttons(["Down"])
            time.sleep(0.3)
            return
        else:
            # We are blocked, we must still be at y=27. Just continue to next column.
            # Make sure we face Right for the next step (walking Right automatically does this, but good to know)
            pass

    # If rightward search fails, let's return to x=21 and search Left (down to x=10)
    print("Rightward search completed or blocked. Returning to x=21...")
    current_pos = mgba.get_coordinates()
    dx = current_pos['x'] - 21
    if dx > 0:
        for _ in range(dx):
            mgba.press_buttons(["Left"])
            time.sleep(0.3)
            
    print("Starting leftward search...")
    for target_x in range(21, 9, -1):
        current_pos = mgba.get_coordinates()
        dx = current_pos['x'] - target_x
        if dx > 0:
            for _ in range(dx):
                mgba.press_buttons(["Left"])
                time.sleep(0.3)
                
        current_pos = mgba.get_coordinates()
        if current_pos['x'] != target_x:
            print(f"Blocked going Left at x={current_pos['x']}. Stopping leftward search.")
            break
            
        print(f"At x={target_x}, y=27. Testing Down...")
        mgba.press_buttons(["Down"])
        time.sleep(0.3)
        test_pos = mgba.get_coordinates()
        if test_pos['y'] > 27:
            print(f"SUCCESS! Found path Down at x={target_x}. Position: {test_pos}")
            mgba.press_buttons(["Down"])
            time.sleep(0.3)
            return

    print("Pathfinding complete. No open path south found on row 27 between x=10 and x=35.")

explore_path()
