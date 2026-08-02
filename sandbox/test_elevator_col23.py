import time
import mgba

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting test from {pos}")

if pos['x'] == 24 and pos['y'] == 14:
    # Walk Left to (23, 14)
    pos = move(['Left'])
    
    # Face UP
    print("Turning UP...")
    mgba.press_buttons(['Up'])
    time.sleep(0.3)
    
    # Take a screenshot before pressing A
    mgba.take_screenshot()
    
    # Press A to interact with elevator
    print("Pressing A to interact...")
    mgba.press_buttons(['A'])
    time.sleep(1.0)
    mgba.take_screenshot()
    
    # Dismiss any text box
    print("Pressing B to dismiss any text...")
    mgba.press_buttons(['B'])
    time.sleep(0.5)
    
    # Try walking UP into the elevator
    print("Trying to walk UP into the elevator...")
    pos = move(['Up'])
    time.sleep(1.0)
    mgba.take_screenshot()

print(f"Final pos: {mgba.get_coordinates()}")
