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

# Currently at (2, 11) on 3F West in State B
# PHASE 5: Warp DOWN to 2F West
print("PHASE 5: Warp DOWN to 2F West...")
success = True
if success:
    success = walk_to_tile(1, 13)
if success:
    success = walk_to_tile(5, 13)
if success:
    success = walk_to_tile(5, 10)

if success:
    print("Stepping LEFT onto (5, 10) to warp DOWN to 2F...")
    mgba.press_buttons(["Left", "sleep 400"])
    time.sleep(1.5)
    print("New position on 2F West:", get_pos())

# PHASE 6: Warp DOWN to 1F West
print("PHASE 6: Warp DOWN to 1F West...")
pos = get_pos()
if pos['y'] == 10:
    mgba.press_buttons(["Down", "sleep 200"])
success = walk_to_tile(5, 11)
if success:
    print("Stepping UP onto stairs at (5, 10) to warp DOWN to 1F...")
    mgba.press_buttons(["Up", "sleep 400"])
    time.sleep(1.5)
    print("New position on 1F West:", get_pos())

# PHASE 7: Cross horizontally to 1F East on Row 5
print("PHASE 7: Crossing to 1F East on Row 5...")
if success:
    success = walk_to_tile(5, 5)
if success:
    success = walk_to_tile(21, 5)

# PHASE 8: Warp DOWN to B1F East (stairs at 22, 2)
print("PHASE 8: Warp DOWN to B1F East...")
if success:
    success = walk_to_tile(21, 2)
if success:
    success = walk_to_tile(22, 2)
if success:
    print("Stepping UP to warp to B1F East...")
    mgba.press_buttons(["Up", "sleep 400"])
    time.sleep(1.5)
    print("New position on B1F East:", get_pos())

# PHASE 9: Retrieve Secret Key on B1F West
print("PHASE 9: Walking along B1F Row 5 to Secret Key...")
if success:
    success = walk_to_tile(19, 5)
if success:
    success = walk_to_tile(1, 5)

if success:
    print("Arrived at Secret Key room! Picking it up...")
    mgba.press_buttons(["Up", "sleep 300", "A", "sleep 500", "B", "sleep 500", "A", "sleep 500", "B", "sleep 500"])
    print("Secret Key retrieved! Current position:", get_pos())

# PHASE 10: DIG out back to Cinnabar Island
if success:
    print("PHASE 10: Escaping via DIG...")
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
