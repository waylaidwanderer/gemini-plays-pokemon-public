import mgba
import time

def main():
    print("Navigating to top-left area on B2F...")
    pos = mgba.get_coordinates()
    print(f"Start pos: {pos}")
    
    # We are at (8, 11).
    # Path to UP spinner at (10, 10): Right, Right, Up
    mgba.press_buttons(["Right", "Right", "Up"])
    time.sleep(3) # Wait for spin to complete
    
    pos = mgba.get_coordinates()
    print(f"Position after spin: {pos}")
    
    # Path to (1, 7): Left, Up, Up
    mgba.press_buttons(["Left", "Up", "Up"])
    time.sleep(1)
    
    pos = mgba.get_coordinates()
    print(f"Position at (1, 7): {pos}")
    
    # Let's explore the top-left further (walk Right along row 7)
    mgba.press_buttons(["Right", "Right", "Right"])
    time.sleep(1)
    
    pos = mgba.get_coordinates()
    print(f"Position after walking row 7: {pos}")
    mgba.take_screenshot()

if __name__ == '__main__':
    main()
