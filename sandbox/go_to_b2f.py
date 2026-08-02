import time
import mgba

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting go_to_b2f from {pos}")

if pos['x'] == 23 and pos['y'] == 15:
    # Right 2 steps to (25, 15)
    pos = move(['Right'])
    pos = move(['Right'])
    
    # Up 4 steps to (25, 11)
    for _ in range(4):
        pos = move(['Up'])
        
    # Left 2 steps to (23, 11)
    for _ in range(2):
        pos = move(['Left'])
        
    # Up 9 steps to (23, 2)
    for _ in range(9):
        pos = move(['Up'])
        
    print("Waiting for floor transition...")
    time.sleep(2.0)
    print(f"Final position on B2F: {mgba.get_coordinates()}")

mgba.take_screenshot()
