import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def exit_via_col8_row2():
    print("Starting on 1F at:", get_pos())
    
    # 1. Walk UP to Row 2 (11, 2)
    for _ in range(3):
        press_and_wait("Up")
    print("At Row 2:", get_pos())
    
    # 2. Walk Left to Column 8 (8, 2)
    for _ in range(3):
        press_and_wait("Left")
    print("At Column 8:", get_pos())
    
    # 3. Walk Down 5 steps to Row 7 (8, 7)
    for _ in range(5):
        press_and_wait("Down")
    print("At Row 7:", get_pos())
    
    # 4. Walk Down 1 more step to exit the store
    print("Exiting store...")
    press_and_wait("Down")
    time.sleep(1.0) # Wait for map transition
    
    print("Outside in Celadon City! Position:", get_pos())
    mgba.take_screenshot()

exit_via_col8_row2()
