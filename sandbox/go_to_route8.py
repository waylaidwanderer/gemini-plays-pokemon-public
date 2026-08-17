import mgba
import time

def press_and_wait(button, delay=0.15):
    mgba.press_buttons([button])
    time.sleep(delay)

def walk_through_underground():
    print("Walking through Saffron Underground Path...")
    while True:
        pos = mgba.get_coordinates()
        if not pos:
            print("Failed to get coordinates, stopping.")
            break
        x, y = pos['x'], pos['y']
        print(f"Current Position: {x}, {y}")
        
        # Stop at Column 2
        if x <= 2:
            print("Reached Column 2! Now walking DOWN to the ladder at (2, 5)...")
            break
            
        # Walk Left
        mgba.press_buttons(["Left"])
        time.sleep(0.3)
        
        new_pos = mgba.get_coordinates()
        if not new_pos:
            print("Failed to get coordinates, stopping.")
            break
        new_x, new_y = new_pos['x'], new_pos['y']
        if new_x == x and new_y == y:
            print(f"Blocked at ({x}, {y})")
            mgba.take_screenshot()
            return

    # Once at x=2, walk DOWN to y=5
    for _ in range(3):
        press_and_wait("Down", 0.25)
        
    pos = mgba.get_coordinates()
    if pos:
        print(f"Position after walking down: {pos['x']}, {pos['y']}")
    mgba.take_screenshot()

walk_through_underground()
