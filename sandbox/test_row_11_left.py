import mgba
import time

def step_one(direction, target_x, target_y):
    pos_before = mgba.get_coordinates()
    print(f"Moving {direction} to ({target_x}, {target_y}). Current: {pos_before}")
    mgba.press_buttons([direction])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        # Try robust escape just in case we hit a battle
        print("Blocked or in battle. Attempting run...")
        mgba.press_buttons(["Down", "sleep 250", "Right", "sleep 250", "A", "sleep 1000", "B"])
        time.sleep(2.0)
        # Try moving again
        mgba.press_buttons([direction])
        time.sleep(0.4)
        pos_after = mgba.get_coordinates()
        
    if pos_after['x'] == target_x and pos_after['y'] == target_y:
        return True
    return False

def main():
    pos = mgba.get_coordinates()
    print(f"Starting at: {pos}")
    
    # We want to go Left along Row 11 to Column 3
    if pos['y'] != 11:
        print("Not on Row 11! Aborting.")
        return
        
    for x in range(pos['x'] - 1, 2, -1):
        if not step_one("Left", x, 11):
            print(f"Failed to go Left to Column {x}.")
            break
            
    print(f"Ending position: {mgba.get_coordinates()}")

if __name__ == "__main__":
    main()
