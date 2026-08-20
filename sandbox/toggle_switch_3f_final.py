import mgba
import time

def main():
    print("Dismissing 'Got away safely!' text...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    pos = mgba.get_coordinates()
    print("Overworld coordinates:", pos)
    
    if pos == {'x': 1, 'y': 11}:
        print("At (1, 11). Turning Right to face (2, 11)...")
        mgba.press_buttons(["Right"])
        time.sleep(0.5) # Wait for turn animation to complete
        
        print("Pressing A to interact with (2, 11)...")
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        
        # Take a screenshot to check for the switch dialogue box
        print("Taking screenshot of interaction...")
        mgba.take_screenshot()
        
        # Press A to select YES (if dialogue opened)
        print("Pressing A to select Yes on switch...")
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        
        # Press A again to dismiss text
        print("Pressing A to dismiss text...")
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        
        # Press B to close dialogue box
        print("Pressing B to close...")
        mgba.press_buttons(["B"])
        time.sleep(1.0)
        
        # Final screenshot to confirm gate state or overworld
        mgba.take_screenshot()
        print("Done!")
    else:
        print("Unexpected overworld position!")
        mgba.take_screenshot()

if __name__ == "__main__":
    main()
