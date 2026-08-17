import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def walk_to_east_roof():
    print("Starting from:", get_pos())
    # 1. Walk to (11, 3)
    # We are at (8, 2)
    press_and_wait("Down") # (8, 3)
    press_and_wait("Right") # (9, 3)
    press_and_wait("Right") # (10, 3)
    press_and_wait("Right") # (11, 3)
    print("At (11, 3):", get_pos())
    
    # 2. Walk down to Row 6 (11, 6)
    for _ in range(3):
        press_and_wait("Down")
    print("At (11, 6):", get_pos())
    
    # 3. Walk right to Column 18 (18, 6)
    for _ in range(7):
        press_and_wait("Right")
    print("At (18, 6):", get_pos())
    
    # 4. Walk up to Row 3 (18, 3)
    for _ in range(3):
        press_and_wait("Up")
    print("At (18, 3):", get_pos())
    
    # Take screenshot of the right side
    mgba.take_screenshot()

walk_to_east_roof()
