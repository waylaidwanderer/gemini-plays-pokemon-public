import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def escape_battle():
    print("Coordinates did not change. Checking for battle or text box...")
    # Mash B to dismiss dialogue
    mgba.press_buttons(["B", "sleep 150", "B", "sleep 150", "B", "sleep 150", "B", "sleep 150"])
    # Attempt to run: Fight -> Down (Item) -> Right (Run) -> A
    print("Attempting to RUN...")
    mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 1200"])
    # Press B to dismiss escape message
    mgba.press_buttons(["B", "sleep 150", "B", "sleep 150"])

def walk_step(direction):
    mgba.press_buttons([direction, "sleep 350"])

def probe_path():
    print("Starting probe path from", get_pos())
    # 1. Walk Left to Column 13
    for i in range(2):
        curr_x, curr_y = get_pos()
        walk_step("Left")
        new_x, new_y = get_pos()
        if new_x == curr_x and new_y == curr_y:
            # Stymied by battle or obstacle
            escape_battle()
            # Retry step
            walk_step("Left")
            
    print("At Column 13, current pos:", get_pos())
    
    # 2. Walk Down to Row 30
    steps_needed = 8  # 22 to 30 is 8 steps
    for i in range(steps_needed):
        curr_x, curr_y = get_pos()
        walk_step("Down")
        new_x, new_y = get_pos()
        if new_x == curr_x and new_y == curr_y:
            escape_battle()
            # Retry
            walk_step("Down")
            new_x, new_y = get_pos()
            if new_x == curr_x and new_y == curr_y:
                print(f"FAILED: Blocked going Down at {curr_x}, {curr_y}")
                return
                
    print("SUCCESS: Reached Row 30! Pos:", get_pos())

if __name__ == "__main__":
    probe_path()
