import mgba
import time

def toggle_switch_2f():
    print("Navigating to front of Mewtwo statue at (2, 12) to toggle back to State A...")
    # Current position: (5, 11)
    
    # 1. Walk Left to (4, 11)
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
    print("Position:", mgba.get_coordinates())
    
    # 2. Walk Left to (3, 11)
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
    print("Position:", mgba.get_coordinates())
    
    # 3. Walk Down to (3, 12)
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
    print("Position:", mgba.get_coordinates())
    
    # 4. Walk Left to (2, 12)
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
    print("Position:", mgba.get_coordinates())
    
    # 5. Press Up to face Up and bump into statue at (2, 11)
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    print("Position:", mgba.get_coordinates())
    
    # 6. Press A to interact with the switch
    print("Pressing A to trigger the switch textbox...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    mgba.take_screenshot()

toggle_switch_2f()
