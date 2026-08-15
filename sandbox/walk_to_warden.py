import mgba
import time

def main():
    # Start at (19, 28)
    print("Starting walk to Warden's House...")
    
    # Path: 
    # Down, Down to (19, 30)
    # Right x 11 to (30, 30)
    # Up x 2 to (30, 28)
    # Left x 3 to (27, 28)
    # Up to enter door at (27, 27)
    
    buttons = ["Down", "Down"] + ["Right"] * 11 + ["Up", "Up"] + ["Left"] * 3 + ["Up"]
    
    mgba.press_buttons(buttons)
    time.sleep(2) # Wait for execution and transition
    
    coords = mgba.get_coordinates()
    print(f"Current coordinates after entering house: {coords}")
    
    screenshot = mgba.take_screenshot()
    print(f"Screenshot taken: {screenshot}")

if __name__ == "__main__":
    main()
