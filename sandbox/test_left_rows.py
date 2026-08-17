import mgba
import time

def run():
    print("--- PROBING ALL ROWS FOR WESTWARD CROSSING ---")
    
    # We are currently at (24, 25).
    # Let's write a loop to test rows from 20 up to 31.
    # To do this safely, we will walk to (24, y), try to walk Left.
    # If our position changes to x=23, we know it's a success! We then walk back right to x=24 and record it.
    
    successes = []
    
    # Let's first walk Up to row 20 to start from the top.
    # From (24, 25) to (24, 20) is 5 steps UP.
    print("Walking to Row 20...")
    for _ in range(5):
        mgba.press_buttons(["Up"])
        time.sleep(0.2)
        
    pos = mgba.get_coordinates()
    current_y = pos['y']
    print(f"Starting probe at row {current_y}...")
    
    # We will probe rows from current_y down to 31.
    while current_y <= 31:
        # Try to step Left
        mgba.press_buttons(["Left"])
        time.sleep(0.25)
        new_pos = mgba.get_coordinates()
        
        if new_pos['x'] == 23:
            print(f"-> SUCCESS! Row {current_y} is OPEN to the west!")
            successes.append(current_y)
            # Step back Right
            mgba.press_buttons(["Right"])
            time.sleep(0.25)
        else:
            # We didn't move Left. So Row current_y is blocked on Column 23.
            pass
            
        # Move Down to the next row
        mgba.press_buttons(["Down"])
        time.sleep(0.25)
        pos = mgba.get_coordinates()
        current_y = pos['y']
        # If we failed to move Down, we are blocked, break the loop
        if pos['x'] != 24:
            print("Error: walked off column 24!")
            break
            
    print("Probe complete! Open rows to the west:", successes)
    mgba.take_screenshot()

if __name__ == "__main__":
    run()
