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
    
    # Test if Down is walkable
    print("Testing if Down from (9, 11) is walkable...")
    test_pos = move(['Down'])
    if test_pos['y'] == 12:
        print("SUCCESS! Walked Down to (9, 12)!")
        # Let's see if we can go further Down
        pos = move(['Down'])  # (9, 13)
        pos = move(['Down'])  # (9, 14)
    else:
        print("Blocked going Down from (9, 11)")

mgba.take_screenshot()
