import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def buy_fresh_water():
    print("Navigating to the Fresh Water vending machine on the roof...")
    # Stand at (9, 3)
    press_and_wait("Down")
    pos = mgba.get_coordinates()
    print(f"At: ({pos['x']}, {pos['y']})")
    
    # Walk left 3 steps to Column 6
    for _ in range(3):
        press_and_wait("Left")
    pos = mgba.get_coordinates()
    print(f"At: ({pos['x']}, {pos['y']})")
    
    # Walk UP to Row 2
    press_and_wait("Up")
    pos = mgba.get_coordinates()
    print(f"At: ({pos['x']}, {pos['y']})")
    
    # Press A to open the vending machine menu
    print("Pressing A...")
    press_and_wait("A", 0.6)
    
    mgba.take_screenshot()

buy_fresh_water()
