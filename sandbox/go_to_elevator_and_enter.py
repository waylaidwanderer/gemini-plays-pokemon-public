import time
import mgba

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Current position: {pos}")

if pos['x'] == 21 and pos['y'] == 9:
    print("Navigating to elevator entrance at (24, 14)...")
    # Down 5 steps (to Row 14)
    for _ in range(5):
        pos = move(['Down'])
    # Right 3 steps (to Column 24)
    for _ in range(3):
        pos = move(['Right'])
    
    # Face UP
    print("Turning UP...")
    mgba.press_buttons(['Up'])
    time.sleep(0.3)
    
    # Press A to open the elevator door using the Lift Key
    print("Pressing A to interact with elevator...")
    mgba.press_buttons(['A'])
    time.sleep(1.0)
    
    # Walk UP into the elevator
    print("Walking UP into the elevator...")
    pos = move(['Up'])
    time.sleep(2.0)
    
    print(f"Coordinates inside elevator: {mgba.get_coordinates()}")

mgba.take_screenshot()
