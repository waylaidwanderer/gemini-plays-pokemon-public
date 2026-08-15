import time
import sys
import bridge
import mgba

sys.stdout.reconfigure(encoding='utf-8')

def main():
    print("Opening Bag and scrolling one by one...")
    # Close any menus
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 300"])
        
    # Open Start menu
    bridge.press_buttons(["Start", "sleep 500"])
    
    # Align to POKÉDEX
    for _ in range(6):
        bridge.press_buttons(["Up", "sleep 150"])
        
    # Select ITEM (Down, Down, A)
    bridge.press_buttons(["Down", "sleep 250", "Down", "sleep 250", "A", "sleep 1000"])
    
    # Take screenshot of Page 1
    p1 = mgba.take_screenshot()
    print(f"Page 1: {p1}")
    
    # Scroll down 10 times, taking a screenshot each time to see scrolling behavior
    for i in range(10):
        bridge.press_buttons(["Down", "sleep 350"])
        p = mgba.take_screenshot()
        print(f"Scroll {i+1}: {p}")
        
    # Close Bag and menu
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 300"])

if __name__ == "__main__":
    main()
