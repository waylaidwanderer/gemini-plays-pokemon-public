import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def exit_store_via_col8():
    print("Starting from:", get_pos())
    
    # 1. Walk Right to (15, 7)
    press_and_wait("Right")
    print("At:", get_pos())
    
    # 2. Walk UP to (15, 5)
    press_and_wait("Up")
    press_and_wait("Up")
    print("At:", get_pos())
    
    # 3. Walk Left to (8, 5)
    for _ in range(7):
        press_and_wait("Left")
    print("At (8, 5):", get_pos())
    
    # 4. Walk Down to (8, 7)
    press_and_wait("Down")
    press_and_wait("Down")
    print("At (8, 7):", get_pos())
    
    # 5. Walk Down to exit the store
    print("Exiting store...")
    press_and_wait("Down")
    time.sleep(1.0) # Wait for map transition
    
    print("Outside in Celadon City! Position:", get_pos())
    mgba.take_screenshot()

exit_store_via_col8()
