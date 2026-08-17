import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def walk_to_vending_machine():
    print("Starting walk from:", get_pos())
    # Walk DOWN 2 steps from (9, 3) to (9, 5)
    press_and_wait("Down")
    press_and_wait("Down")
    print("At:", get_pos())
    
    # Walk RIGHT 4 steps from (9, 5) to (13, 5)
    for _ in range(4):
        press_and_wait("Right")
    print("At:", get_pos())
    
    # Walk UP 3 steps from (13, 5) to (13, 2)
    for _ in range(3):
        press_and_wait("Up")
    print("At:", get_pos())
    
    # Walk RIGHT 1 step from (13, 2) to (14, 2)
    press_and_wait("Right")
    print("At:", get_pos())
    
    # Face UP
    press_and_wait("Up")
    print("Facing UP at:", get_pos())
    
    # Interact with the vending machine
    print("Pressing A to open vending machine...")
    press_and_wait("A", 1.0)
    
    # Take screenshot of the screen to verify if menu is open
    mgba.take_screenshot()

walk_to_vending_machine()
