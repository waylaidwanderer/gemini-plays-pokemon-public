import mgba
import time
from PIL import Image

if __name__ == "__main__":
    # We are currently at (3, 6). Step Left to (2, 6)
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
    
    pos = mgba.get_coordinates()
    print(f"Position at start: {pos}")
    if pos == {'x': 2, 'y': 6}:
        # Face UP
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        
        # Step 1: Interact
        print("Pressing A (1) to interact...")
        mgba.press_buttons(["A"])
        time.sleep(2.0)
        
        # Step 2: Show prompt
        print("Pressing A (2) to show prompt...")
        mgba.press_buttons(["A"])
        time.sleep(2.0)
        
        # Step 3: Select YES
        print("Pressing A (3) to select YES...")
        mgba.press_buttons(["A"])
        time.sleep(2.0)
        
        # Step 4: Close dialogue
        print("Pressing A (4) to close dialogue...")
        mgba.press_buttons(["A"])
        time.sleep(2.0)
        
        # Let's test stepping Right
        print("Testing stepping Right...")
        mgba.press_buttons(["Right"])
        time.sleep(0.5)
        
        pos_after = mgba.get_coordinates()
        print(f"Position after stepping Right: {pos_after}")
        if pos_after == {'x': 2, 'y': 6}:
            print("STATE A STRICTLY VERIFIED SUCCESSFUL!!!")
        else:
            print("STILL IN STATE B.")
