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
    
    # 1. Walk down to Row 6 (2, 6)
    for _ in range(4):
        press_and_wait("Down")
    print("At Row 6:", get_pos())
    
    # 2. Walk right to Column 8 (8, 6)
    for _ in range(6):
        press_and_wait("Right")
    print("At Col 8:", get_pos())
    
    # 3. Walk up to Row 2 (8, 2)
    for _ in range(4):
        press_and_wait("Up")
    print("At (8, 2):", get_pos())
    
    # 4. Interact with the vending machine at (8, 1)
    print("Pressing A...")
    press_and_wait("A", 1.0)
    
    # Take screenshot of the vending machine menu
    mgba.take_screenshot()

buy_drink_col8()
