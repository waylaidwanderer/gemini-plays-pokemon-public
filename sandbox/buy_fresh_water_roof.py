import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def buy_vending_roof():
    print("Starting on Roof at:", get_pos())
    # We are currently at (15, 3)
    # Walk Left 9 steps to (6, 3)
    for _ in range(9):
        press_and_wait("Left")
    print("At:", get_pos())
    
    # Walk UP 1 step to (6, 2)
    press_and_wait("Up")
    print("At:", get_pos())
    
    # Press A to open the vending machine menu
    print("Pressing A...")
    press_and_wait("A", 1.0)
    
    # Select Option 1 (Fresh Water)
    print("Selecting Fresh Water (Option 1)...")
    press_and_wait("A", 0.5)
    # Dialogue: "A can of FRESH WATER popped out!"
    print("Confirming dialogue 1...")
    press_and_wait("A", 1.0)
    print("Confirming dialogue 2...")
    press_and_wait("A", 1.0)
    
    # Interacting again to buy Soda Pop
    print("Interacting again...")
    press_and_wait("A", 1.0)
    print("Selecting Soda Pop (Option 2)...")
    press_and_wait("Down", 0.3)
    press_and_wait("A", 0.5)
    print("Confirming Soda Pop dialogue...")
    press_and_wait("A", 1.0)
    press_and_wait("A", 1.0)
    
    # Exit
    print("Exiting...")
    press_and_wait("B", 0.5)
    
    # Take screenshot of final state
    mgba.take_screenshot()
    print("Fresh Water and Soda Pop purchased successfully!")

buy_vending_roof()
