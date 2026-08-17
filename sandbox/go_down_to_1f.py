import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def step_by_step_descend():
    print("Current position:", get_pos())
    # 1. Close text box
    print("Closing text box...")
    press_and_wait("B", 0.5)
    
    # 2. Walk Right 2 steps to (16, 2)
    print("Walking to (16, 2)...")
    press_and_wait("Right")
    press_and_wait("Right")
    print("At (16, 2):", get_pos())
    
    # 3. Press UP to take DOWN escalator
    print("Pressing UP to go to 4F...")
    press_and_wait("Up", 1.0)
    time.sleep(0.5)
    print("After warp, position is:", get_pos())
    
    # Take screenshot to inspect visually
    mgba.take_screenshot()

step_by_step_descend()
