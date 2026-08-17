import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def walk_west_route8():
    print("Walking west along Route 8...")
    while True:
        pos = mgba.get_coordinates()
        if not pos:
            print("Failed to get coordinates, stopping.")
            break
        x, y = pos['x'], pos['y']
        print(f"Current Position: {x}, {y}")
        
        # Saffron Gatehouse is at the far west (around column 2-5)
        if x <= 5:
            print("Reached Saffron Gatehouse area! Stopping.")
            break
            
        # Let's try to walk Left
        mgba.press_buttons(["Left"])
        time.sleep(0.4) # Wait for movement or battle trigger
        
        new_pos = mgba.get_coordinates()
        if not new_pos:
            print("Failed to get coordinates after move, stopping.")
            break
        new_x, new_y = new_pos['x'], new_pos['y']
        
        if new_x == x and new_y == y:
            print(f"Movement failed at ({x}, {y}). Might be blocked or in battle.")
            mgba.take_screenshot()
            break

walk_west_route8()
