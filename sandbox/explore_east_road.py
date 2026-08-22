import mgba
import time

def handle_battle():
    print("Coordinates did not change. Likely a battle! Attempting to flee...")
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.0)
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.3)

def walk_step(tx, ty, direction):
    attempts = 0
    while attempts < 15:
        pos = mgba.get_coordinates()
        if pos['x'] == tx and pos['y'] == ty:
            return True
            
        mgba.press_buttons([direction])
        time.sleep(0.55)
        new_pos = mgba.get_coordinates()
        
        if new_pos == pos:
            print(f"Bumped at {pos} going {direction}. Attempting battle escape...")
            handle_battle()
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
        else:
            if new_pos['x'] == tx and new_pos['y'] == ty:
                return True
        attempts += 1
    return False

def walk_to_local(tx, ty):
    pos = mgba.get_coordinates()
    attempts = 0
    while (pos['x'] != tx or pos['y'] != ty) and attempts < 40:
        dx = tx - pos['x']
        dy = ty - pos['y']
        if dx < 0: d = "Left"
        elif dx > 0: d = "Right"
        elif dy < 0: d = "Up"
        else: d = "Down"
        
        pos_before = pos
        mgba.press_buttons([d])
        time.sleep(0.55)
        pos = mgba.get_coordinates()
        if pos == pos_before:
            handle_battle()
            pos = mgba.get_coordinates()
        attempts += 1
    return pos['x'] == tx and pos['y'] == ty

# Start at (10, 7) on 2F West/Central (State B)
pos = mgba.get_coordinates()
print("Starting explore_east_road from:", pos)

if pos['x'] == 10 and pos['y'] == 7:
    print("--- STEP 1: GO TO 1F WEST VIA 2F WEST STAIRS ---")
    path_to_2f_west_stairs = [
        # Walk LEFT along Row 7 to Column 7
        (9, 7, 'Left'),
        (8, 7, 'Left'),
        (7, 7, 'Left'),
        # Walk DOWN Column 7 to Row 10
        (7, 8, 'Down'),
        (7, 9, 'Down'),
        (7, 10, 'Down'),
    ]
    for target in path_to_2f_west_stairs:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach 2F West stairs at ({tx}, {ty})")
            exit()
            
    print("Stepping DOWN to go DOWN the stairs to 1F West...")
    mgba.press_buttons(["Down"])
    time.sleep(2.0)

# We land on 1F West (State B)
pos = mgba.get_coordinates()
print("Position on 1F West after stairs:", pos)

if pos['x'] == 7:
    print("--- STEP 2: WALKING TO 1F EAST ALTERNATE STAIRS AT (18, 10) ---")
    path_to_alternate_stairs = [
        # Walk to Row 8
        (7, 9, 'Up' if pos['y'] > 8 else 'Down'),
        (7, 8, 'Up' if pos['y'] > 8 else 'Down'),
        # Walk RIGHT along Row 8 to Column 18
        (8, 8, 'Right'),
        (9, 8, 'Right'),
        (10, 8, 'Right'),
        (11, 8, 'Right'),
        (12, 8, 'Right'),
        (13, 8, 'Right'),
        (14, 8, 'Right'),
        (15, 8, 'Right'), # Through the gate at (15, 8) which is open in State B!
        (16, 8, 'Right'),
        (17, 8, 'Right'),
        (18, 8, 'Right'),
        # Walk DOWN Column 18 to Row 10
        (18, 9, 'Down'),
        (18, 10, 'Down'),
    ]
    for target in path_to_alternate_stairs:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach 1F East stairs at ({tx}, {ty})")
            exit()
            
    print("Stepping UP to enter 1F East alternate stairs and go UP to 2F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)

pos = mgba.get_coordinates()
print("Position on 2F East after alternate stairs:", pos)

# Let's test walking to Column 15 and going UP to Row 11
if pos['x'] == 20 and pos['y'] == 16:
    print("--- STEP 3: TRYING TO REACH 3F EAST STAIRS FROM (20, 16) ---")
    path_to_stairs_2f = [
        (19, 16, 'Left'),
        (18, 16, 'Left'),
        (17, 16, 'Left'),
        (16, 16, 'Left'),
        (15, 16, 'Left'),
    ]
    for target in path_to_stairs_2f:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to walk along Row 16 at target ({tx}, {ty})")
            break
            
    print("At Column 15. Trying to walk UP to stairs at (15, 11)...")
    path_up_15 = [
        (15, 15, 'Up'),
        (15, 14, 'Up'),
        (15, 13, 'Up'),
        (15, 12, 'Up'),
        (15, 11, 'Up'),
    ]
    for target in path_up_15:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Blocked on Column 15 at target ({tx}, {ty})")
            break
            
    pos_stairs = mgba.get_coordinates()
    print("Final position of stairs test:", pos_stairs)
    if pos_stairs['x'] == 15 and pos_stairs['y'] == 11:
        print("SUCCESS! We reached the stairs at (15, 11) on 2F East!")
        mgba.press_buttons(["Up"])
        time.sleep(2.0)
        print("Warped to 3F East! Current position:", mgba.get_coordinates())
        
mgba.take_screenshot()
