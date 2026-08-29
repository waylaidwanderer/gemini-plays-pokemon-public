import mgba
import time
from PIL import Image

def main():
    pos = mgba.get_coordinates()
    print(f"test_switch: Start coordinates: {pos}")
    
    # We are at (1, 10)
    # Walk Down to (1, 12)
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
    
    # Walk Right to (2, 12)
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
    
    pos = mgba.get_coordinates()
    print(f"Standing at: {pos}")
    
    # Face UP
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    
    # Press A to interact with Mewtwo statue at (2, 11)
    print("Pressing A (1)...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    screenshot = mgba.take_screenshot()
    print("Screenshot saved.")
    
if __name__ == "__main__":
    main()
