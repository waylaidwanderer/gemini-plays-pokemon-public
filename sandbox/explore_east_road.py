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

# Currently at (10, 6) on 2F West/Central (State B)
pos = mgba.get_coordinates()
print("Starting definitive 2F West switch toggle to State A via Row 10 from:", pos)

if pos['x'] == 10 and pos['y'] == 6:
    print("--- STEP 1: WALKING TO 2F WEST SWITCH VIA ROW 10 ---")
    path_to_switch = [
        # Walk DOWN Column 10 to Row 10
        (10, 7, 'Down'),
        (10, 8, 'Down'),
        (10, 9, 'Down'),
        (10, 10, 'Down'),
        # Walk LEFT along Row 10 to Column 2
        (9, 10, 'Left'),
        (8, 10, 'Left'),
        (7, 10, 'Left'),
        (6, 10, 'Left'),
        (5, 10, 'Left'),
        (4, 10, 'Left'),
        (3, 10, 'Left'),
        (2, 10, 'Left'),
        # Walk DOWN Column 2 to Row 12
        (2, 11, 'Down'),
        (2, 12, 'Down'),
    ]
    for target in path_to_switch:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()
            
    print("At (2, 12) on 2F West. Facing UP and toggling switch back to State A...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    mgba.press_buttons(["A", "sleep 600", "A", "sleep 600", "B"])
    time.sleep(1.5)

# We are on 2F West at (2, 11) in State A.
pos = mgba.get_coordinates()
print("Position on 2F West after toggling to State A:", pos)

if pos['x'] == 2 and pos['y'] == 11:
    print("--- STEP 2: WALKING TO stairs at (15, 11) on 2F East ---")
    path_to_stairs = [
        # Walk to (12, 12) on Row 12 (since Row 13 gate is open in State A!)
        (2, 12, 'Down'),
        (3, 12, 'Right'),
        (4, 12, 'Right'),
        (5, 12, 'Right'),
        (6, 12, 'Right'),
        (7, 12, 'Right'),
        (8, 12, 'Right'),
        (9, 12, 'Right'),
        (10, 12, 'Right'),
        (11, 12, 'Right'),
        (12, 12, 'Right'),
        # Walk DOWN Column 12 to Row 15
        (12, 13, 'Down'), # Open in State A!
        (12, 14, 'Down'),
        (12, 15, 'Down'),
        # Walk RIGHT along Row 15 to Column 15
        (13, 15, 'Right'),
        (14, 15, 'Right'),
        (15, 15, 'Right'),
        # Walk UP Column 15 to stairs at (15, 11)
        (15, 14, 'Up'),
        (15, 13, 'Up'),
        (15, 12, 'Up'),
        (15, 11, 'Up'),
    ]
    for target in path_to_stairs:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach stairs at ({tx}, {ty})")
            exit()
            
    print("At (15, 11) on 2F East. Stepping UP to go UP to 3F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)

pos = mgba.get_coordinates()
print("Position on 3F East after warp:", pos)
mgba.take_screenshot()
