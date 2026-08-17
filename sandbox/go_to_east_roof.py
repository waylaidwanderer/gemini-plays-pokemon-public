import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def go_to_east_roof():
    print("Starting position:", get_pos())
    
    # 1. Walk down to Row 6 (4, 6)
    press_and_wait("Down")
    press_and_wait("Down")
    press_and_wait("Down")
    press_and_wait("Down")
    print("At Row 6:", get_pos())
    
    # 2. Walk right along Row 6 to Column 18 (18, 6)
    for _ in range(14):
        press_and_wait("Right")
    print("At Column 18:", get_pos())
    
    # 3. Walk up to Row 3 (18, 3)
    for _ in range(3):
        press_and_wait("Up")
    print("At (18, 3):", get_pos())
    
    # Take screenshot of the right side
    mgba.take_screenshot()

go_to_east_roof()
