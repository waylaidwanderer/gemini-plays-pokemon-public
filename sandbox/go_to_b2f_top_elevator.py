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

if pos['x'] == 27 and pos['y'] == 8:
    # Walk Up to (27, 7)
    pos = move(['Up'])
    # Walk Left 4 steps to (23, 7)
    for _ in range(4):
        pos = move(['Left'])
    # Walk Up 4 steps to (23, 3)
    for _ in range(4):
        pos = move(['Up'])
    # Walk Left 2 steps to (21, 3)
    for _ in range(2):
        pos = move(['Left'])
        
    # Face UP (looking at (21, 2))
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
