import time
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import bridge
import mgba

sys.stdout.reconfigure(encoding='utf-8')

def main():
    print("Checking BAG contents...")
    
    # 1. Dismiss dialogue by pressing B a few times
    print("Dismissing dialogue...")
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 300"])
        
    # 2. Open START menu (cursor is on POKÉMON or OPTION)
    # Let's open the START menu and move to POKÉDEX first to reset
    bridge.press_buttons(["Start", "sleep 600"])
    
    # Press UP 7 times to wrap to POKÉDEX (1)
    for _ in range(7):
        bridge.press_buttons(["Up", "sleep 150"])
        
    # Move DOWN 2 times to ITEM (3)
    bridge.press_buttons(["Down", "sleep 200", "Down", "sleep 200"])
    
    # Open ITEM menu
    bridge.press_buttons(["A", "sleep 1000"])
    
    # Take screenshot of first page of BAG
    mgba.take_screenshot()
    print("First page of BAG captured.")
    
    # Scroll down to see more items (Gen 1 BAG holds up to 20 items, showing 3-4 at a time)
    for i in range(5):
        bridge.press_buttons(["Down", "sleep 200"])
    mgba.take_screenshot()
    print("Second page of BAG captured.")
    
    for i in range(5):
        bridge.press_buttons(["Down", "sleep 200"])
    mgba.take_screenshot()
    print("Third page of BAG captured.")
    
    # Close menu
    bridge.press_buttons(["B", "sleep 400", "Start", "sleep 400"])

if __name__ == "__main__":
    main()
