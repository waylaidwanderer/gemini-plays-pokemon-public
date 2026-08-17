import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def go_to_underground():
    print("Navigating west on Row 5 towards the Underground Path...")
    # Current Position is (41, 6)
    
    # 1. Walk UP 1 step to Row 5
    print("Step 1: Walking UP to Row 5...")
    press_and_wait("Up", 0.25)
    
    # 2. Walk LEFT to Column 12
    print("Step 2: Walking LEFT towards Column 12...")
    while True:
        pos = mgba.get_coordinates()
        if not pos:
            print("Failed to get coordinates, stopping.")
            break
        x, y = pos['x'], pos['y']
        print(f"Current Position: {x}, {y}")
        
        # Stop at Column 12
        if x <= 12:
            print("Reached Column 12! Stopping to enter the building.")
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
            print(f"Movement failed at ({x}, {y}). Might be blocked by an NPC or obstacle.")
            mgba.take_screenshot()
            break

go_to_underground()
