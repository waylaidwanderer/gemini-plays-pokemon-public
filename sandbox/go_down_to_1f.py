import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def exit_store_from_16_2():
    print("Starting on 1F at:", get_pos())
    
    # 1. Walk Left to Column 15 (15, 2)
    press_and_wait("Left")
    print("At:", get_pos())
    
    # 2. Walk Down 4 steps to Row 6 (15, 6)
    for _ in range(4):
        press_and_wait("Down")
    print("At Row 6:", get_pos())
    
    # 3. Walk Down 2 more steps to exit the store
    print("Exiting store...")
    press_and_wait("Down")
    press_and_wait("Down")
    time.sleep(1.0) # Wait for map transition to Celadon City
    
    print("Outside in Celadon City! Position:", get_pos())
    mgba.take_screenshot()

exit_store_from_16_2()
