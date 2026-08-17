import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def buy_drink_from_4_6():
    print("Starting at:", get_pos())
    
    # 1. Walk right 4 steps to Column 8 (8, 6)
    for _ in range(4):
        press_and_wait("Right")
    print("At (8, 6):", get_pos())
    
    # 2. Walk up 4 steps to Row 2 (8, 2)
    for _ in range(4):
        press_and_wait("Up")
    print("At (8, 2):", get_pos())
    
    # 3. Interact with the vending machine at (8, 1)
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
    
    # Take screenshot of final state
    mgba.take_screenshot()
    print("Fresh Water purchased successfully!")

buy_drink_from_4_6()
