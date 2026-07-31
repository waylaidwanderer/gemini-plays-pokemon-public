import mgba
import time

def main():
    print("Navigating from (3, 13) back to right side of the maze...")
    # Currently at (3, 13)
    # Path: Right to (4, 13), Down to (4, 14), Down onto (4, 15) spinner
    mgba.press_buttons(["Right", "Down", "Down"])
    time.sleep(3) # Wait for spin to complete (spins to 8, 13)
    
    pos = mgba.get_coordinates()
    print(f"Pos after spin 1: {pos}")
    
    # Path: Right x2 to (10, 13), Up to (10, 12), Up to (10, 11)
    mgba.press_buttons(["Right", "Right", "Up", "Up"])
    time.sleep(1.5)
    
    # Path: Right x2 onto (12, 11) spinner -> spins us to (2, 9)
    mgba.press_buttons(["Right", "Right"])
    time.sleep(4.0) # Wait for spin to complete
    
    pos = mgba.get_coordinates()
    print(f"Pos after spin 2: {pos}")
    
    # Path: Right to (3, 9), Down to (3, 11), Right onto (4, 11) spinner -> spins us to (8, 11)
    mgba.press_buttons(["Right", "Down", "Down", "Right"])
    time.sleep(3.0) # Wait for spin to complete
    
    pos = mgba.get_coordinates()
    print(f"Pos after spin 3: {pos}")
    
    # Path: Right x5 to (13, 11) -> wait, (12, 11) is UP spinner!
    # No, from (8, 11), can we go Right?
    # Let's check coordinates. We are at (8, 11).
    # Path to columns 25-28:
    # Walk Right x5: (8, 11) -> (13, 11)?
    # Wait, (12, 11) is an UP spinner!
    # If we walk Right from (11, 11) onto (12, 11), we will spin!
    # But wait, is there another row?
    # Row 13 is walkable: (8, 13) to (24, 13)!
    # Let's go to Row 13!
    # From (8, 11): Down to (8, 12) (UP spinner). No!
    # Walk Right to (9, 11) -> (10, 11) -> Down to (10, 12) -> (10, 13) -> walk Right to (24, 13)!
    # Yes! Row 13 is completely clear of spinners all the way to column 24!
    mgba.press_buttons(["Right", "Right", "Down", "Down", "Right", "Right", "Right", "Right", "Right"])
    time.sleep(2)
    
    pos = mgba.get_coordinates()
    print(f"Position at column 15, row 13: {pos}")
    
    # Let's walk all the way to (25, 13)
    mgba.press_buttons(["Right"] * 10)
    time.sleep(2)
    
    pos = mgba.get_coordinates()
    print(f"Position at right side: {pos}")
    mgba.take_screenshot()

if __name__ == '__main__':
    main()
