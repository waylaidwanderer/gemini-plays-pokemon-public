import time
import sys
import bridge
import mgba

sys.stdout.reconfigure(encoding='utf-8')

def main():
    print("Opening Bag and scrolling all the way to the bottom...")
    # Close any menus
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 300"])
        
    # Open Start menu
    bridge.press_buttons(["Start", "sleep 500"])
    
    # Align to POKÉDEX
    for _ in range(6):
        bridge.press_buttons(["Up", "sleep 200"])
        
    # Select ITEM
    bridge.press_buttons(["Down", "sleep 250", "Down", "sleep 250", "A", "sleep 1000"])
    
    # We are in the Bag. Let's take a screenshot of the top page.
    img1 = mgba.take_screenshot()
    print(f"Bag Page 1: {img1}")
    
    # Scroll down 4 times (which should scroll by 4 items)
    for _ in range(4):
        bridge.press_buttons(["Down", "sleep 250"])
    time.sleep(0.5)
    img2 = mgba.take_screenshot()
    print(f"Bag Page 2: {img2}")
    
    # Scroll down 4 more times
    for _ in range(4):
        bridge.press_buttons(["Down", "sleep 250"])
    time.sleep(0.5)
    img3 = mgba.take_screenshot()
    print(f"Bag Page 3: {img3}")
    
    # Close Bag and menu
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 300"])

if __name__ == "__main__":
    main()
