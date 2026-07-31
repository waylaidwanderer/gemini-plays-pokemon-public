import mgba
import time

def main():
    print("Starting B2F path test...")
    pos = mgba.get_coordinates()
    print(f"Start pos: {pos}")
    
    # We are at (20, 12).
    # Path: Up, Up, Left, Left, Left
    # Buttons: Up, Up, Left, Left, Left
    mgba.press_buttons(["Up", "Up", "Left", "Left", "Left"])
    time.sleep(1)
    
    pos = mgba.get_coordinates()
    print(f"Position after path and spin: {pos}")
    
    # Let's take a screenshot to verify where we are
    mgba.take_screenshot()

if __name__ == '__main__':
    main()
