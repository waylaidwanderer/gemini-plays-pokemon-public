import mgba
import time

def main():
    print("Mashing B to clear dialogue, then opening Start menu...")
    # Press B 10 times with delay to guarantee exiting any dialogue/menus
    for _ in range(10):
        mgba.press_buttons(["B", "sleep 200"])
    
    # Press Start to open the menu
    mgba.press_buttons(["Start", "sleep 500"])
    
    screenshot = mgba.take_screenshot()
    print(f"Screenshot of Start menu: {screenshot}")

if __name__ == "__main__":
    main()
