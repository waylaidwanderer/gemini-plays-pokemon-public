import time
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import bridge
import mgba

def main():
    print("Opening START menu...")
    bridge.press_buttons(["Start", "sleep 500"])
    
    print("Navigating to ITEM...")
    # Cursor is at pokedex, ITEM is down 2
    bridge.press_buttons(["Down", "sleep 200", "Down", "sleep 200", "A", "sleep 800"])
    
    # Take screenshot of the Bag
    print("Capturing screenshot of the BAG...")
    img = mgba.take_screenshot()
    print(f"BAG_SCREENSHOT: {img}")
    
    # Close BAG and START menu safely
    print("Closing BAG and menu...")
    bridge.press_buttons(["B", "sleep 400", "B", "sleep 400"])

if __name__ == "__main__":
    main()
