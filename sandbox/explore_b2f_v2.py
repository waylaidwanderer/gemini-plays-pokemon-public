import mgba
import time

def main():
    print("Navigating to Poké Ball at (6, 12)...")
    # Current pos: (8, 11)
    # Path: Left, Left, Down
    buttons = ["Left", "Left", "Down"]
    mgba.press_buttons(buttons)
    time.sleep(2)
    
    # Press A to clear the textbox
    mgba.press_buttons(["A"])
    time.sleep(1)
    
    pos = mgba.get_coordinates()
    print(f"Current position: {pos}")
    mgba.take_screenshot()

if __name__ == '__main__':
    main()
