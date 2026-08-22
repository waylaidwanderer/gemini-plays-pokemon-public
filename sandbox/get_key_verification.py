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

# Starting at Cinnabar Island (11, 12)
pos = mgba.get_coordinates()
print("Starting verification run from Cinnabar:", pos)

if pos['x'] == 11 and pos['y'] == 12:
    # 1. Walk from Cinnabar Center to Mansion entrance
    cinnabar_path = [
        (12, 12, 'Right'),
        (13, 12, 'Right'),
        # Up Column 13 to Row 4
        (13, 11, 'Up'),
        (13, 10, 'Up'),
        (13, 9, 'Up'),
        (13, 8, 'Up'),
        (13, 7, 'Up'),
        (13, 6, 'Up'),
        (13, 5, 'Up'),
        (13, 4, 'Up'),
        # Left along Row 4 to Column 6
        (12, 4, 'Left'),
        (11, 4, 'Left'),
        (10, 4, 'Left'),
        (9, 4, 'Left'),
        (8, 4, 'Left'),
        (7, 4, 'Left'),
        (6, 4, 'Left'),
    ]
    for target in cinnabar_path:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed on Cinnabar at ({tx}, {ty})")
            exit()
            
    print("At (6, 4). Stepping UP to enter Mansion...")
    mgba.press_buttons(["Up"])
    time.sleep(2.5)

# Land inside Mansion 1F West
pos = mgba.get_coordinates()
print("Position inside Mansion 1F West:", pos)

if pos['x'] == 5 and pos['y'] == 27:
    path_to_1f_stairs = [
        # Walk UP Column 5 to clear exit warp
        (5, 26, 'Up'),
        (5, 25, 'Up'),
        (5, 24, 'Up'),
        (5, 23, 'Up'),
        # Walk RIGHT to Column 7
        (6, 23, 'Right'),
        (7, 23, 'Right'),
        # Walk UP Column 7 to Row 11
        (7, 22, 'Up'),
        (7, 21, 'Up'),
        (7, 20, 'Up'),
        (7, 19, 'Up'),
        (7, 18, 'Up'),
        (7, 17, 'Up'),
        (7, 16, 'Up'),
        (7, 15, 'Up'),
        (7, 14, 'Up'),
        (7, 13, 'Up'),
        (7, 12, 'Up'),
        (7, 11, 'Up'),
        # Walk right across Row 11
        (8, 11, 'Right'),
        (9, 11, 'Right'),
        (10, 11, 'Right'),
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
    for target in path_to_1f_stairs:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed on 1F at ({tx}, {ty})")
            exit()
            
    print("At (18, 10) on 1F East stairs. Stepping UP to go to 2F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.5)

print("Final position of verification run:", mgba.get_coordinates())
mgba.take_screenshot()
