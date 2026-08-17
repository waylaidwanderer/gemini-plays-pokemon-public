import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def walk_to_vending_left():
    print("Starting position:", get_pos())
    # Walk Right 4 steps to (11, 3)
    for _ in range(4):
        press_and_wait("Right")
    print("At (11, 3):", get_pos())
    
    # Walk Down 3 steps to (11, 6)
    for _ in range(3):
        press_and_wait("Down")
    print("At (11, 6):", get_pos())
    
    # Walk Left 10 steps to (1, 6)
    for _ in range(10):
        press_and_wait("Left")
    print("At (1, 6):", get_pos())
    
    # Walk Up 4 steps to (1, 2)
    for _ in range(4):
        press_and_wait("Up")
    print("At (1, 2):", get_pos())
    
    # Take screenshot of the top-left area
    mgba.take_screenshot()

walk_to_vending_left()
