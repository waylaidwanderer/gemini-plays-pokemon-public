import mgba
import time

def main():
    print("Selecting ITEM and taking screenshot...")
    # Cursor is on POKEMON. Down moves it to ITEM.
    mgba.press_buttons(["Down", "sleep 250", "A", "sleep 1000"])
    
    screenshot = mgba.take_screenshot()
    print(f"Screenshot of ITEM bag: {screenshot}")

if __name__ == "__main__":
    main()
