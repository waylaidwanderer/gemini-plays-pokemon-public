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

# Currently at (2, 11) on 2F West (State A)
pos = mgba.get_coordinates()
print("Starting Row 15 path to 3F East stairs from:", pos)

if pos['x'] == 2 and pos['y'] == 11:
    print("--- STEP 1: WALKING TO 2F WEST SWITCH ENTRY ---")
    if not walk_step(2, 12, 'Down'):
        print("Failed to walk to (2, 12)")
        exit()

# Standing at (2, 12) on 2F West (State A)
pos = mgba.get_coordinates()
if pos['x'] == 2 and pos['y'] == 12:
    print("--- STEP 2: WALKING TO stairs at (15, 11) on 2F East ---")
    path_to_stairs = [
        # Walk back to (12, 12) on Row 12 (open in State A!)
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
print("Position on next floor after climbing stairs:", pos)
mgba.take_screenshot()
