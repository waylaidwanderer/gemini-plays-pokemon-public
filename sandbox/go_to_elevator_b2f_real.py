import time
import mgba

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Current pos: {pos}")

if pos['x'] == 23 and pos['y'] == 11:
    # Walk Right 5 steps to (28, 11)
    for _ in range(5):
        pos = move(['Right'])
        
    # Walk Down 3 steps to (28, 14)
    for _ in range(3):
        pos = move(['Down'])
        
    # Walk Left 4 steps to (24, 14)
    for _ in range(4):
        pos = move(['Left'])
        
    # Turn UP
    print("Turning UP...")
    mgba.press_buttons(['Up'])
    time.sleep(0.3)
    
    # Take screenshot before pressing A
    mgba.take_screenshot()
    
    # Press A to use Lift Key
    print("Pressing A to use Lift Key...")
    mgba.press_buttons(['A'])
    time.sleep(1.0)
    mgba.take_screenshot()
    
    # Walk UP into elevator
    print("Walking UP into elevator...")
    pos = move(['Up'])
    time.sleep(2.0)
    print(f"New position: {mgba.get_coordinates()}")

mgba.take_screenshot()
