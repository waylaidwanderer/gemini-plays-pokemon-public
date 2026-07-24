import mgba
import time

def main():
    print("Testing column 16 for walkable gaps on rows 26 to 34...")
    # Starting position: (12, 24)
    # We walk to (15, 24) first
    mgba.press_buttons(["Right", "Right", "Right", "sleep 250"])
    pos = mgba.get_coordinates()
    print(f"Start at (15, 24). Coordinates: {pos}")
    
    # We will walk Down to row 34, and on each row we try to step Right to column 16,
    # then step back Left if we succeeded.
    # Rows to test: 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34
    
    # Let's perform the test row by row
    current_y = 24
    for row in range(24, 35):
        # We are at (15, current_y).
        # Walk to (15, row)
        diff = row - current_y
        if diff > 0:
            mgba.press_buttons(["Down"] * diff + ["sleep 250"])
            current_y = row
            
        # Check coordinates to make sure we are at (15, row)
        pos_before = mgba.get_coordinates()
        
        # Try to step Right
        mgba.press_buttons(["Right", "sleep 250"])
        pos_after = mgba.get_coordinates()
        
        # If position X is now 16, we succeeded!
        # Note: if get_coordinates() returns 0,0, we can also check if we moved by seeing if they are different
        # but since we can't trust 0,0, we should check if they are different and not 0,0.
        # Actually, if we succeed, we warp? No, if we succeed, we are on column 16.
        # Let's print the result
        print(f"Row {row}: {pos_before} -> {pos_after}")
        
        # If we succeeded, we walk back Left
        # Since we might not know if we succeeded, we can just press Left anyway to be safe!
        mgba.press_buttons(["Left", "sleep 250"])
        current_y = row # make sure we track y
        
if __name__ == "__main__":
    main()
