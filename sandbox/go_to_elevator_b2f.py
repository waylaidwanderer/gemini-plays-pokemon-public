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

if pos['x'] == 23 and pos['y'] == 7:
    # Walk Right 2 steps to (25, 7)
    pos = move(['Right'])
    pos = move(['Right'])
    
    # Walk Down 7 steps to (25, 14)
    for _ in range(7):
        pos = move(['Down'])
        
    # Walk Left 1 step to (24, 14)
    pos = move(['Left'])
    
    # Face UP
    print("Turning UP...")
    mgba.press_buttons(['Up'])
    time.sleep(0.3)
    
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
