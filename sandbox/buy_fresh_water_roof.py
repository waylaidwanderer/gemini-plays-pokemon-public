import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def sweep_vending():
    # We are currently at (7, 1) facing UP.
    # We will test column 6, 5, 4 on Row 1
    
    # 1. Test Column 6
    print("Moving to Column 6...")
    press_and_wait("Left")
    press_and_wait("Up")
    time.sleep(0.1)
    print(f"Testing Column 6 (standing at {get_pos()} facing UP)...")
    press_and_wait("A", 1.0)
    # Take screenshot
    scr = mgba.take_screenshot()
    print("Screenshot at col 6:", scr)
    # If menu is open, we can try to buy Fresh Water
    # Press B just in case to close menu if open, or we can see it on next turn
    press_and_wait("B", 0.5)
    
    # 2. Test Column 5
    print("Moving to Column 5...")
    press_and_wait("Left")
    press_and_wait("Up")
    time.sleep(0.1)
    print(f"Testing Column 5 (standing at {get_pos()} facing UP)...")
    press_and_wait("A", 1.0)
    # Take screenshot
    scr = mgba.take_screenshot()
    print("Screenshot at col 5:", scr)
    press_and_wait("B", 0.5)
    
    # 3. Test Column 4
    print("Moving to Column 4...")
    press_and_wait("Left")
    press_and_wait("Up")
    time.sleep(0.1)
    print(f"Testing Column 4 (standing at {get_pos()} facing UP)...")
    press_and_wait("A", 1.0)
    # Take screenshot
    scr = mgba.take_screenshot()
    print("Screenshot at col 4:", scr)
    press_and_wait("B", 0.5)

sweep_vending()
