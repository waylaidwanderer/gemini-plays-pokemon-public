import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def go_to_underground():
    print("Navigating from (23, 12) to the Underground Path Entrance Building...")
    
    # 1. Walk LEFT 11 steps to Column 12
    print("Step 1: Walking LEFT to Column 12...")
    for _ in range(11):
        press_and_wait("Left", 0.25)
        
    # 2. Walk UP 9 steps to Row 3 (the doorway)
    print("Step 2: Walking UP towards the door at (12, 3)...")
    for _ in range(9):
        press_and_wait("Up", 0.25)
        
    # 3. Take 1 more step UP to enter the building!
    print("Step 3: Entering the building...")
    press_and_wait("Up", 1.0)
    
    # Check new position
    pos = mgba.get_coordinates()
    if pos:
        print(f"New position: {pos['x']}, {pos['y']}")
    mgba.take_screenshot()

go_to_underground()
