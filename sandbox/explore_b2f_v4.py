import mgba
import time

def main():
    print("Navigating to far-left vertical corridor...")
    # Current pos: (10, 12)
    # Path to (3, 11): Up, Left x7
    buttons = ["Up", "Left", "Left", "Left", "Left", "Left", "Left", "Left"]
    mgba.press_buttons(buttons)
    time.sleep(2)
    
    pos = mgba.get_coordinates()
    print(f"Position at column 3: {pos}")
    
    # Now walk Down as far as possible to find the bottom corridor
    # Let's do 10 steps Down
    mgba.press_buttons(["Down"] * 10)
    time.sleep(3)
    
    pos = mgba.get_coordinates()
    print(f"Final position: {pos}")
    mgba.take_screenshot()

if __name__ == '__main__':
    main()
