import mgba
import time

def main():
    print("Navigating to UP spinner at (12, 13)...")
    pos = mgba.get_coordinates()
    print(f"Current pos: {pos}")
    
    # We are at (16, 10).
    # Path: Left, Left, Down, Down, Down, Left, Left
    mgba.press_buttons(["Left", "Left", "Down", "Down", "Down", "Left", "Left"])
    time.sleep(3) # Wait for spin to complete
    
    pos = mgba.get_coordinates()
    print(f"Position after spin: {pos}")
    mgba.take_screenshot()

if __name__ == '__main__':
    main()
