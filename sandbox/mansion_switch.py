import mgba
import time

def interact_with_statue_front():
    print("Navigating to front of Mewtwo statue at (2, 12) to interact...")
    # We are currently at (3, 11).
    
    # 1. Walk Down to (3, 12)
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
    print("Position after Down:", mgba.get_coordinates())
    
    # 2. Walk Left to (2, 12)
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
    print("Position after Left:", mgba.get_coordinates())
    
    # 3. Walk Up to face Up and bump into statue at (2, 11)
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    print("Position after Up:", mgba.get_coordinates())
    
    # 4. Press A to interact
    print("Pressing A to interact with switch...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    mgba.take_screenshot()

interact_with_statue_front()
