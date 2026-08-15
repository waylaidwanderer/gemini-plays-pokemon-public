import mgba
import time

def main():
    print("Dismissing dialogue and opening Start menu...")
    # Press B 3 times to clear the dialogue
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300", "B", "sleep 500"])
    
    # Press Start to open the menu
    mgba.press_buttons(["Start", "sleep 500"])
    
    screenshot = mgba.take_screenshot()
    print(f"Screenshot of Start menu: {screenshot}")

if __name__ == "__main__":
    main()
