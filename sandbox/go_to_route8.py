import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def navigate_around_ledge_to_celadon():
    print("Navigating around the Route 7 ledge to Saffron/Celadon...")
    # Current Position is (2, 14) on foot
    
    # 1. Walk RIGHT 6 steps to Column 8
    print("Step 1: Walking RIGHT to Column 8...")
    for _ in range(6):
        press_and_wait("Right", 0.25)
        
    # 2. Walk UP 6 steps to Row 8 (climbing the ledge gap at (8, 11))
    print("Step 2: Walking UP to Row 8...")
    for _ in range(6):
        press_and_wait("Up", 0.25)
        
    # 3. Walk LEFT to Column 2
    print("Step 3: Walking LEFT to Column 2...")
    for _ in range(6):
        press_and_wait("Left", 0.25)
        
    # Check position
    pos = mgba.get_coordinates()
    if pos:
        print(f"Position at end of Step 3: {pos['x']}, {pos['y']}")
    mgba.take_screenshot()

navigate_around_ledge_to_celadon()
