import mgba
import time

def main():
    print("Navigating to RIGHT spinner at (4, 11)...")
    # Current pos: (1, 12)
    # Path to (3, 11): Down, Right, Right, Up, Up
    # Then step Right onto (4, 11) spinner
    buttons = ["Down", "Right", "Right", "Up", "Up", "Right"]
    mgba.press_buttons(buttons)
    time.sleep(3) # Wait for spin to complete
    
    pos = mgba.get_coordinates()
    print(f"Current position after spin: {pos}")
    mgba.take_screenshot()

if __name__ == '__main__':
    main()
