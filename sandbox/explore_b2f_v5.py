import mgba
import time

def main():
    print("Navigating to (3, 13)...")
    # Current pos: (2, 9)
    # Path: Right, Down, Down, Down, Down
    mgba.press_buttons(["Right", "Down", "Down", "Down", "Down"])
    time.sleep(2)
    
    pos = mgba.get_coordinates()
    print(f"Current position: {pos}")
    mgba.take_screenshot()

if __name__ == '__main__':
    main()
