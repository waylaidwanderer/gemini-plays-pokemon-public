import mgba
import time

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    # Attempt to escape battle by mashing B, then selecting RUN
    print("Potential battle or obstacle! Attempting to run/clear...")
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 100"])
    # Select RUN (Right, Down, A)
    mgba.press_buttons(["Right", "sleep 150", "Down", "sleep 150", "A", "sleep 500"])
    for _ in range(3):
        mgba.press_buttons(["B", "sleep 100"])

def walk_to_tile(tx, ty):
    # Precise pathfinding step-by-step
    print(f"Target: ({tx}, {ty})")
    max_attempts = 40
    for attempt in range(max_attempts):
        pos = get_pos()
        x, y = pos['x'], pos['y']
        if x == tx and y == ty:
            print(f"Arrived at ({tx}, {ty})!")
            return True
            
        # Determine step direction
        if x < tx:
            d = "Right"
        elif x > tx:
            d = "Left"
        elif y < ty:
            d = "Down"
        elif y > ty:
            d = "Up"
        else:
            return True
            
        print(f"Currently at ({x}, {y}). Stepping {d}...")
        mgba.press_buttons([d, "sleep 150"])
        
        pos_after = get_pos()
        if pos == pos_after:
            # We didn't move! Could be a battle or an NPC/wall block
            print("Did not move. Checking for battle...")
            run_from_battle()
            # Try again
            mgba.press_buttons([d, "sleep 150"])
            
    print(f"Failed to reach ({tx}, {ty}) after {max_attempts} attempts.")
    return False

# Execute precise path to the 3F West Switch
# Path: (9, 11) -> (8, 11) -> (8, 13) -> (1, 13) -> (1, 11)
success = True
if success:
    success = walk_to_tile(8, 11)
if success:
    success = walk_to_tile(8, 13)
if success:
    success = walk_to_tile(1, 13)
if success:
    success = walk_to_tile(1, 11)

if success:
    print("Arrived at (1, 11)! Toggling switch...")
    mgba.press_buttons(["Right", "sleep 200", "A", "sleep 500", "B", "sleep 200"])
    pos = get_pos()
    print("Finished. Current position:", pos)
else:
    print("Failed navigation!")
