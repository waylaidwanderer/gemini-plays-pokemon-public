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

# --- PART 2: WALK FROM 2F WEST (2, 11) TO 3F EAST LANDING (16, 11) ---

pos = mgba.get_coordinates()
print("Starting Mansion run Part 2 from 2F West:", pos)

if pos['x'] == 2 and pos['y'] == 11:
    path_to_stairs = [
        (3, 11, 'Right'),
        (4, 11, 'Right'),
        (5, 11, 'Right'),
        (6, 11, 'Right'),
        (7, 11, 'Right'),
        (7, 10, 'Up'),
    ]
    print("Step 1: Walking to 2F West stairs...")
    for target in path_to_stairs:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach 2F West stairs at ({tx}, {ty})")
            exit()
            
    time.sleep(2.0) # Wait for stairs transition

# We are on 1F West at (7, 10) in State B.
pos = mgba.get_coordinates()
if pos['x'] == 7 and pos['y'] == 10:
    path_to_1f_stairs = [
        (7, 11, 'Down'),
        (8, 11, 'Right'),
        (9, 11, 'Right'),
        (10, 11, 'Right'),
        (11, 11, 'Right'),
        (11, 10, 'Up'),
        (12, 10, 'Right'),
        (12, 9, 'Up'),
        (12, 8, 'Up'),
        (12, 7, 'Up'),
        (12, 6, 'Up'),
        (12, 5, 'Up'),
        (13, 5, 'Right'),
        (14, 5, 'Right'),
        (15, 5, 'Right'),
        (16, 5, 'Right'),
        (17, 5, 'Right'),
        (18, 5, 'Right'),
        (19, 5, 'Right'),
        (20, 5, 'Right'),
        (21, 5, 'Right'),
        (21, 4, 'Up'),
        (21, 3, 'Up'),
        (22, 3, 'Right'),
        (23, 3, 'Right'),
        (24, 3, 'Right'),
        (25, 3, 'Right'),
        (26, 3, 'Right'),
        (26, 4, 'Down'),
        (26, 5, 'Down'),
        (26, 6, 'Down'),
    ]
    print("Step 2: Crossing to 1F East stairs...")
    for target in path_to_1f_stairs:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach 1F East stairs at ({tx}, {ty})")
            exit()
            
    time.sleep(2.0) # Wait for stairs transition

# We are on 2F East at (26, 7) in State B.
pos = mgba.get_coordinates()
if pos['x'] == 26 and pos['y'] == 7:
    path_to_3f_stairs = [
        (26, 8, 'Down'),
        (26, 9, 'Down'),
        (26, 10, 'Down'),
        (26, 11, 'Down'),
        (25, 11, 'Left'),
        (24, 11, 'Left'),
        (23, 11, 'Left'),
        (22, 11, 'Left'),
        (21, 11, 'Left'),
        (20, 11, 'Left'),
        (19, 11, 'Left'),
        (18, 11, 'Left'),
        (17, 11, 'Left'),
        (16, 11, 'Left'),
        (15, 11, 'Left'),
    ]
    print("Step 3: Walking to 2F East stairs...")
    for target in path_to_3f_stairs:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach 2F East stairs at ({tx}, {ty})")
            exit()
            
    print("At (15, 11). Walking UP onto stairs to warp to 3F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0) # Wait for stairs transition

print("End of Part 2! Current position:", mgba.get_coordinates())
mgba.take_screenshot()
