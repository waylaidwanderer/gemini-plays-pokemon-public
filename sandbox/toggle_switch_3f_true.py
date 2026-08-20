import mgba
import time

def main():
    print("Testing statues at (3, 12) and (3, 10) with proper Gen 1 timing...")
    
    # Current position is (2, 11).
    # 1. Walk Down to (2, 12)
    print("Moving Down to (2, 12)...")
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    
    pos = mgba.get_coordinates()
    print("Coordinates:", pos)
    
    if pos == {'x': 2, 'y': 12}:
        # Face Right towards (3, 12) with Gen 1 sleep
        print("Facing Right towards (3, 12)...")
        mgba.press_buttons(["Right", "sleep 250", "A"])
        time.sleep(1.0)
        
        # Take a screenshot to check if dialogue opened
        print("Taking screenshot of (3, 12) attempt...")
        mgba.take_screenshot()
        
        # Press A again in case dialogue opened (to press the switch)
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        
    # 2. Walk to (2, 10)
    print("Moving Up to (2, 10)...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    pos = mgba.get_coordinates()
    print("Coordinates:", pos)
    
    if pos == {'x': 2, 'y': 10}:
        # Face Right towards (3, 10) with Gen 1 sleep
        print("Facing Right towards (3, 10)...")
        mgba.press_buttons(["Right", "sleep 250", "A"])
        time.sleep(1.0)
        
        # Take a screenshot to check if dialogue opened
        print("Taking screenshot of (3, 10) attempt...")
        mgba.take_screenshot()
        
        # Press A again in case dialogue opened
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        
        mgba.take_screenshot()

if __name__ == "__main__":
    main()
