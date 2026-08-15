import mgba
import time

def main():
    print("Scrolling down the ITEM menu further...")
    # Currently, cursor is on SUPER ROD (3rd visible item, which is item #5).
    # Let's press Down 4 times to see the next items.
    mgba.press_buttons(["Down", "sleep 200", "Down", "sleep 200", "Down", "sleep 200", "Down", "sleep 250"])
    
    screenshot = mgba.take_screenshot()
    print(f"Screenshot after 4 more Down presses: {screenshot}")

if __name__ == "__main__":
    main()
