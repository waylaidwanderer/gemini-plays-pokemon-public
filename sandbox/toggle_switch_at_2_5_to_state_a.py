import mgba
import time

def main():
    # Currently at "Got away safely!" text box on (3, 5).
    # Clear the text box
    print("Clearing 'Got away safely!' text...")
    mgba.press_buttons(["B"])
    time.sleep(1.0)
    
    # Face Left toward the switch at (2, 5)
    print("Turning Left...")
    mgba.press_buttons(["Left"])
    time.sleep(0.8)
    
    # Interact with the switch
    print("Interacting with Mewtwo switch at (2, 5)...")
    mgba.press_buttons(["A"])
    time.sleep(0.6)
    mgba.press_buttons(["A"])
    time.sleep(0.6)
    mgba.press_buttons(["A"])
    time.sleep(0.6)
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    
    # Clear any residual dialogs
    mgba.press_buttons(["B"])
    time.sleep(0.6)
    
    # Take screenshot
    scr = mgba.take_screenshot()
    print("Mewtwo switch toggled! Screenshot saved to:", scr)
    print("Current coordinates:", mgba.get_coordinates())

if __name__ == "__main__":
    main()
