import mgba
import time

def handle_battle():
    print("Coordinates did not change. Handling battle safely...")
    # Clear dialogue
    for _ in range(3):
        mgba.press_buttons(["B"])
        time.sleep(0.25)
    # Flee (Down, Right, A)
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A"])
    time.sleep(1.5)
    # Clear dialogue
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.25)

def walk_step(tx, ty, d):
    attempts = 0
    while attempts < 15:
        pos = mgba.get_coordinates()
        if pos['x'] == tx and pos['y'] == ty:
            return True
        mgba.press_buttons([d])
        time.sleep(0.55)
        new_pos = mgba.get_coordinates()
        
        if new_pos == pos:
            print(f"Bumped at {pos} going {d} towards ({tx}, {ty}). Handling battle/obstacle...")
            handle_battle()
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
        else:
            if new_pos['x'] == tx and new_pos['y'] == ty:
                return True
        attempts += 1
    return False

# Starting at (12, 10) on 2F West (State B)
pos = mgba.get_coordinates()
print("Starting safe descent to 1F West via actual stairs (7, 10):", pos)

if pos['x'] == 12 and pos['y'] == 10:
    print("--- STEP 1: WALKING TO 2F WEST ACTUAL STAIRS AT (7, 10) ---")
    path_to_stairs = [
        # Walk DOWN to Row 11
        (12, 11, 'Down'),
        # Walk LEFT along Row 11 to Column 7
        (11, 11, 'Left'),
        (10, 11, 'Left'),
        (9, 11, 'Left'),
        (8, 11, 'Left'),
        (7, 11, 'Left'),
        # Walk UP onto stairs at (7, 10)
        (7, 10, 'Up'),
    ]
    for target in path_to_stairs:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()
            
    print("At 2F West main stairs (7, 10). Stepping UP to warp DOWN to 1F West...")
    mgba.press_buttons(["Up"])
    time.sleep(2.5)

pos = mgba.get_coordinates()
print("Position on 1F West after stairs (expected at (7, 10)):", pos)

# In case we land at (7, 10), walk to open gate at (15, 8)
if pos['x'] == 7 and pos['y'] == 10:
    print("--- STEP 2: WALKING TO 1F EAST VIA OPEN GATE (15, 8) ---")
    path_to_1f_east = [
        # Walk DOWN to Row 11
        (7, 11, 'Down'),
        # Walk RIGHT along Row 11 to Column 15
        (8, 11, 'Right'),
        (9, 11, 'Right'),
        (10, 11, 'Right'),
        (11, 11, 'Right'),
        (12, 11, 'Right'),
        (13, 11, 'Right'),
        (14, 11, 'Right'),
        (15, 11, 'Right'),
        # Walk UP Column 15 through open gate to Row 7
        (15, 10, 'Up'),
        (15, 9, 'Up'),
        (15, 8, 'Up'),
        (15, 7, 'Up'),
        # Walk UP to Row 6
        (15, 6, 'Up'),
        # Walk RIGHT along Row 6 to Column 26
        (16, 6, 'Right'),
        (17, 6, 'Right'),
        (18, 6, 'Right'),
        (19, 6, 'Right'),
        (20, 6, 'Right'),
        (21, 6, 'Right'),
        (22, 6, 'Right'),
        (23, 6, 'Right'),
        (24, 6, 'Right'),
        (25, 6, 'Right'),
        (26, 6, 'Right'),
    ]
    for target in path_to_1f_east:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed on 1F West State B at ({tx}, {ty})")
            exit()
            
    print("At 1F East stairs (26, 6). Stepping UP to go to 2F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.5)

print("Final position after script:", mgba.get_coordinates())
mgba.take_screenshot()
