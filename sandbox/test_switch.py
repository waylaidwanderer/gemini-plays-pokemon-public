import mgba
import time

def main():
    pos = mgba.get_coordinates()
    print(f"test_switch: Start coordinates: {pos}")
    
    # We are at (1, 10)
    # Walk Down to (1, 11)
    if pos['x'] == 1 and pos['y'] == 10:
        mgba.press_buttons(["Down"])
        time.sleep(0.4)
        
    # Face Right
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
    
    # Press A to interact with switch at (2, 11)
    print("Pressing A (1)...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    screenshot = mgba.take_screenshot()
    print("Screenshot saved.")
    
if __name__ == "__main__":
    main()
