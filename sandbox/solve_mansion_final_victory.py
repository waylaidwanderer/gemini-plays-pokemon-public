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

# Starting at (10, 18) on 2F West (State A)
pos = mgba.get_coordinates()
print("Starting definitive Mansion Victory Part 2 from 2F West:", pos)

if pos['x'] == 10 and pos['y'] == 18:
    print("--- STEP 1: WALKING TO 2F EAST ALTERNATE STAIRS AT (19, 8) ---")
    path_to_stairs = [
        # Walk UP Column 10 to Row 10
        (10, 17, 'Up'),
        (10, 16, 'Up'),
        (10, 15, 'Up'),
        (10, 14, 'Up'),
        (10, 13, 'Up'),
        (10, 12, 'Up'),
        (10, 11, 'Up'),
        (10, 10, 'Up'),
        # Walk RIGHT along Row 10 to Column 12 on 2F East
        (11, 10, 'Right'),
        (12, 10, 'Right'),
        # Walk UP Column 12 to Row 6
        (12, 9, 'Up'),
        (12, 8, 'Up'),
        (12, 7, 'Up'),
        (12, 6, 'Up'),
        # Walk RIGHT along Row 6 to Column 19
        (13, 6, 'Right'),
        (14, 6, 'Right'),
        (15, 6, 'Right'),
        (16, 6, 'Right'),
        (17, 6, 'Right'),
        (18, 6, 'Right'),
        (19, 6, 'Right'),
        # Walk DOWN Column 19 to Row 8 (onto stairs)
        (19, 7, 'Down'),
        (19, 8, 'Down'),
    ]
    for target in path_to_stairs:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach stairs at ({tx}, {ty})")
            exit()
            
    print("Stepping DOWN to enter alternate stairs and go UP to 3F East...")
    mgba.press_buttons(["Down"])
    time.sleep(2.0)

pos = mgba.get_coordinates()
print("Position on next floor after climbing stairs (expected on 3F East):", pos)
mgba.take_screenshot()
