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
    while attempts < 40:
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

# --- PART 1: WALK FROM (11, 12) TO 2F WEST SWITCH AND TOGGLE TO STATE B, GO TO 1F WEST ---

pos = mgba.get_coordinates()
print("Starting Mansion Part 1 from:", pos)

if pos['x'] == 11 and pos['y'] == 12:
    # Walk to Column 19
    path_to_east = [
        (12, 12, 'Right'),
        (13, 12, 'Right'),
        (14, 12, 'Right'),
        (15, 12, 'Right'),
        (16, 12, 'Right'),
        (17, 12, 'Right'),
        (18, 12, 'Right'),
        (19, 12, 'Right'),
    ]
    print("Walking to East side Column 19...")
    for target in path_to_east:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()

    # Walk UP Column 19 to Row 5
    path_up_19 = [
        (19, 11, 'Up'),
        (19, 10, 'Up'),
        (19, 9, 'Up'),
        (19, 8, 'Up'),
        (19, 7, 'Up'),
        (19, 6, 'Up'),
        (19, 5, 'Up'),
    ]
    print("Walking UP Column 19...")
    for target in path_up_19:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()

    # Walk LEFT to Column 14
    path_left_row5 = [
        (18, 5, 'Left'),
        (17, 5, 'Left'),
        (16, 5, 'Left'),
        (15, 5, 'Left'),
        (14, 5, 'Left'),
    ]
    print("Walking LEFT along Row 5...")
    for target in path_left_row5:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()

    # Walk UP to Row 4
    print("Walking UP to Row 4...")
    if not walk_step(14, 4, 'Up'):
        print("Failed to walk UP to Row 4")
        exit()

    # Walk LEFT along Row 4 to Column 6
    path_left_row4 = [
        (13, 4, 'Left'),
        (12, 4, 'Left'),
        (11, 4, 'Left'),
        (10, 4, 'Left'),
        (9, 4, 'Left'),
        (8, 4, 'Left'),
        (7, 4, 'Left'),
        (6, 4, 'Left'),
    ]
    print("Walking LEFT along Row 4...")
    for target in path_left_row4:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()

    # Enter Mansion safely
    print("Stepping UP to enter Mansion...")
    mgba.press_buttons(["Up"])
    time.sleep(3.0) # Wait for transition

    pos_inside = mgba.get_coordinates()
    print("Position after transition:", pos_inside)
    if pos_inside['x'] != 5 or pos_inside['y'] != 27:
        print("Failed to enter Mansion!")
        exit()

    # Walk UP immediately to clear exit warp
    print("Clearing exit warp...")
    for _ in range(4):
        mgba.press_buttons(["Up"])
        time.sleep(0.55)

# Inside Mansion 1F West, walk UP stairs to 2F West
pos = mgba.get_coordinates()
if pos['x'] == 5 and pos['y'] == 23:
    path_to_stairs = [
        (7, 23, 'Right'),
        (7, 10, 'Up'),
    ]
    print("Step 2: Going UP the stairs to 2F West...")
    for target in path_to_stairs:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach 2F West stairs at ({tx}, {ty})")
            exit()
            
    time.sleep(2.0) # Wait for stairs transition

# On 2F West, walk to 2F West switch and toggle to State B
pos = mgba.get_coordinates()
if pos['x'] == 7 and pos['y'] == 10:
    path_to_switch = [
        (7, 11, 'Down'),
        (2, 11, 'Left'),
        (2, 12, 'Down'),
    ]
    print("Step 3: Walking to 2F West switch...")
    for target in path_to_switch:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach switch at ({tx}, {ty})")
            exit()
            
    print("At (2, 12). Facing UP and toggling switch to State B...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    mgba.press_buttons(["A", "sleep 600", "A", "sleep 600", "B"])
    time.sleep(1.5)

# Go DOWN the stairs to 1F West (we land on 1F West at (7, 10) in State B)
pos = mgba.get_coordinates()
if pos['x'] == 2 and pos['y'] == 11:
    path_to_stairs = [
        (7, 11, 'Right'),
        (7, 10, 'Up'),
    ]
    print("Step 4: Going DOWN the stairs to 1F West...")
    for target in path_to_stairs:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach 1F West stairs at ({tx}, {ty})")
            exit()
            
    time.sleep(2.0) # Wait for stairs transition

print("Finished Mansion Part 1 successfully! Current position:", mgba.get_coordinates())
mgba.take_screenshot()
