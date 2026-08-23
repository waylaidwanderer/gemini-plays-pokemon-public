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

# Currently at (22, 2) on 1F East in State A
# PHASE 1: Walk to 1F East stairs at (18, 10) and warp UP to 2F East
print("PHASE 1: Warp UP to 2F East...")
success = True
if success:
    success = walk_to_tile(22, 3)
if success:
    success = walk_to_tile(18, 3)
if success:
    success = walk_to_tile(18, 11)
if success:
    print("Stepping UP onto stairs at (18, 10) to warp UP...")
    mgba.press_buttons(["Up", "sleep 400"])
    time.sleep(1.5)
    print("New position on 2F East:", get_pos())

# PHASE 2: Walk to 2F West to 3F West stairs at (7, 10) and warp UP
print("PHASE 2: Warp UP to 3F West...")
# We land around (18, 11) or (18, 10) on 2F East. Let's walk to (18, 3)
pos = get_pos()
if pos['y'] == 10:
    mgba.press_buttons(["Down", "sleep 200"])
if success:
    success = walk_to_tile(18, 3)
if success:
    success = walk_to_tile(7, 3)
if success:
    success = walk_to_tile(7, 11)
if success:
    print("Stepping UP onto stairs at (7, 10) to warp UP...")
    mgba.press_buttons(["Up", "sleep 400"])
    time.sleep(1.5)
    print("New position on 3F West:", get_pos())

# PHASE 3: Walk detour path to switch at (2, 11) and toggle it to State B
print("PHASE 3: Walking detour to switch on 3F West...")
if success:
    # We land around (7, 11) on 3F West.
    success = walk_to_tile(8, 11)
if success:
    success = walk_to_tile(8, 10)
if success:
    success = walk_to_tile(4, 10)
if success:
    success = walk_to_tile(4, 13)
if success:
    success = walk_to_tile(1, 13)
if success:
    success = walk_to_tile(1, 11)

if success:
    print("Arrived at (1, 11)! Toggling switch to State B...")
    mgba.press_buttons(["Right", "sleep 200", "A", "sleep 500", "B", "sleep 200"])
    print("Mansion toggled to State B successfully! Current position:", get_pos())
else:
    print("Failed navigation!")
