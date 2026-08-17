import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def exit_via_col16():
    print("Starting exit via Column 16 from:", get_pos())
    # We are currently at (8, 7)
    
    # 1. Walk Right 7 steps to Column 15 (15, 7)
    for _ in range(7):
        press_and_wait("Right")
    print("At (15, 7):", get_pos())
    
    # Take a screenshot to inspect if Column 16 is open
    mgba.take_screenshot()
    
    # 2. Walk Right 1 step to Column 16 (16, 7)
    print("Stepping onto Column 16...")
    press_and_wait("Right", 1.0)
    
    # Verify outside
    final_x, final_y = get_pos()
    print("Final position:", (final_x, final_y))
    if final_y > 7 or final_x == 10:
        print("SUCCESS! Successfully exited the Department Store!")
        mgba.take_screenshot()
        return True
    else:
        print("FAILED to exit. We are at:", (final_x, final_y))
        # If we didn't warp, let's try walking DOWN from (16, 7)
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

exit_via_col16()
