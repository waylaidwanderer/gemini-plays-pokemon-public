import time
import mgba

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting B1F elevator test from {pos}")

if pos['x'] == 19 and pos['y'] == 15:
    # Walk Right to (25, 15)
    for _ in range(6):
        pos = move(['Right'])
    
    # Face Left
    print("Turning Left...")
    mgba.press_buttons(['Left'])
    time.sleep(0.3)
    
    # Take screenshot before pressing A
    mgba.take_screenshot()
    
    # Press A to use Lift Key
    print("Pressing A to open elevator...")
    mgba.press_buttons(['A'])
    time.sleep(1.0)
    mgba.take_screenshot()
    
    # Try to walk Left into (24, 15)
    print("Trying to walk Left into the elevator...")
    pos = move(['Left'])
    time.sleep(1.0)
    mgba.take_screenshot()

print(f"Final position: {mgba.get_coordinates()}")
