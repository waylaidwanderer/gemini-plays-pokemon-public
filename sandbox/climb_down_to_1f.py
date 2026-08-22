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

# Starting at (2, 12) on 2F West (State B)
pos = mgba.get_coordinates()
print("Starting safe climb down to 1F West from:", pos)

if pos['x'] == 2 and pos['y'] == 12:
    print("--- STEP 1: WALKING TO 2F WEST STAIRS ---")
    path_back_2f = [
        # Walk DOWN to Row 13
        (2, 13, 'Down'),
        # Walk RIGHT to Column 3 on Row 13 (bypassing Pit at (3, 12))
        (3, 13, 'Right'),
        # Walk RIGHT along Row 13 to Column 7
        (4, 13, 'Right'),
        (5, 13, 'Right'),
        (6, 13, 'Right'),
        (7, 13, 'Right'),
        # Walk UP Column 7 to Row 11
        (7, 12, 'Up'),
        (7, 11, 'Up'),
        # Walk RIGHT along Row 11 to Column 12 (bypassing stairs and pit)
        (8, 11, 'Right'),
        (9, 11, 'Right'),
        (10, 11, 'Right'),
        (11, 11, 'Right'),
        (12, 11, 'Right'),
        # Walk UP Column 12 to Row 3 (stairs)
        (12, 10, 'Up'),
        (12, 9, 'Up'),
        (12, 8, 'Up'),
        (12, 7, 'Up'),
        (12, 6, 'Up'),
        (12, 5, 'Up'),
        (12, 4, 'Up'),
        (12, 3, 'Up'),
    ]
    for target in path_back_2f:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed on 2F West at ({tx}, {ty})")
            exit()
            
    print("At 2F West stairs (12, 3). Stepping UP to go DOWN to 1F West (State B)...")
    mgba.press_buttons(["Up"])
    time.sleep(2.5)

print("Final position after 1F descent script:", mgba.get_coordinates())
mgba.take_screenshot()
