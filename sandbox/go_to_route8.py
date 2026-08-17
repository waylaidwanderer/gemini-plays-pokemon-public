import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def go_to_route8():
    print("Navigating to Route 8 from Lavender Town...")
    
    # 1. Walk Right 2 steps to Column 10
    print("Step 1: Walking Right to Column 10...")
    for _ in range(2):
        press_and_wait("Right", 0.25)
        
    # 2. Walk UP 9 steps to Row 8
    print("Step 2: Walking UP to Row 8...")
    for _ in range(9):
        press_and_wait("Up", 0.25)
        
    # 3. Walk LEFT to transition to Route 8
    print("Step 3: Walking LEFT to transition to Route 8...")
    # Walk 15 steps Left to ensure we cross Column 0 and trigger transition
    for i in range(15):
        pos = mgba.get_coordinates()
        if pos:
            print(f"Current position: {pos['x']}, {pos['y']}")
            # In Route 8, our X coordinate will be near 59, and map will change
            # Let's check if the map has changed or X coordinate jumped to > 50
            if pos['x'] > 50:
                print("Transitioned to Route 8!")
                break
        press_and_wait("Left", 0.25)
        
    img = mgba.take_screenshot()
    print(f"Route 8 transition check complete! Screenshot: {img}")

go_to_route8()
