import mgba
import time

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("Potential battle or obstacle! Attempting to run/clear...")
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 100"])
    # Select RUN (Right, Down, A)
    mgba.press_buttons(["Right", "sleep 150", "Down", "sleep 150", "A", "sleep 500"])
    for _ in range(3):
        mgba.press_buttons(["B", "sleep 100"])

def walk_to_tile(tx, ty):
    print(f"Target: ({tx}, {ty})")
    max_attempts = 40
    for attempt in range(max_attempts):
        pos = get_pos()
        x, y = pos['x'], pos['y']
        if x == tx and y == ty:
            print(f"Arrived at ({tx}, {ty})!")
            return True
            
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
            print("Did not move. Waiting for NPC or checking for battle...")
            moved = False
            for wait_attempt in range(5):
                mgba.press_buttons(["sleep 200"]) # Wait a bit for NPC to move
                mgba.press_buttons([d, "sleep 150"])
                pos_check = get_pos()
                if pos_check != pos:
                    moved = True
                    break
            
            if not moved:
                print("Still blocked. Assuming battle, running...")
                run_from_battle()
                mgba.press_buttons([d, "sleep 150"])
            
    print(f"Failed to reach ({tx}, {ty}) after {max_attempts} attempts.")
    return False

# Currently at (8, 13) on 2F West
# Path to stairs: (8, 13) -> (8, 11) -> (6, 11) -> (6, 10) -> (5, 10)
success = True
if success:
    success = walk_to_tile(8, 11)
if success:
    success = walk_to_tile(6, 11)
if success:
    success = walk_to_tile(6, 10)
if success:
    success = walk_to_tile(5, 10)

if success:
    print("Arrived at stairs (5, 10) on 2F West! Current position:", get_pos())
else:
    print("Failed navigation!")
