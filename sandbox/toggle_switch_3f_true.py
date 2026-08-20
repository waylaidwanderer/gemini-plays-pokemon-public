import mgba
import time

def main():
    print("Currently at (2, 13). Facing LEFT.")
    
    # 1. Turn UP in place
    print("Pressing Up to turn face UP...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    pos = mgba.get_coordinates()
    print("Position after turning UP:", pos)
    
    # 2. Step UP to (2, 12)
    print("Pressing Up to step UP to (2, 12)...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    pos = mgba.get_coordinates()
    print("Position after stepping UP:", pos)
    
    if pos == {'x': 2, 'y': 12}:
        # 3. Try stepping UP to (2, 11)
        print("Pressing Up to test if (2, 11) is walkable...")
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        
        pos_test = mgba.get_coordinates()
        print("Position after testing (2, 11):", pos_test)
        
        if pos_test == {'x': 2, 'y': 11}:
            print("(2, 11) is WALKABLE! Stepping back down to (2, 12)...")
            mgba.press_buttons(["Down"])
            time.sleep(0.5)
            # Face Up again
            mgba.press_buttons(["Up"])
            time.sleep(0.5)
        else:
            print("(2, 11) is SOLID (blocked by statue/switch)!")
            
        # 4. Stand at (2, 12) facing UP, and press A to interact with (2, 11)
        print("At (2, 12) facing UP. Pressing A to toggle switch...")
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        
        # Take a screenshot to check for switch dialogue
        print("Taking screenshot to check for switch dialogue...")
        mgba.take_screenshot()
        
        # Press A again to select Yes (if dialogue popped up)
        print("Pressing A to confirm...")
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        
        # Take a final screenshot
        mgba.take_screenshot()
        print("Done!")
    else:
        print("Failed to reach (2, 12)!")
        mgba.take_screenshot()

if __name__ == "__main__":
    main()
