import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def go_to_roof():
    print("Starting on 2F at:", get_pos())
    
    # 2F -> 3F (UP stairs at 16, 1)
    print("Moving 2F -> 3F...")
    press_and_wait("Right")
    press_and_wait("Right")
    press_and_wait("Up", 1.0)
    print("Now at:", get_pos())
    
    # 3F -> 4F (UP stairs at 12, 1)
    print("Moving 3F -> 4F...")
    press_and_wait("Left")
    press_and_wait("Left")
    press_and_wait("Left")
    press_and_wait("Left")
    press_and_wait("Up", 1.0)
    print("Now at:", get_pos())
    
    # 4F -> 5F (UP stairs at 16, 1)
    print("Moving 4F -> 5F...")
    press_and_wait("Right")
    press_and_wait("Right")
    press_and_wait("Right")
    press_and_wait("Right")
    press_and_wait("Up", 1.0)
    print("Now at:", get_pos())
    
    # 5F -> Roof (UP stairs at 12, 1)
    print("Moving 5F -> Roof...")
    press_and_wait("Left")
    press_and_wait("Left")
    press_and_wait("Left")
    press_and_wait("Left")
    press_and_wait("Up", 1.0)
    print("Now at:", get_pos())
    
    # Take screenshot of Roof landing
    mgba.take_screenshot()
    print("Arrived on Roof! Final position:", get_pos())

go_to_roof()
