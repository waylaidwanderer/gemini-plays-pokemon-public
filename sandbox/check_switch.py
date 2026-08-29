import mgba
import time
from PIL import Image

if __name__ == "__main__":
    # We are at (3, 6). Step Left to (2, 6)
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
    
    pos = mgba.get_coordinates()
    print(f"Starting at: {pos}")
    if pos == {'x': 2, 'y': 6}:
        # Face UP
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        
        # Take pre-toggle screenshot
        img1_path = mgba.take_screenshot()
        print(f"Pre-toggle screenshot: {img1_path}")
        
        # We know we are currently looking at the overworld.
        # Press A once to open the switch text box: "A secret switch! Press it?"
        mgba.press_buttons(["A"])
        time.sleep(2.5)
        
        # Press A again to select YES on the prompt: "Who wouldn't?" appears
        mgba.press_buttons(["A"])
        time.sleep(2.5)
        
        # Press A a third time to close the "Who wouldn't?" text box
        mgba.press_buttons(["A"])
        time.sleep(2.5)
        
        # Take post-toggle screenshot
        img2_path = mgba.take_screenshot()
        print(f"Post-toggle screenshot: {img2_path}")
        
        # Copy to fixed names for easy inspection
        img1 = Image.open(img1_path)
        img1.save("state_current.png")
        img2 = Image.open(img2_path)
        img2.save("state_toggled.png")
        print("Screenshots saved to state_current.png and state_toggled.png")
        
        # Let's test stepping Right
        mgba.press_buttons(["Right"])
        time.sleep(0.5)
        print(f"Position after toggle and stepping Right: {mgba.get_coordinates()}")
