import mgba
import time

def main():
    print("Systematic search for leftward passage on B1F columns 18-19...")
    # Currently at B1F (25, 15)
    
    # Let's walk to column 24 first
    mgba.press_buttons(["Left", "sleep 320"])
    
    # We will test each row from 14 to 34
    for row in range(14, 35):
        print(f"Testing row {row}...")
        # Walk to (24, row)
        current_pos = mgba.get_coordinates()
        # Since get_coordinates might be 0,0, we track our row manually.
        # But we can also use absolute movements or step-by-step
        # To go to row, we can just calculate the difference from the current row
        # Our current row is 'row' (after we move there).
        # Wait, if we start at (24, 15), we can just walk Down row-by-row!
        # At each row, we attempt to walk Left 8 steps.
        # If we successfully walked Left (meaning we didn't bump immediately, or we moved),
        # how do we check? We can check if get_coordinates() X coordinate is less than 24!
        # Wait, if get_coordinates() returns 0,0, we can also check if the screen changed or if we can walk Left several steps.
        # Let's just try to walk Left 6 steps. If we succeed, we will be at column 18.
        # Then we walk Right 6 steps to return to column 24.
        # If we didn't succeed (bumped), walking Right will do nothing or walk us Right (but we are already at the wall, so it does nothing!).
        # This is extremely safe and self-correcting!
        
        # Step 1: Attempt to walk Left 6 steps
        mgba.press_buttons(["Left"] * 6 + ["sleep 320"])
        pos_after_left = mgba.get_coordinates()
        
        # Step 2: Walk Right 6 steps to return to column 24 (just in case we moved Left)
        mgba.press_buttons(["Right"] * 6 + ["sleep 320"])
        
        print(f"Row {row} left test: pos_after_left={pos_after_left}")
        
        # Step 3: Move Down 1 step to the next row
        mgba.press_buttons(["Down", "sleep 320"])
        
    final_img = mgba.take_screenshot()
    print(f"Final Screenshot: {final_img}")

if __name__ == "__main__":
    main()
