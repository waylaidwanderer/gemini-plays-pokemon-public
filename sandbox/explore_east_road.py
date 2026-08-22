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

# Currently at (12, 12) on 2F East (State B)
pos = mgba.get_coordinates()
print("Starting explore_east_road from:", pos)

if pos['x'] == 12 and pos['y'] == 12:
    print("--- STEP 1: GO TO 1F WEST VIA 2F WEST STAIRS ---")
    path_to_2f_west_stairs = [
        # Walk UP Column 12 to Row 3
        (12, 11, 'Up'),
        (12, 10, 'Up'),
        (12, 9, 'Up'),
        (12, 8, 'Up'),
        (12, 7, 'Up'),
        (12, 6, 'Up'),
        (12, 5, 'Up'),
        (12, 4, 'Up'),
        (12, 3, 'Up'),
        # Walk LEFT along Row 3 to Column 7
        (11, 3, 'Left'),
        (10, 3, 'Left'),
        (9, 3, 'Left'),
        (8, 3, 'Left'),
        (7, 3, 'Left'),
        # Walk DOWN Column 7 to Row 10
        (7, 4, 'Down'),
        (7, 5, 'Down'),
        (7, 6, 'Down'),
        (7, 7, 'Down'),
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
print("Position on 1F West:", pos)

# Typically we land at (7, 11) or (7, 10).
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
            
    print("Stepping UP to enter 1F East alternate stairs and go UP...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)

pos = mgba.get_coordinates()
print("Position on next floor after climbing alternate stairs:", pos)
mgba.take_screenshot()
