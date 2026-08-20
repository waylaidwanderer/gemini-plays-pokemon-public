import mgba
import time

def move_to_statue_front():
    print("Navigating to front of Mewtwo statue from (3, 10)...")
    # Current position: (3, 10)
    
    # 1. Walk Down to (3, 11)
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
    print("Position:", mgba.get_coordinates())
    
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
    
    # 5. Press A to interact with the switch
    print("Pressing A to interact with Mewtwo statue switch...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    mgba.take_screenshot()

move_to_statue_front()
