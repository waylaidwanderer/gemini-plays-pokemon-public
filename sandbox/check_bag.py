import mgba
import time

def main():
    print("Opening Start Menu...")
    mgba.press_buttons(["Start", "sleep 500"])
    
    # Take screenshot of menu
    print("Taking menu screenshot...")
    img = mgba.take_screenshot()
    print("Menu opened.")
    
    print("Moving cursor to PACK...")
    mgba.press_buttons(["Down", "sleep 200", "A", "sleep 800"])
    
    # Take screenshot of first pack page
    print("Taking page 1 screenshot...")
    mgba.take_screenshot()
    
    # Scroll down 3 times
    print("Scrolling down...")
    mgba.press_buttons(["Down", "sleep 150", "Down", "sleep 150", "Down", "sleep 150", "Down", "sleep 150"])
    
    print("Taking page 2 screenshot...")
    mgba.take_screenshot()
    
    # Scroll down more
    print("Scrolling down further...")
    mgba.press_buttons(["Down", "sleep 150", "Down", "sleep 150", "Down", "sleep 150", "Down", "sleep 150"])
    
    print("Taking page 3 screenshot...")
    mgba.take_screenshot()
    
    # Close menu
    print("Closing menu...")
    mgba.press_buttons(["B", "sleep 200", "B", "sleep 200", "B", "sleep 200"])
    
if __name__ == "__main__":
    main()
