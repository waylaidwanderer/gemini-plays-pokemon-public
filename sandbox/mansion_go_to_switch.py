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

# Starting at (23, 10) on 1F East inside the Mansion (State A)
pos = mgba.get_coordinates()
print("Starting mansion_go_to_switch from:", pos)

if pos['x'] == 23 and pos['y'] == 10:
    path = [
        # Walk RIGHT to Column 24
        (24, 10, 'Right'),
        # Walk DOWN Column 24 to Row 15
        (24, 11, 'Down'),
        (24, 12, 'Down'),
        (24, 13, 'Down'),
        (24, 14, 'Down'),
        (24, 15, 'Down'),
        # Walk LEFT along Row 15 to Column 12
        (23, 15, 'Left'),
        (22, 15, 'Left'),
        (21, 15, 'Left'),
        (20, 15, 'Left'),
        (19, 15, 'Left'),
        (18, 15, 'Left'),
        (17, 15, 'Left'),
        (16, 15, 'Left'),
        (15, 15, 'Left'),
        (14, 15, 'Left'),
        (13, 15, 'Left'),
        (12, 15, 'Left'),
        # Walk UP Column 12 to Row 10
        (12, 14, 'Up'),
        (12, 13, 'Up'),
        (12, 12, 'Up'),
        (12, 11, 'Up'),
        (12, 10, 'Up'),
        # Walk LEFT to Column 7
        (11, 10, 'Left'),
        (10, 10, 'Left'),
        (9, 10, 'Left'),
        (8, 10, 'Left'),
        (7, 10, 'Left'),
    ]
    
    print("Walking path to 1F West stairs...")
    for target in path:
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

print("Final position:", mgba.get_coordinates())
mgba.take_screenshot()
