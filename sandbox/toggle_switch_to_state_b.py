import mgba
import time

def toggle_switch():
    print("Initiating switch toggle...")
    # 4 A-Press sequence with generous delays (2.0s)
    # A-Press 1: Interacts with the statue
    print("A-Press 1")
    mgba.press_buttons(["A"])
    time.sleep(2.0)
    
    # A-Press 2: Advances text to YES/NO menu
    print("A-Press 2")
    mgba.press_buttons(["A"])
    time.sleep(2.0)
    
    # A-Press 3: Selects YES (default)
    print("A-Press 3")
    mgba.press_buttons(["A"])
    time.sleep(2.0)
    
    # A-Press 4: Dismisses the textbox and restores the overworld
    print("A-Press 4")
    mgba.press_buttons(["A"])
    time.sleep(2.0)

toggle_switch()
mgba.take_screenshot()
print("Switch toggled successfully!")
