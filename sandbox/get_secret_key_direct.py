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

# Starting at (2, 7) on 1F West
pos = mgba.get_coordinates()
print("Starting Ultimate Master Mansion Route from:", pos)

if pos['x'] == 2 and pos['y'] == 7:
    print("--- STEP 1: WALKING TO 1F WEST STAIRS ---")
    path_1f = [
        (2, 6, 'Up'),
        (3, 6, 'Right'),
        (4, 6, 'Right'),
        (5, 6, 'Right'),
        (6, 6, 'Right'),
        (7, 6, 'Right'),
        (8, 6, 'Right'),
        (9, 6, 'Right'),
        (10, 6, 'Right'),
        (11, 6, 'Right'),
        (12, 6, 'Right'),
        (12, 5, 'Up'),
        (12, 4, 'Up'),
        (12, 3, 'Up'),
    ]
    for target in path_1f:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed on 1F at ({tx}, {ty})")
            exit()
            
    print("At 1F West stairs (12, 3). Stepping UP to warp to 2F West...")
    mgba.press_buttons(["Up"])
    time.sleep(2.5)

# Land on 2F West (expected at (12, 3))
pos = mgba.get_coordinates()
print("Position on 2F West:", pos)

# Walk down to Row 6 on 2F West
if pos['x'] == 12 and pos['y'] < 6:
    for r in range(pos['y'] + 1, 7):
        walk_step(12, r, 'Down')

