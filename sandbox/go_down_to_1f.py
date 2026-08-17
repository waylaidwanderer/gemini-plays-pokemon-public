import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def read_sign_at_14_2():
    print("Starting from:", get_pos())
    # We are at (15, 7)
    
    # 1. Walk UP Column 15 to Row 2 (15, 2)
    for _ in range(5):
        press_and_wait("Up")
    print("At:", get_pos())
    
    # 2. Walk Left to Column 14 (14, 2)
    press_and_wait("Left")
    print("At (14, 2):", get_pos())
    
    # 3. Face UP
    press_and_wait("Up")
    time.sleep(0.1)
    
    # 4. Press A to read the sign
    print("Pressing A...")
    press_and_wait("A", 1.0)
    
    # Take screenshot of the text box
    mgba.take_screenshot()
    
    # Close text box
    press_and_wait("B", 0.5)
    press_and_wait("B", 0.5)

read_sign_at_14_2()
