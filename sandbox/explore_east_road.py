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

# Currently at (5, 11) on 1F West
pos = mgba.get_coordinates()
print("Starting explore_east_road from 1F West (5, 11):", pos)

if pos['x'] == 5 and pos['y'] == 11:
    print("--- STEP 1: WALK TO 1F EAST ALTERNATE STAIRS AT (18, 10) ---")
    path = [
        # Walk RIGHT to Column 10 on Row 11
        (6, 11, 'Right'),
        (7, 11, 'Right'),
        (8, 11, 'Right'),
        (9, 11, 'Right'),
        (10, 11, 'Right'),
        # Walk UP Column 10 to Row 8
        (10, 10, 'Up'),
        (10, 9, 'Up'),
        (10, 8, 'Up'),
        # Walk RIGHT along Row 8 to Column 18
        (11, 8, 'Right'),
        (12, 8, 'Right'),
        (13, 8, 'Right'),
        (14, 8, 'Right'),
        (15, 8, 'Right'), # Through open gate at (15, 8) in State B!
        (16, 8, 'Right'),
        (17, 8, 'Right'),
        (18, 8, 'Right'),
        # Walk DOWN Column 18 to Row 10
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

if pos['x'] != 5: # Check if we successfully went up
    print("--- STEP 2: WALKING TO 3F EAST STAIRS ---")
    # Land at (20, 16) or similar. Let's walk to Row 16, Column 20 first if needed
    # (stairs normally warp us directly to (20, 16) or adjacent)
    # Walk left along Row 16 to Column 15
    path_to_stairs_2f = [
        (19, 16, 'Left'),
        (18, 16, 'Left'),
        (17, 16, 'Left'),
        (16, 16, 'Left'),
        (15, 16, 'Left'),
    ]
    for target in path_to_stairs_2f:
        tx, ty, d = target
        # Since we might not land exactly at (20, 16), let's ensure we walk correctly
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
