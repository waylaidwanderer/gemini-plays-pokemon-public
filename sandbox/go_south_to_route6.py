import mgba
import time

def main():
    # We start at (9, 30).
    # Let's walk right to (18, 30).
    # We will press Right 9 times.
    print("Walking east from 9 to 18...")
    buttons = ["Right"] * 9
    mgba.press_buttons(buttons)
    
    # Take screenshot and get coordinates
    time.sleep(0.5)
    img_path = mgba.take_screenshot()
    pos = mgba.get_coordinates()
    print(f"Position after walking east: {pos}")
    
    # Now let's try to walk south towards the Gatehouse (Row 39).
    # We'll walk down to row 36, then check pos, then walk more.
    print("Walking south...")
    mgba.press_buttons(["Down"] * 6)
    time.sleep(0.5)
    
    img_path = mgba.take_screenshot()
    pos = mgba.get_coordinates()
    print(f"Position after walking south: {pos}")

if __name__ == "__main__":
    main()
