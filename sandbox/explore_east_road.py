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

# Currently at (10, 26) on 1F West (State B)
pos = mgba.get_coordinates()
print("Starting definitive alternate stairs route from:", pos)

if pos['x'] == 10 and pos['y'] == 26:
    print("--- STEP 1: WALKING TO 1F EAST ALTERNATE STAIRS AT (18, 10) ---")
    path = [
        # Walk UP Column 10 from Row 26 to Row 5
        (10, 25, 'Up'),
        (10, 24, 'Up'),
        (10, 23, 'Up'),
        (10, 22, 'Up'),
        (10, 21, 'Up'),
        (10, 20, 'Up'),
        (10, 19, 'Up'),
        (10, 18, 'Up'),
        (10, 17, 'Up'),
        (10, 16, 'Up'),
        (10, 15, 'Up'),
        (10, 14, 'Up'),
        (10, 13, 'Up'),
        (10, 12, 'Up'),
        (10, 11, 'Up'),
        (10, 10, 'Up'),
        (10, 9, 'Up'),
        (10, 8, 'Up'),
        (10, 7, 'Up'),
        (10, 6, 'Up'),
        (10, 5, 'Up'),
        # Walk RIGHT along Row 5 to Column 18
        (11, 5, 'Right'),
        (12, 5, 'Right'),
        (13, 5, 'Right'),
        (14, 5, 'Right'),
        (15, 5, 'Right'), # Through open gate at (15, 5) in State B!
        (16, 5, 'Right'),
        (17, 5, 'Right'),
        (18, 5, 'Right'),
        # Walk DOWN Column 18 to Row 10
        (18, 6, 'Down'),
        (18, 7, 'Down'),
        (18, 8, 'Down'),
        (18, 9, 'Down'),
        (18, 10, 'Down'),
    ]
    for target in path:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()
            
    print("At (18, 10) on 1F East. Stepping UP to enter alternate stairs...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)

# Land on next floor (2F East)
pos = mgba.get_coordinates()
print("Position on next floor after climbing alternate stairs:", pos)

if pos['x'] != 10 or pos['y'] != 26: # Check if we successfully went up
    print("--- STEP 2: WALKING TO 3F EAST STAIRS ---")
    # Land at (20, 16) or similar. Walk left along Row 16 to Column 15
    path_to_stairs_2f = [
        (19, 16, 'Left'),
        (18, 16, 'Left'),
        (17, 16, 'Left'),
        (16, 16, 'Left'),
        (15, 16, 'Left'),
    ]
    for target in path_to_stairs_2f:
        tx, ty, d = target
        walk_step(tx, ty, d)
        
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