pos = mgba.get_coordinates()
if pos['x'] == 12 and pos['y'] == 6:
    print("--- STEP 2: WALKING TO 2F WEST SWITCH BYPASSING PIT ---")
    path_2f = [
        # Walk left along Row 6 to Column 3 (bypassing Pit on Column 2)
        (11, 6, 'Left'),
        (10, 6, 'Left'),
        (9, 6, 'Left'),
        (8, 6, 'Left'),
        (7, 6, 'Left'),
        (6, 6, 'Left'),
        (5, 6, 'Left'),
        (4, 6, 'Left'),
        (3, 6, 'Left'),
        # Walk DOWN Column 3 to Row 12 (bypassing Pit on Column 2 Row 8)
        (3, 7, 'Down'),
        (3, 8, 'Down'),
        (3, 9, 'Down'),
        (3, 10, 'Down'),
        (3, 11, 'Down'),
        (3, 12, 'Down'),
        # Walk LEFT to Column 2
        (2, 12, 'Left'),
    ]
    for target in path_2f:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed on 2F West at ({tx}, {ty})")
            exit()
            
    print("At (2, 12) on 2F West. Facing UP and toggling switch to State B...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    # Interact with switch
    mgba.press_buttons(["A", "sleep 300", "A", "sleep 500", "B"])
    time.sleep(1.5)

pos = mgba.get_coordinates()
print("Position on 2F West after switch toggle:", pos)

# We are now on 2F West in State B. Walk back to 2F West stairs at (12, 3)
if pos['x'] == 2 and pos['y'] == 12:
    print("--- STEP 3: WALKING BACK TO 2F WEST STAIRS ---")
    path_back_2f = [
        # Walk RIGHT to Column 3 on Row 12
        (3, 12, 'Right'),
        # Walk UP Column 3 to Row 6
        (3, 11, 'Up'),
        (3, 10, 'Up'),
        (3, 9, 'Up'),
        (3, 8, 'Up'),
        (3, 7, 'Up'),
        (3, 6, 'Up'),
        # Walk RIGHT along Row 6 to Column 12
        (4, 6, 'Right'),
        (5, 6, 'Right'),
        (6, 6, 'Right'),
        (7, 6, 'Right'),
        (8, 6, 'Right'),
        (9, 6, 'Right'),
        (10, 6, 'Right'),
        (11, 6, 'Right'),
        (12, 6, 'Right'),
        # Walk UP to stairs
        (12, 5, 'Up'),
        (12, 4, 'Up'),
        (12, 3, 'Up'),
    ]
    for target in path_back_2f:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed back on 2F West at ({tx}, {ty})")
            exit()
            
    print("At 2F West stairs. Stepping UP to go DOWN to 1F West (State B)...")
    mgba.press_buttons(["Up"])
    time.sleep(2.5)

pos = mgba.get_coordinates()
print("Position on 1F West after stairs (expected at (12, 3)):", pos)

# In case we land at (12, 3), walk down to Row 6
if pos['x'] == 12 and pos['y'] < 6:
    for r in range(pos['y'] + 1, 7):
        walk_step(12, r, 'Down')

pos = mgba.get_coordinates()
if pos['x'] == 12 and pos['y'] == 6:
    print("--- STEP 4: WALKING THROUGH OPEN GATE AT (15, 8) TO 1F EAST ---")
    path_to_1f_east = [
        # Walk RIGHT to Column 15 on Row 6
        (13, 6, 'Right'),
        (14, 6, 'Right'),
        (15, 6, 'Right'),
        # Since we are in State B, walk DOWN through the open gate at (15, 8)
        (15, 7, 'Down'),
        (15, 8, 'Down'),
        (15, 9, 'Down'),
        # Walk RIGHT to Column 26
        (16, 9, 'Right'),
        (17, 9, 'Right'),
        (18, 9, 'Right'),
        (19, 9, 'Right'),
        (20, 9, 'Right'),
        (21, 9, 'Right'),
        (22, 9, 'Right'),
        (23, 9, 'Right'),
        (24, 9, 'Right'),
        (25, 9, 'Right'),
        (26, 9, 'Right'),
        # Walk UP to stairs at (26, 6)
        (26, 8, 'Up'),
        (26, 7, 'Up'),
        (26, 6, 'Up'),
    ]
    for target in path_to_1f_east:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed on 1F State B at ({tx}, {ty})")
            exit()
            
    print("At 1F East stairs (26, 6). Stepping UP to go to 2F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.5)

pos = mgba.get_coordinates()
print("Position on 2F East (expected at (26, 7)):", pos)

# In case we land at (26, 7), walk to stairs at (15, 11) on 2F East
if pos['x'] == 26 and pos['y'] == 7:
    print("--- STEP 5: WALKING TO 2F EAST STAIRS TO 3F EAST ---")
    path_to_3f_stairs = [
        # Walk DOWN to Row 11
        (26, 8, 'Down'),
        (26, 9, 'Down'),
        (26, 10, 'Down'),
        (26, 11, 'Down'),
        # Walk LEFT to Column 15 on Row 11
        (25, 11, 'Left'),
        (24, 11, 'Left'),
        (23, 11, 'Left'),
        (22, 11, 'Left'),
        (21, 11, 'Left'),
        (20, 11, 'Left'),
        (19, 11, 'Left'),
        (18, 11, 'Left'),
        (17, 11, 'Left'),
        (16, 11, 'Left'),
        (15, 11, 'Left'),
    ]
    for target in path_to_3f_stairs:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed on 2F East at ({tx}, {ty})")
            exit()
            
    print("At 2F East stairs (15, 11). Stepping UP to warp to 3F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.5)

pos = mgba.get_coordinates()
print("Position on 3F East (expected at (16, 11)):", pos)

# In case we land at (16, 11), walk to balcony drop-off at (20, 18)
if pos['x'] == 16 and pos['y'] == 11:
    print("--- STEP 6: WALKING TO 3F EAST BALCONY AND DROPPING ---")
    path_to_balcony = [
        # Walk RIGHT to Column 20
        (17, 11, 'Right'),
        (18, 11, 'Right'),
        (19, 11, 'Right'),
        (20, 11, 'Right'),
        # Walk DOWN to Row 18
        (20, 12, 'Down'),
        (20, 13, 'Down'),
        (20, 14, 'Down'),
        (20, 15, 'Down'),
        (20, 16, 'Down'),
        (20, 17, 'Down'), # Since we are in State B, this balcony gate is open!
        (20, 18, 'Down'),
    ]
    for target in path_to_balcony:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed on 3F East at ({tx}, {ty})")
            exit()
            
    print("At (20, 18). Stepping LEFT to drop from balcony...")
    mgba.press_buttons(["Left"])
    time.sleep(3.0)

pos = mgba.get_coordinates()
print("Position after balcony drop (expected on B1F East at (19, 16)):", pos)

# On B1F East in State B, walk UP to Row 5, and LEFT through open gate to get Secret Key
if pos['x'] == 19 and pos['y'] == 16:
    print("--- STEP 7: RETRIEVING SECRET KEY ON B1F ---")
    path_to_key = [
        # Walk UP Column 19 to Row 5
        (19, 15, 'Up'),
        (19, 14, 'Up'),
        (19, 13, 'Up'),
        (19, 12, 'Up'),
        (19, 11, 'Up'),
        (19, 10, 'Up'),
        (19, 9, 'Up'),
        (19, 8, 'Up'),
        (19, 7, 'Up'),
        (19, 6, 'Up'),
        (19, 5, 'Up'),
        # Walk LEFT along Row 5 through the open B1F gate at (9, 5) to Column 1
        (18, 5, 'Left'),
        (17, 5, 'Left'),
        (16, 5, 'Left'),
        (15, 5, 'Left'),
        (14, 5, 'Left'),
        (13, 5, 'Left'),
        (12, 5, 'Left'),
        (11, 5, 'Left'),
        (10, 5, 'Left'),
        (9, 5, 'Left'),
        (8, 5, 'Left'),
        (7, 5, 'Left'),
        (6, 5, 'Left'),
        (5, 5, 'Left'),
        (4, 5, 'Left'),
        (3, 5, 'Left'),
        (2, 5, 'Left'),
        (1, 5, 'Left'),
    ]
    for target in path_to_key:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed on B1F at ({tx}, {ty})")
            exit()
            
    print("At (1, 5). Facing UP and retrieving Secret Key...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    mgba.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "B", "sleep 300"])
    time.sleep(1.0)
    
    print("Secret Key retrieved successfully! ESCAPING VIA DIG...")
    # Open Start menu, select Pokémon, select TRUFFLE (Paras), select DIG
    mgba.press_buttons(["Start", "sleep 300", "Down", "A", "sleep 500"])
    mgba.press_buttons(["Down", "Down", "Down", "Down", "Down", "A", "sleep 300"])
    mgba.press_buttons(["A", "sleep 2000"])

print("Final position at end of Master Script:", mgba.get_coordinates())
mgba.take_screenshot()
