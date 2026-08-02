import time
import mgba

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting find_stairs_b2f_left from {pos}")

if pos['x'] == 2 and pos['y'] == 9:
    # Let's walk to (1, 9)
    pos = move(['Left'])
    
    # Try Up to (1, 8)
    pos = move(['Up'])
    
    # Try Up to (1, 7)
    pos = move(['Up'])
    
    # Try Right to (2, 7)
    pos = move(['Right'])
    
    # Try Up to (2, 6)
    pos = move(['Up'])
    
    print("Waiting to see if we warp...")
    time.sleep(2.0)
    print(f"Final position: {mgba.get_coordinates()}")

mgba.take_screenshot()
