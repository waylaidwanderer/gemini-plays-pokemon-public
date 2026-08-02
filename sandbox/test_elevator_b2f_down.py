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

if pos['x'] == 24 and pos['y'] == 14:
    # Walk Down to (24, 15)
    pos = move(['Down'])
    
    # Face Down is already set because we walked Down
    # Press A to use Lift Key
    print("Pressing A to open elevator...")
    mgba.press_buttons(['A'])
    time.sleep(1.0)
    mgba.take_screenshot()
    
    # Walk Down into elevator
    print("Walking Down into elevator...")
    pos = move(['Down'])
    time.sleep(2.0)
    print(f"New position: {mgba.get_coordinates()}")

mgba.take_screenshot()
