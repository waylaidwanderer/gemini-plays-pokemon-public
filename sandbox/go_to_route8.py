import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def bypass_and_walk_west():
    print("Bypassing the Biker at (46, 13)...")
    # Current Position is (47, 13)
    
    # 1. Walk UP to Row 12
    press_and_wait("Up", 0.25)
    
    # 2. Walk LEFT 3 steps to Column 44
    for _ in range(3):
        press_and_wait("Left", 0.25)
        
    # 3. Walk DOWN 1 step to Row 13
    press_and_wait("Down", 0.25)
    
    # 4. Resume walking west until Column 5
    print("Resuming west-bound path...")
    while True:
        pos = mgba.get_coordinates()
        if not pos:
            print("Failed to get coordinates, stopping.")
            break
        x, y = pos['x'], pos['y']
        print(f"Current Position: {x}, {y}")
        
        if x <= 5:
            print("Reached Column 5! Stopping at the Saffron Gatehouse.")
            break
            
        # Try to walk Left
        mgba.press_buttons(["Left"])
        time.sleep(0.4)
        
        new_pos = mgba.get_coordinates()
        if not new_pos:
            print("Failed to get coordinates, stopping.")
            break
        new_x, new_y = new_pos['x'], new_pos['y']
        
        if new_x == x and new_y == y:
            print(f"Movement failed at ({x}, {y}). Might be blocked by another obstacle.")
            mgba.take_screenshot()
            break

bypass_and_walk_west()
