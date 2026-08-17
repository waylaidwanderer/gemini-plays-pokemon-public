import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def try_exit_col16():
    print("Starting from:", get_pos())
    # We are currently at (9, 7)
    
    # 1. Walk UP 2 steps to Row 5 (9, 5)
    press_and_wait("Up")
    press_and_wait("Up")
    print("At Row 5:", get_pos())
    
    # 2. Walk Right 6 steps to Column 15 (15, 5)
    for _ in range(6):
        press_and_wait("Right")
    print("At Column 15:", get_pos())
    
    # 3. Walk Down 2 steps to Row 7 (15, 7)
    press_and_wait("Down")
    press_and_wait("Down")
    print("At (15, 7):", get_pos())
    
    # Take screenshot of the right side to inspect Column 16
    mgba.take_screenshot()
    
    # 4. Walk Right 1 step to Column 16 (16, 7)
    print("Stepping onto Column 16...")
    press_and_wait("Right", 1.0) # Wait for potential map transition
    
    # Verify outside
    final_x, final_y = get_pos()
    print("Final position:", (final_x, final_y))
    if final_y > 7 or final_x == 10:
        print("SUCCESS! Successfully exited the Department Store!")
        mgba.take_screenshot()
        return True
    else:
        print("FAILED to exit. We are at:", (final_x, final_y))
        # If we didn't warp, let's try walking DOWN from (16, 7) or (15, 7)
        print("Trying to walk DOWN from:", get_pos())
        press_and_wait("Down", 1.0)
        final_x2, final_y2 = get_pos()
        print("Final position after DOWN:", (final_x2, final_y2))
        if final_y2 > 7 or final_x2 == 10:
            print("SUCCESS! Successfully exited the Department Store via DOWN!")
            mgba.take_screenshot()
            return True
            
    print("Failed to exit.")
    return False

try_exit_col16()
