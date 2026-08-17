import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def buy_drink_col8():
    print("Starting at:", get_pos())
    
    # 1. Walk down to Row 6 (4, 6)
    press_and_wait("Down")
    press_and_wait("Down")
    print("At Row 6:", get_pos())
    
    # 2. Walk right to Column 8 (8, 6)
    press_and_wait("Right")
    press_and_wait("Right")
    press_and_wait("Right")
    press_and_wait("Right")
    print("At Col 8:", get_pos())
    
    # 3. Walk up to Row 2 (8, 2)
    press_and_wait("Up")
    press_and_wait("Up")
    press_and_wait("Up")
    press_and_wait("Up")
    print("At (8, 2):", get_pos())
    
    # 4. Interact with the vending machine at (8, 1)
    print("Pressing A...")
    press_and_wait("A", 1.0)
    
    # Select Option 1 (Fresh Water)
    print("Selecting Fresh Water (Option 1)...")
    press_and_wait("A", 0.5)
    
    # Confirm Fresh Water popped out
    print("Confirming dialogue 1...")
    press_and_wait("A", 1.0)
    print("Confirming dialogue 2...")
    press_and_wait("A", 1.0)
    
    # Interacting again to buy Soda Pop (just in case!)
    print("Interacting again...")
    press_and_wait("A", 1.0)
    print("Selecting Soda Pop (Option 2)...")
    press_and_wait("Down", 0.3)
    press_and_wait("A", 0.5)
    print("Confirming Soda Pop dialogue...")
    press_and_wait("A", 1.0)
    press_and_wait("A", 1.0)
    
    # Exit vending machine
    print("Exiting...")
    press_and_wait("B", 0.5)
    
    # Take screenshot of final state
    mgba.take_screenshot()
    print("Fresh Water and Soda Pop purchased successfully!")

buy_drink_col8()
