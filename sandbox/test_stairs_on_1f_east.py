import mgba
import time

def handle_battle():
    print("Coordinates did not change. Likely a battle! Attempting to flee...")
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.0)
    for _ in range(4):
        mgba.press_buttons(["B"])
        time.sleep(0.3)

def walk_step(tx, ty, direction):
    attempts = 0
    while attempts < 10:
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

# Starting at (12, 12) on 1F West inside the Mansion
pos = mgba.get_coordinates()
print("Starting test_stairs_on_1f_east from:", pos)

if pos['x'] == 12 and pos['y'] == 12:
    # 1. Walk down to Row 13
    print("Walking down to Row 13...")
    if not walk_step(12, 13, 'Down'):
        print("Failed to walk DOWN to Row 13")
        exit()

    # 2. Walk RIGHT along Row 13 to Column 16
    path_right = [
        (13, 13, 'Right'),
        (14, 13, 'Right'),
        (15, 13, 'Right'),
        (16, 13, 'Right'),
    ]
    print("Walking RIGHT along Row 13 to Column 16...")
    for target in path_right:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()

    # 3. Walk UP Column 16 to Row 11
    path_up = [
        (16, 12, 'Up'),
        (16, 11, 'Up'),
    ]
    print("Walking UP Column 16 to stairs...")
    for target in path_up:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()

    # 4. Step UP onto the stairs to warp to 2F East
    print("Stepping UP to enter 1F East stairs...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)

print("Coordinates after 1F East stairs warp:", mgba.get_coordinates())
mgba.take_screenshot()
