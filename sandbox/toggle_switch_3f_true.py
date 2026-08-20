import mgba
import time

def check_dialogue():
    # Take a screenshot to check for switch dialogue
    print("Checking for dialogue...")
    mgba.take_screenshot()

def main():
    print("Currently at (2, 11).")
    
    # 1. Walk DOWN to (2, 12)
    print("Moving Down to (2, 12)...")
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    
    pos = mgba.get_coordinates()
    print("Coordinates:", pos)
    
    if pos == {'x': 2, 'y': 12}:
        # Face Right towards (3, 12)
        print("Facing Right towards (3, 12) and pressing A...")
        mgba.press_buttons(["Right", "A"])
        time.sleep(1.0)
        check_dialogue()
        
        # Press A again in case dialogue opened
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        
        pos_after = mgba.get_coordinates()
        print("Coordinates after (3, 12) attempt:", pos_after)
        
    # Let's also try (3, 10) if we are still here
    pos = mgba.get_coordinates()
    if pos['x'] == 2:
        # Move to (2, 10)
        print("Moving to (2, 10)...")
        # To go from (2, 12) to (2, 10), we need to press Up twice
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        
        pos = mgba.get_coordinates()
        print("Coordinates:", pos)
        
        if pos == {'x': 2, 'y': 10}:
            # Face Right towards (3, 10)
            print("Facing Right towards (3, 10) and pressing A...")
            mgba.press_buttons(["Right", "A"])
            time.sleep(1.0)
            check_dialogue()
            
            mgba.press_buttons(["A"])
            time.sleep(1.0)
            
            mgba.take_screenshot()

if __name__ == "__main__":
    main()
