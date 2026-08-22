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

# Starting at (10, 11) on 2F West/Central (State B)
pos = mgba.get_coordinates()
print("Starting explore_east_road from 2F:", pos)

if pos['x'] == 10 and pos['y'] == 11:
    print("--- STEP 1: GO TO 1F WEST VIA 2F WEST STAIRS ---")
    path_to_stairs = [
        (10, 10, 'Down'),
        (9, 10, 'Left'),
        (8, 10, 'Left'),
        (7, 10, 'Left'),
    ]
    for target in path_to_stairs:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach 2F West stairs at ({tx}, {ty})")
            exit()
            
    print("Stepping DOWN to go DOWN to 1F West...")
    mgba.press_buttons(["Down"])
    time.sleep(2.0)

# We land on 1F West (State B)
pos = mgba.get_coordinates()
print("Position on 1F West after stairs:", pos)

# Typically we land at (7, 11) or (7, 10).
if pos['x'] == 7:
    print("--- STEP 2: WALKING TO 1F EAST ALTERNATE STAIRS AT (18, 10) VIA ROW 5 ---")
    path_to_alternate_stairs = [
        # Walk UP Column 7 to Row 5
        (7, 9, 'Up' if pos['y'] > 8 else 'Down'),
        (7, 8, 'Up' if pos['y'] > 8 else 'Down'),
        (7, 7, 'Up'),
        (7, 6, 'Up'),
        (7, 5, 'Up'),
        # Walk RIGHT along Row 5 to Column 18
        (8, 5, 'Right'),
        (9, 5, 'Right'),
        (10, 5, 'Right'),
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
    for target in path_to_alternate_stairs:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach 1F East stairs at ({tx}, {ty})")
            exit()
            
    print("At (18, 10) on 1F East. Stepping UP to enter alternate stairs...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)

pos = mgba.get_coordinates()
print("Position on next floor after climbing alternate stairs:", pos)
mgba.take_screenshot()
