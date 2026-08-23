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

# Currently at (7, 10) on 3F West in State B
# PHASE 1: Walk to Row 6 and walk to the 3F East pitfall at (26, 6)
print("PHASE 1: Walking Row 6 to 3F East pitfall...")
success = True
if success:
    success = walk_to_tile(10, 11)
if success:
    success = walk_to_tile(10, 6)
if success:
    success = walk_to_tile(26, 6)

if success:
    print("Stepped into the pitfall! Waiting to land on 1F East...")
    time.sleep(2.0)
    print("New position on 1F East:", get_pos())

# PHASE 2: Walk to B1F stairs at (22, 2) on 1F East and warp DOWN
print("PHASE 2: Warp DOWN to B1F East...")
if success:
    # We land around (25, 6) on 1F East inside the fenced room.
    success = walk_to_tile(22, 6)
if success:
    success = walk_to_tile(22, 2)
if success:
    print("Stepping UP to warp down to B1F...")
    mgba.press_buttons(["Up", "sleep 400"])
    time.sleep(1.5)
    print("New position on B1F East:", get_pos())

# PHASE 3: Walk along B1F Row 5 across Column 9 gate to (1, 5)
print("PHASE 3: Crossing B1F Row 5 to Secret Key...")
if success:
    success = walk_to_tile(19, 5)
if success:
    success = walk_to_tile(1, 5)

# PHASE 4: Retrieve Secret Key at (1, 4)
if success:
    print("PHASE 4: Picking up the Secret Key at (1, 4)...")
    mgba.press_buttons(["Up", "sleep 300", "A", "sleep 500", "B", "sleep 500", "A", "sleep 500", "B", "sleep 500"])
    print("Secret Key retrieved! Current position:", get_pos())

# PHASE 5: DIG out back to Cinnabar Island
if success:
    print("PHASE 5: Escaping via DIG...")
    mgba.press_buttons(["Start", "sleep 300"])
    mgba.press_buttons(["Down", "sleep 150", "A", "sleep 600"]) # Select POKéMON
    for _ in range(5):
        mgba.press_buttons(["Down", "sleep 150"])
    mgba.press_buttons(["A", "sleep 500"]) # Select TRUFFLE (Slot 6)
    mgba.press_buttons(["A", "sleep 1000"]) # Select DIG
    time.sleep(3.0)
    print("SUCCESS! Final position on Cinnabar Island:", get_pos())
else:
    print("Failed navigation!")
