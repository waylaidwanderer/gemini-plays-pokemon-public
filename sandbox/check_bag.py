import mgba
import time

def main():
    print("Scrolling down to check the last items in the list...")
    # Cursor is currently on MAX REVIVE (item #9).
    # Let's press Down 2 times to see if we can highlight HM03 and whatever is below it.
    mgba.press_buttons(["Down", "sleep 200", "Down", "sleep 250"])
    
    screenshot = mgba.take_screenshot()
    print(f"Screenshot after 2 Down presses: {screenshot}")

if __name__ == "__main__":
    main()
