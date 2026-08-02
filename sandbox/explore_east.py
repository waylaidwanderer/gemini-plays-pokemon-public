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
    # Walk Right to (9, 11)
    pos = move(['Right'])
    # Walk Right to (10, 11)
    pos = move(['Right'])
    
    # Take screenshot at (10, 11) to see what is to our right!
    print("Taking screenshot at (10, 11) to inspect right side...")
    mgba.take_screenshot()
    
    # Try to walk Right
    print("Testing if (11, 11) is walkable...")
    test_pos = move(['Right'])
    if test_pos['x'] == 10:
        print("Blocked going Right! Testing Up/Down from (10, 11)...")
        # Try Up
        test_up = move(['Up'])
        if test_up['y'] == 10:
            print("Up is walkable, now at:", test_up)
            # Take screenshot
            mgba.take_screenshot()
            # Return Down
            move(['Down'])
        else:
            print("Up is blocked")
            
        # Try Down
        test_down = move(['Down'])
        if test_down['y'] == 12:
            print("Down is walkable, now at:", test_down)
            mgba.take_screenshot()
            # Return Up
            move(['Up'])
        else:
            print("Down is blocked")
            
mgba.take_screenshot()
