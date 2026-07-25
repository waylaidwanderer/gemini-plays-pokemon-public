import mgba
import time

def main():
    print("Starting systematic staircase search on column 13, rows 5 to 27...")
    # We are currently at (14, 15).
    # Let's first test rows 15 to 27 going Down.
    # On each row, we will try to press Left and check if we succeeded.
    # If we succeeded, we will print it and stop!
    
    current_y = 15
    for row in range(15, 28):
        # Move to (14, row)
        steps_down = row - current_y
        if steps_down > 0:
            mgba.press_buttons(["Down"] * steps_down + ["sleep 200"])
            current_y = row
            
        pos = mgba.get_coordinates()
        print(f"At (14, {row}). Coordinates: {pos}")
        
        # Try to step Left
        mgba.press_buttons(["Left", "sleep 300"])
        new_pos = mgba.get_coordinates()
        
        if new_pos['x'] == 13:
            print(f"SUCCESS!!! Found staircase on column 13 at row {row}!")
            return
        elif new_pos['x'] == 14:
            # We got blocked, which is normal
            pass
        else:
            # We warped or moved unexpectedly
            print(f"Unexpected movement: {new_pos}")
            return
            
    print("Rows 15 to 27 are completely blocked on column 13.")

if __name__ == '__main__':
    main()
