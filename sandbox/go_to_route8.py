import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def go_to_route8_final():
    print("Currently at (0, 14) on foot.")
    
    # 1. Walk UP to Row 8
    # Since we are at y=14, walking UP 6 steps gets us to y=8.
    print("Step 1: Walking UP to Row 8...")
    for _ in range(6):
        press_and_wait("Up", 0.25)
        
    # 2. Walk LEFT to transition to Route 8
    print("Step 2: Walking LEFT into Route 8...")
    # 5 steps Left should trigger the transition to Route 8 (59, 8)
    for _ in range(5):
        press_and_wait("Left", 0.25)
        
    # Verify new position
    pos = mgba.get_coordinates()
    if pos:
        print(f"New position: {pos['x']}, {pos['y']}")
    mgba.take_screenshot()

go_to_route8_final()
