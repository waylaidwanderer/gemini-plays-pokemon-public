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

# Starting at (12, 12) on 1F West (State B)
pos = mgba.get_coordinates()
print("Starting 1F West to East crossing script from:", pos)

if pos['x'] == 12 and pos['y'] == 12:
    print("--- STEP 1: WALKING UP COLUMN 12 TO ROW 6 ---")
    path_up = [
        (12, 11, 'Up'),
        (12, 10, 'Up'),
        (12, 9, 'Up'),
        (12, 8, 'Up'),
        (12, 7, 'Up'),
        (12, 6, 'Up'),
    ]
    for target in path_up:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach 1F West target at ({tx}, {ty})")
            exit()

pos = mgba.get_coordinates()
if pos['x'] == 12 and pos['y'] == 6:
    print("--- STEP 2: WALKING TO 1F EAST VIA OPEN GATE (15, 8) ---")
    path_to_1f_east = [
        # Walk RIGHT to Column 15 on Row 6
        (13, 6, 'Right'),
        (14, 6, 'Right'),
        (15, 6, 'Right'),
        # Since we are in State B, walk DOWN through the open gate at (15, 8)
        (15, 7, 'Down'),
        (15, 8, 'Down'),
        (15, 9, 'Down'),
        # Walk RIGHT along Row 9 to Column 26
        (16, 9, 'Right'),
        (17, 9, 'Right'),
        (18, 9, 'Right'),
        (19, 9, 'Right'),
        (20, 9, 'Right'),
        (21, 9, 'Right'),
        (22, 9, 'Right'),
        (23, 9, 'Right'),
        (24, 9, 'Right'),
        (25, 9, 'Right'),
        (26, 9, 'Right'),
        # Walk UP Column 26 to stairs at (26, 6)
        (26, 8, 'Up'),
        (26, 7, 'Up'),
        (26, 6, 'Up'),
    ]
    for target in path_to_1f_east:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed on 1F State B at ({tx}, {ty})")
            exit()
            
    print("At 1F East stairs (26, 6). Stepping UP to go to 2F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.5)

print("Final position after 1F East crossing:", mgba.get_coordinates())
mgba.take_screenshot()
