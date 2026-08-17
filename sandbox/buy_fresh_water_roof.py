import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def find_vending_machine():
    print("Starting search from:", get_pos())
    
    # 1. Walk right to Column 11 (11, 6)
    press_and_wait("Right")
    press_and_wait("Right")
    press_and_wait("Right")
    print("At (11, 6):", get_pos())
    
    # 2. Walk up to Row 2 (11, 2)
    for _ in range(4):
        press_and_wait("Up")
    print("At (11, 2):", get_pos())
    
    # 3. Walk left along Row 2 and try interacting UP with columns 10, 9, 8, 7
    # We will try columns 10, 9, 8, 7
    for target_col in [10, 9, 8, 7]:
        cx, cy = get_pos()
        # Walk left to target_col
        steps = cx - target_col
        for _ in range(steps):
            press_and_wait("Left")
        
        # Face UP
        press_and_wait("Up")
        time.sleep(0.1)
        cx, cy = get_pos()
        print(f"Testing Column {cx} on Row 1 (standing at {cx}, {cy} facing UP)...")
        
        # Press A
        press_and_wait("A", 0.6)
        
        # Take a screenshot to inspect later
        scr = mgba.take_screenshot()
        print(f"Screenshot for col {cx}: {scr}")
        
        # Press B to close any potential dialog just in case
        press_and_wait("B", 0.3)

find_vending_machine()
