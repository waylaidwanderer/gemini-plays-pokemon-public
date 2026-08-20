import mgba
import time

def main():
    print("Currently at (2, 13). Moving Up to (2, 12)...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    pos = mgba.get_coordinates()
    print("Coordinates after moving Up:", pos)
    
    if pos == {'x': 2, 'y': 12}:
        # Press Up to face Up and press A
        print("Facing Up towards (2, 11) and interacting with switch...")
        mgba.press_buttons(["Up", "A"])
        time.sleep(1.0)
        
        # Take screenshot to see if dialogue box popped up
        mgba.take_screenshot()
        
        # Let's dismiss the text box and select YES (default)
        print("Pressing A to select Yes on switch...")
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        
        mgba.take_screenshot()
        print("Done!")
    else:
        print("Failed to reach (2, 12)!")
        mgba.take_screenshot()

if __name__ == "__main__":
    main()
