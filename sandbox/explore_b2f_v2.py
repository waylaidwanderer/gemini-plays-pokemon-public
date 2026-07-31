import mgba
import time

def main():
    print("Exploring the right side of the B2F maze...")
    # Current pos: (6, 11)
    # Path: Right, Right, Right, Right, Down
    buttons = ["Right", "Right", "Right", "Right", "Down"]
    mgba.press_buttons(buttons)
    time.sleep(2)
    
    pos = mgba.get_coordinates()
    print(f"Current position: {pos}")
    mgba.take_screenshot()

if __name__ == '__main__':
    main()
