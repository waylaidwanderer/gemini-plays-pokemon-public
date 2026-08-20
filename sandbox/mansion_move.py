import mgba
import time

def complete_toggle():
    print("Dismissing battle and navigating to front of Mewtwo statue to toggle...")
    # Currently we are at (3, 11) on 2F in the 'Got away safely!' screen.
    
    # 1. Dismiss battle text
    mgba.press_buttons(["A"])
    time.sleep(0.6)
    
    # 2. Walk Down to (3, 12)
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
    print("Position:", mgba.get_coordinates())
    
    # 3. Walk Left to (2, 12)
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
    print("Position:", mgba.get_coordinates())
    
    # 4. Press Up to face Up and bump into statue at (2, 11)
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    print("Position:", mgba.get_coordinates())
    
    # 5. Press A to interact with switch
    print("Pressing A to trigger switch dialogue...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    mgba.take_screenshot()

complete_toggle()
