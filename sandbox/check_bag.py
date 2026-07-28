import mgba
import time

def main():
    print("Opening menu...")
    mgba.press_buttons(["Start", "sleep 500"])
    
    # Let's take a screenshot of the main menu first to see where the cursor is
    img1 = mgba.take_screenshot()
    print(f"Main menu screenshot saved to: {img1}")
    
    # Press Down twice and A to open Item menu
    print("Navigating to ITEM...")
    mgba.press_buttons(["Down", "sleep 200", "Down", "sleep 200", "A", "sleep 500"])
    
    # Take screenshot of Item menu
    img2 = mgba.take_screenshot()
    print(f"Item menu screenshot saved to: {img2}")
    
    # Close menu to restore state
    print("Closing menu...")
    mgba.press_buttons(["B", "sleep 200", "B", "sleep 200", "B", "sleep 200"])
    print("Done!")

if __name__ == "__main__":
    main()
