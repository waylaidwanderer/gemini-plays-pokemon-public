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

# Currently at (10, 18) on 1F West (State A)
pos = mgba.get_coordinates()
print("Starting definitive Mansion Victory Part 2 from:", pos)

if pos['x'] == 10 and pos['y'] == 18:
    print("--- STEP 1: WALKING TO 1F EAST ALTERNATE STAIRS ---")
    path_to_stairs = [
        # Walk UP Column 10 to Row 11
        (10, 17, 'Up'),
        (10, 16, 'Up'),
        (10, 15, 'Up'),
        (10, 14, 'Up'),
        (10, 13, 'Up'),
        (10, 12, 'Up'),
        (10, 11, 'Up'),
        # Since we are in State A, the Row 11 gate is open! Walk RIGHT along Row 11 to Column 18
        (11, 11, 'Right'),
        (12, 11, 'Right'),
        (13, 11, 'Right'),
        (14, 11, 'Right'),
        (15, 11, 'Right'),
        (16, 11, 'Right'),
        (17, 11, 'Right'),
        (18, 11, 'Right'),
        # Walk UP to stairs at (18, 10)
        (18, 10, 'Up'),
    ]
    for target in path_to_stairs:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach stairs at ({tx}, {ty})")
            exit()
            
    print("Stepping UP to enter alternate stairs and go UP to 2F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)

# Land on 2F East (State A)
pos = mgba.get_coordinates()
print("Position on 2F East after climbing stairs (expected 22, 7):", pos)

if pos['x'] == 22 and pos['y'] == 7:
    print("--- STEP 2: WALKING TO 2F EAST STAIRS TO 3F EAST ---")
    path_to_stairs_3f = [
        # Walk LEFT along Row 7 to Column 19
        (21, 7, 'Left'),
        (20, 7, 'Left'),
        (19, 7, 'Left'),
        # Walk DOWN to Row 8 (onto stairs)
        (19, 8, 'Down'),
    ]
    for target in path_to_stairs_3f:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach stairs at ({tx}, {ty})")
            exit()
            
    print("Stepping DOWN to enter stairs and go UP to 3F East...")
    mgba.press_buttons(["Down"])
    time.sleep(2.0)

pos = mgba.get_coordinates()
print("Final position of Part 2 (expected on 3F East):", pos)
mgba.take_screenshot()
