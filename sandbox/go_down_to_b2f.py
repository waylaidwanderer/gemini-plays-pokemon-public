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

if pos['x'] == 25 and pos['y'] == 7:
    # Walk Right to (26, 7)
    pos = move(['Right'])
    # Walk Right to (27, 7)
    pos = move(['Right'])
    # Walk Down to (27, 8) to take the stairs to B2F
    pos = move(['Down'])
    
    print("Waiting for transition to B2F...")
    time.sleep(2.0)
    print(f"New position: {mgba.get_coordinates()}")

mgba.take_screenshot()
