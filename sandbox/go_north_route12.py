import mgba
import time

def navigate_north():
    print("Starting northward navigation on Route 12...")
    for step in range(50): # limit steps to avoid infinite loop
        pos = mgba.get_coordinates()
        if not pos:
            print("Failed to get coordinates, stopping.")
            break
        x, y = pos['x'], pos['y']
        print(f"Current Position: {x}, {y}")
        
        if y <= 16:
            print("Reached y <= 16! Target gatehouse reached.")
            mgba.take_screenshot()
            break
            
        # Press Up
        mgba.press_buttons(["Up"])
        # Wait a little bit for movement or battle transition
        time.sleep(0.6)
        
        new_pos = mgba.get_coordinates()
        if not new_pos:
            print("Failed to get coordinates after move, stopping.")
            break
        new_x, new_y = new_pos['x'], new_pos['y']
        
        if new_x == x and new_y == y:
            print(f"Movement failed at ({x}, {y}). Might be blocked, in a battle, or map transition.")
            mgba.take_screenshot()
            break

navigate_north()
