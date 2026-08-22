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

# Starting at (2, 10) on 2F West inside the Mansion (State B)
pos = mgba.get_coordinates()
print("Starting mansion_switch_to_3f from:", pos)

if pos['x'] == 2 and pos['y'] == 10:
    # 1. Walk down to (2, 11)
    walk_step(2, 11, 'Down')
    
    # 2. Walk RIGHT to (7, 11) and UP to stairs at (7, 10)
    path_to_stairs = [
        (3, 11, 'Right'),
        (4, 11, 'Right'),
        (5, 11, 'Right'),
        (6, 11, 'Right'),
        (7, 11, 'Right'),
        (7, 10, 'Up'),
    ]
    print("Walking to 2F West stairs...")
    for target in path_to_stairs:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()
            
    print("Stepping UP to enter 2F West stairs and go DOWN to 1F West...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)

# We land on 1F West at (7, 10). Walk to open gate at (15, 8)
pos = mgba.get_coordinates()
if pos['x'] == 7 and pos['y'] == 10:
    path_to_gate = [
        (7, 11, 'Down'),
        (11, 11, 'Right'),
        (11, 10, 'Up'),
        (12, 10, 'Right'),
        (12, 9, 'Up'),
        (12, 8, 'Up'),
        (13, 8, 'Right'),
        (14, 8, 'Right'),
        (15, 8, 'Right'), # Shutter gate (15, 8) is OPEN in State B!
        (16, 8, 'Right'), # Land on 1F East south of Row 7 gate!
    ]
    print("Walking to 1F gate at (15, 8) and crossing to 1F East...")
    for target in path_to_gate:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()

# We are on 1F East at (16, 8). Walk DOWN Column 16 to stairs at (16, 11)
pos = mgba.get_coordinates()
if pos['x'] == 16 and pos['y'] == 8:
    path_to_stairs_1f = [
        (16, 9, 'Down'),
        (16, 10, 'Down'),
        (16, 11, 'Down'),
    ]
    print("Walking to 1F East stairs...")
    for target in path_to_stairs_1f:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()
            
    print("Stepping DOWN to enter 1F East stairs and go UP to 2F East...")
    mgba.press_buttons(["Down"])
    time.sleep(2.0)

# We land on 2F East at (20, 16) (from 1F East stairs (18, 10)). Walk to 3F East stairs
pos = mgba.get_coordinates()
if pos['x'] == 20 and pos['y'] == 16:
    path_to_stairs_2f = [
        # Walk RIGHT along Row 16 to Column 24
        (21, 16, 'Right'),
        (22, 16, 'Right'),
        (23, 16, 'Right'),
        (24, 16, 'Right'),
        # Walk UP Column 24 to Row 12
        (24, 15, 'Up'),
        (24, 14, 'Up'),
        (24, 13, 'Up'),
        (24, 12, 'Up'),
        # Walk LEFT along Row 12 to Column 15
        (23, 12, 'Left'),
        (22, 12, 'Left'),
        (21, 12, 'Left'),
        (20, 12, 'Left'),
        (19, 12, 'Left'),
        (18, 12, 'Left'),
        (17, 12, 'Left'),
        (16, 12, 'Left'),
        (15, 12, 'Left'),
        # Walk UP Column 15 to Row 11
        (15, 11, 'Up'),
    ]
    print("Walking to 2F East stairs...")
    for target in path_to_stairs_2f:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()
            
    print("Stepping UP to enter 2F East stairs and warp to 3F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)

print("Final position after script:", mgba.get_coordinates())
mgba.take_screenshot()
