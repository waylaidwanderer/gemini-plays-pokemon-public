import mgba
import time

def handle_battle_or_text():
    print("Detected battle or text! Dismissing/escaping...")
    # Press B to dismiss text, then Down+Right+A to run
    mgba.press_buttons(["B", "sleep 300", "Down", "Right", "A", "sleep 1000", "B"])
    time.sleep(0.5)

def dynamic_walk_to(tx, ty, max_steps=40):
    """
    Robustly walk to target (tx, ty) using dynamic pathfinding.
    Handles wild encounters, heals, and drift automatically.
    """
    print(f"Moving dynamically to target ({tx}, {ty})...")
    steps = 0
    while steps < max_steps:
        pos = mgba.get_coordinates()
        cx, cy = pos['x'], pos['y']
        print(f"At ({cx}, {cy}). Target: ({tx}, {ty})")
        
        if cx == tx and cy == ty:
            print("Successfully reached target!")
            return True
            
        # Determine direction
        direction = None
        if cx < tx:
            direction = "Right"
        elif cx > tx:
            direction = "Left"
        elif cy < ty:
            direction = "Down"
        elif cy > ty:
            direction = "Up"
            
        if not direction:
            break
            
        print(f"Pressing {direction}...")
        mgba.press_buttons([direction])
        time.sleep(0.4)
        
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            # We didn't move. Clear battle/text and try again
            handle_battle_or_text()
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                # If still blocked, we might have hit a wall
                print(f"Completely blocked at ({cx}, {cy}) going {direction}!")
                return False
                
        steps += 1
        
    print(f"Failed to reach ({tx}, {ty}) within {max_steps} steps.")
    return False

def run_master_route():
    # We are currently at (22, 7) on 3F (State B).
    pos = mgba.get_coordinates()
    print(f"Starting at: {pos}")
    if pos['x'] != 22 or pos['y'] != 7:
        print("Error: Not at (22, 7)!")
        return False
        
    # Walk to row 3 column 18
    print("--- STEP 1: Walking to (18, 3) on 3F ---")
    if not dynamic_walk_to(18, 7):
        return False
    if not dynamic_walk_to(18, 3):
        return False
        
    # Walk along row 3 to column 25
    print("--- STEP 2: Walking to (25, 3) on 3F ---")
    if not dynamic_walk_to(25, 3):
        return False
        
    # Walk Down column 25 to row 14
    print("--- STEP 3: Walking to (25, 14) on 3F ---")
    if not dynamic_walk_to(25, 14):
        return False
        
    # Walk Left to (24, 14)
    print("--- STEP 4: Walking to (24, 14) on 3F ---")
    if not dynamic_walk_to(24, 14):
        return False
        
    # Drop to 1F B1F stairs!
    print("--- STEP 5: Dropping to 1F B1F stairs ---")
    mgba.press_buttons(["Left"])
    time.sleep(1.5)
    
    pos = mgba.get_coordinates()
    print(f"Landed on 1F! Position: {pos}")
    mgba.take_screenshot()
    return True

if __name__ == "__main__":
    run_master_route()
