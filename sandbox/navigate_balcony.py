import mgba
import time

def move_to(target_x, target_y):
    current = mgba.get_coordinates()
    print(f"Starting at {current}")
    
    # Move vertically to Row 11 first
    while current['y'] > target_y:
        mgba.press_buttons(["Up"])
        time.sleep(0.1)
        next_pos = mgba.get_coordinates()
        if next_pos == current:
            print(f"Blocked at {current} while moving Up")
            return False
        current = next_pos
        print(f"Moved to {current}")
        
    while current['y'] < target_y:
        mgba.press_buttons(["Down"])
        time.sleep(0.1)
        next_pos = mgba.get_coordinates()
        if next_pos == current:
            print(f"Blocked at {current} while moving Down")
            return False
        current = next_pos
        print(f"Moved to {current}")

    # Move horizontally to Target X
    while current['x'] > target_x:
        mgba.press_buttons(["Left"])
        time.sleep(0.1)
        next_pos = mgba.get_coordinates()
        if next_pos == current:
            print(f"Blocked at {current} while moving Left")
            return False
        current = next_pos
        print(f"Moved to {current}")
        
    while current['x'] < target_x:
        mgba.press_buttons(["Right"])
        time.sleep(0.1)
        next_pos = mgba.get_coordinates()
        if next_pos == current:
            print(f"Blocked at {current} while moving Right")
            return False
        current = next_pos
        print(f"Moved to {current}")
        
    print(f"Successfully reached target {current}")
    return True

# Attempt to navigate to (3, 11)
success = move_to(3, 11)
if success:
    print("Reached (3, 11) successfully!")
else:
    print("Navigation failed.")
