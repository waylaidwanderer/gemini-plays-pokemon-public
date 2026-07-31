import mgba
import time

def main():
    print("Navigating through southern spinner at (11, 14)...")
    # Current pos: (10, 12)
    # Path: Down, Down, Right (onto 11, 14 spinner)
    buttons = ["Down", "Down", "Right"]
    mgba.press_buttons(buttons)
    time.sleep(3) # Wait for spin to complete
    
    pos = mgba.get_coordinates()
    print(f"Current position after spin: {pos}")
    mgba.take_screenshot()

if __name__ == '__main__':
    main()
