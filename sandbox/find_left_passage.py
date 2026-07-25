import mgba
import time

def test_left(row):
    # Try to step Left
    mgba.press_buttons(["Left", "sleep 320"])
    # If we succeeded, we will have moved to column 23
    # But since get_coordinates can be 0,0, let's step Right back just in case we succeeded!
    # Wait, if we succeeded, we want to know! But we can just print the coordinates or verify
    # actually, if we didn't succeed, pressing Right will do nothing or walk us Right.
    # So let's just step Right to return to column 24 if we did move Left.
    mgba.press_buttons(["Right", "sleep 320"])

def main():
    print("Searching for a leftward passage below row 27...")
    # Currently at (24, 27)
    
    # We will step Down, then try walking Left, then step Right (just in case), and repeat
    for row in range(28, 35):
        print(f"Testing row {row}...")
        mgba.press_buttons(["Down", "sleep 320"])
        test_left(row)
        
    final_img = mgba.take_screenshot()
    print(f"Final Screenshot: {final_img}")

if __name__ == "__main__":
    main()
