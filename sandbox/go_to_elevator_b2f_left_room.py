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

if pos['x'] == 2 and pos['y'] == 9:
    # Walk Right to (3, 9)
    pos = move(['Right'])
    # Walk Down 2 steps to (3, 11)
    pos = move(['Down'])
    pos = move(['Down'])
    
    # Step onto (4, 11) RIGHT-pointing spinner
    print("Stepping onto RIGHT-pointing spinner...")
    pos = move(['Right'])
    print("Waiting for slide...")
    time.sleep(5.0)
    pos = mgba.get_coordinates()
    print(f"Position after slide: {pos}")
    
if pos['x'] == 8 and pos['y'] == 11:
    # Walk Right 13 steps to (21, 11)
    print("Walking Right to Column 21...")
    for _ in range(13):
        pos = move(['Right'])
        
    # Walk Up 9 steps to (21, 2) (elevator)
    print("Walking Up to Row 3...")
    for _ in range(8):
        pos = move(['Up'])
        
    # Stand at (21, 3) and face UP
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
