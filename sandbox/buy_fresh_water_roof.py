import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def test_row2():
    print("Starting at:", get_pos())
    # 1. Walk Down to (8, 2)
    press_and_wait("Down")
    print("At:", get_pos())
    
    # 2. Face UP
    press_and_wait("Up")
    time.sleep(0.1)
    print(f"Testing standing at {get_pos()} facing UP...")
    
    # 3. Press A
    press_and_wait("A", 1.0)
    
    # Take screenshot
    scr = mgba.take_screenshot()
    print("Screenshot:", scr)
    
    # Press B to close if menu opens
    press_and_wait("B", 0.5)

test_row2()
