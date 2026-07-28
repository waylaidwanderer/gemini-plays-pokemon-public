import mgba
import time

def main():
    print("Opening bag to use Town Map...")
    # 1. Open Start Menu
    mgba.press_buttons(["Start", "sleep 500"])
    
    # 2. Go to ITEM (Down 1 step from first option)
    mgba.press_buttons(["Down", "sleep 200", "A", "sleep 600"])
    
    # 3. We are now in the bag. Let's find TOWN MAP.
    # In the bag, we can scroll down.
    # Let's take a screenshot of the bag first
    scr = mgba.take_screenshot()
    print(f"Bag Screenshot: {scr}")
    
    # Let's scroll Down and press A to see what item we select.
    # Usually TOWN MAP is near the top or bottom.
    # Let's press Down 5 times, taking screenshots, or let's search for it.
    # Let's just scroll through the bag to find it!
    for i in range(10):
        # Press A to see item options or just select.
        # But wait, if we just scroll and look at the item names in the screenshots:
        mgba.press_buttons(["Down", "sleep 200"])
        scr = mgba.take_screenshot()
        print(f"Scroll {i+1}: {scr}")
        
    # Let's exit the bag
    mgba.press_buttons(["B", "sleep 200", "B", "sleep 200", "B"])

if __name__ == "__main__":
    main()
