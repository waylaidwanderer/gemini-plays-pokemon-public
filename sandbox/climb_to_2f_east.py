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

# Starting at (5, 27) inside Mansion 1F West (State A)
pos = mgba.get_coordinates()
print("Starting Mansion 1F alternate stairs climb from:", pos)

if pos['x'] == 5 and pos['y'] == 27:
    path_1f = [
        # Walk UP to clear exit warp
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
        # Walk UP onto stairs at (18, 10)
        (18, 10, 'Up'),
    ]
    for target in path_1f:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach 1F target at ({tx}, {ty})")
            exit()
            
    print("At (18, 10) on 1F East stairs. Stepping UP to go to 2F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.5)

print("Final position of 1F climb script:", mgba.get_coordinates())
mgba.take_screenshot()
