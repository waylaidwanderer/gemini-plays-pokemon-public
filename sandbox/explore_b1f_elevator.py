import time
import mgba

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting B1F elevator exploration from {pos}")

if pos['x'] == 23 and pos['y'] == 14:
    # Walk Down to Row 15
    pos = move(['Down'])
    
    # Walk Right to Column 24
    pos = move(['Right'])
    
    # Walk Right to Column 25
    pos = move(['Right'])
    
    # Let's see if we can walk Down to Row 16 from Column 25
    print("Testing if (25, 16) is walkable...")
    pos = move(['Down'])
    
    if pos['y'] == 15:
        # If blocked at (25, 16), walk Left to Column 24
        print("Blocked at (25, 16), walking Left to (24, 15)...")
        pos = move(['Left'])
        # Test if we can walk Down to Row 16 from Column 24
        print("Testing if (24, 16) is walkable...")
        pos = move(['Down'])
    
    if pos['y'] == 16:
        # If we succeeded in walking Down to Row 16, let's keep walking Down to see how far we can go!
        print("Row 16 is walkable! Walking Down further...")
        for _ in range(5):
            pos = move(['Down'])
            if pos['y'] == 19:
                print("We reached Row 19!")

mgba.take_screenshot()
