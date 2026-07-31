import mgba
import time

def main():
    print("Navigating to Poké Ball at (1, 11)...")
    # Current pos: (2, 9)
    # Path: Right, Down, Down, Down, Down, Left, Left, Up, Up
    buttons = ["Right", "Down", "Down", "Down", "Down", "Left", "Left", "Up", "Up"]
    mgba.press_buttons(buttons)
    time.sleep(2)
    
    # We should be on the item pickup textbox now.
    # Let's press A to clear the textbox.
    mgba.press_buttons(["A"])
    time.sleep(1)
    
    pos = mgba.get_coordinates()
    print(f"Current position after picking up item: {pos}")
    mgba.take_screenshot()

if __name__ == '__main__':
    main()
