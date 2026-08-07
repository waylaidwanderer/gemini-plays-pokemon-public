import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def escape_battle():
    print("Coordinates did not change. Checking for battle or text box...")
    # Press B to dismiss any dialogue or "Wild pokemon appeared" text
    # Mash B a few times to be safe
    mgba.press_buttons(["B", "sleep 200", "B", "sleep 200", "B", "sleep 200", "B", "sleep 200"])
    
    # Try to RUN: from Fight, Down moves to Item, Right moves to Run, A selects Run.
    print("Attempting to RUN...")
    mgba.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A", "sleep 1200"])
    
    # Press B to dismiss "Got away safely!" or retry if it failed
    mgba.press_buttons(["B", "sleep 200", "B", "sleep 200", "B", "sleep 200"])

def walk_step(direction):
    print(f"Stepping {direction}")
    mgba.press_buttons([direction, "sleep 600"])

def navigate_to(target_x, target_y):
    """
    Navigates to a specific target coordinate.
    Handles battles and obstacles by retrying.
    """
    print(f"Navigating to ({target_x}, {target_y})...")
    
    stuck_count = 0
    non_battle_stuck = 0
    last_x, last_y = None, None
    
    while True:
        curr_x, curr_y = get_pos()
        print(f"Current Pos: ({curr_x}, {curr_y}) | Target: ({target_x}, {target_y})")
        
        if curr_x == target_x and curr_y == target_y:
            print("Reached target!")
            return True
            
        dx = target_x - curr_x
        dy = target_y - curr_y
        
        # Determine next step direction
        if dx > 0:
            direction = "Right"
        elif dx < 0:
            direction = "Left"
        elif dy > 0:
            direction = "Down"
        elif dy < 0:
            direction = "Up"
        else:
            break
            
        walk_step(direction)
        new_x, new_y = get_pos()
        
        if new_x == curr_x and new_y == curr_y:
            stuck_count += 1
            if stuck_count >= 2:
                # Let's check if we are at the exact same coordinate as the previous loop's stuck detection
                if (curr_x, curr_y) == (last_x, last_y):
                    non_battle_stuck += 1
                    if non_battle_stuck >= 3:
                        print(f"ERROR: Physically stuck at ({curr_x}, {curr_y}) trying to go {direction}! Obstacle detected.")
                        raise RuntimeError(f"Physical obstacle at ({curr_x}, {curr_y}) going {direction}")
                else:
                    non_battle_stuck = 1
                    last_x, last_y = curr_x, curr_y
                
                escape_battle()
                stuck_count = 0
        else:
            stuck_count = 0
            non_battle_stuck = 0
            
        # Small sleep between steps
        time.sleep(0.1)

if __name__ == "__main__":
    # Test getting coordinates
    print("Current coordinates:", get_pos())
