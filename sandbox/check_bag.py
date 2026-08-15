import mgba
import time

def main():
    print("Scrolling down the ITEM menu...")
    # Currently, cursor is on the first item (MOON STONE).
    # Let's press Down 4 times to see the next items.
    mgba.press_buttons(["Down", "sleep 200", "Down", "sleep 200", "Down", "sleep 200", "Down", "sleep 250"])
    
    screenshot = mgba.take_screenshot()
    print(f"Screenshot after 4 Down presses: {screenshot}")

if __name__ == "__main__":
    main()
