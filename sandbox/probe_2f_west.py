import mgba
import time

def step_one(direction, target_x, target_y):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        # Check if in battle and escape
        mgba.press_buttons(["Down", "sleep 250", "Right", "sleep 250", "A", "sleep 1000", "B"])
        time.sleep(2.0)
        mgba.press_buttons([direction])
        time.sleep(0.4)
        pos_after = mgba.get_coordinates()
        
    if pos_after['x'] == target_x and pos_after['y'] == target_y:
        return True
    return False

def main():
    print("probe_2f_west: Starting...")
    pos = mgba.get_coordinates()
    
    # We are currently at (22, 1).
    # Let's walk to (12, 1)
    for x in range(21, 11, -1):
        if not step_one("Left", x, 1):
            print("Failed to walk to Column 12.")
            return
            
    # For each row from 1 to 6, we try to go Left on Column 12
    open_rows = []
    for y in range(1, 7):
        print(f"Testing Row {y}...")
        # Walk to (12, y)
        current = mgba.get_coordinates()
        while current['y'] != y:
            dy = y - current['y']
            dir_step = "Down" if dy > 0 else "Up"
            if not step_one(dir_step, 12, current['y'] + (1 if dy > 0 else -1)):
                print(f"Failed to reach (12, {y})")
                break
            current = mgba.get_coordinates()
            
        current = mgba.get_coordinates()
        if current['y'] == y:
            # Try to walk Left to Column 11
            if step_one("Left", 11, y):
                print(f"Row {y} is open to Column 11!")
                open_rows.append(y)
                # Step Right back to Column 12 to continue testing
                step_one("Right", 12, y)
            else:
                print(f"Row {y} is blocked at Column 11.")
                
    print(f"Testing completed. Open rows to Column 11: {open_rows}")

if __name__ == "__main__":
    main()
