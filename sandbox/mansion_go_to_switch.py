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

# Starting at (26, 5) on 1F East inside the Mansion (State A)
pos = mgba.get_coordinates()
print("Starting mansion_go_to_switch from:", pos)

if pos['x'] == 26 and pos['y'] == 5:
    path_to_1f_west = [
        # Walk LEFT along Row 5 all the way to Column 12
        (25, 5, 'Left'),
        (24, 5, 'Left'),
        (23, 5, 'Left'),
        (22, 5, 'Left'),
        (21, 5, 'Left'),
        (20, 5, 'Left'),
        (19, 5, 'Left'),
        (18, 5, 'Left'),
        (17, 5, 'Left'),
        (16, 5, 'Left'),
        (15, 5, 'Left'),
        (14, 5, 'Left'),
        (13, 5, 'Left'),
        (12, 5, 'Left'),
    ]
    print("Walking LEFT across Row 5 on 1F East to 1F West...")
    for target in path_to_1f_west:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()

# We are on 1F West at (12, 5). Walk DOWN Column 12 to Row 10, and to stairs at (7, 10)
pos = mgba.get_coordinates()
if pos['x'] == 12 and pos['y'] == 5:
    path_to_stairs = [
        (12, 6, 'Down'),
        (12, 7, 'Down'),
        (12, 8, 'Down'),
        (12, 9, 'Down'),
        (12, 10, 'Down'),
        # Walk LEFT to Column 7
        (11, 10, 'Left'),
        (10, 10, 'Left'),
        (9, 10, 'Left'),
        (8, 10, 'Left'),
        (7, 10, 'Left'),
    ]
    print("Walking to 1F West stairs...")
    for target in path_to_stairs:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()
            
    print("Stepping UP to enter 1F West stairs and warp to 2F West...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)

# We land on 2F West at (7, 10). Walk to switch at (2, 11) and toggle to State B
pos = mgba.get_coordinates()
if pos['x'] == 7 and pos['y'] == 10:
    path_to_switch = [
        (7, 11, 'Down'),
        (2, 11, 'Left'),
    ]
    print("Walking to 2F West switch...")
    for target in path_to_switch:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach switch at ({tx}, {ty})")
            exit()
            
    print("At (2, 11). Facing UP and toggling switch to State B...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    mgba.press_buttons(["A", "sleep 600", "A", "sleep 600", "B"])
    time.sleep(1.5)

print("Finished mansion_go_to_switch successfully! Current position:", mgba.get_coordinates())
mgba.take_screenshot()
