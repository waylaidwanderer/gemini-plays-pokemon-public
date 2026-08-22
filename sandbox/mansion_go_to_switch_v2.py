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

def walk_to_local(tx, ty):
    pos = mgba.get_coordinates()
    attempts = 0
    while (pos['x'] != tx or pos['y'] != ty) and attempts < 40:
        dx = tx - pos['x']
        dy = ty - pos['y']
        if dx < 0: d = "Left"
        elif dx > 0: d = "Right"
        elif dy < 0: d = "Up"
        else: d = "Down"
        
        pos_before = pos
        mgba.press_buttons([d])
        time.sleep(0.55)
        pos = mgba.get_coordinates()
        if pos == pos_before:
            handle_battle()
            pos = mgba.get_coordinates()
        attempts += 1
    return pos['x'] == tx and pos['y'] == ty

# Start at (21, 6) on 2F East (State B)
pos = mgba.get_coordinates()
print("Starting mansion_go_to_switch_v2 from:", pos)

if pos['x'] == 21 and pos['y'] == 6:
    print("--- STEP 1: GO DOWN STAIRS TO 1F EAST ---")
    path_to_stairs = [
        (22, 6, 'Right'),
        (23, 6, 'Right'),
        (24, 6, 'Right'),
        (25, 6, 'Right'),
        (26, 6, 'Right'),
        (26, 7, 'Down'),
    ]
    for target in path_to_stairs:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()
            
    print("Stepping DOWN to enter 2F East stairs and go DOWN to 1F East...")
    mgba.press_buttons(["Down"])
    time.sleep(2.0)

# We land on 1F East (State B). Let's check coordinates.
pos = mgba.get_coordinates()
print("Position on 1F East after descending:", pos)

# Typically we land at (26, 7) or (26, 6).
if pos['x'] == 26:
    print("--- STEP 2: WALKING TO 1F EAST (WEST-CENTRAL) STAIRS ---")
    path_to_stairs_1f = [
        (26, 11, 'Down'),
        (25, 11, 'Left'),
        (25, 21, 'Down'),
        (24, 21, 'Left'),
        (23, 21, 'Left'),
        (22, 21, 'Left'),
        (21, 21, 'Left'),
        (20, 21, 'Left'),
        (19, 21, 'Left'),
        (18, 21, 'Left'),
        (17, 21, 'Left'),
        (16, 21, 'Left'),
        (15, 21, 'Left'),
        (14, 21, 'Left'),
        (13, 21, 'Left'),
        (12, 21, 'Left'),
        (12, 11, 'Up'),
        (13, 11, 'Right'),
        (14, 11, 'Right'),
        (15, 11, 'Right'),
        (16, 11, 'Right'),
        (17, 11, 'Right'),
        (18, 11, 'Right'),
        (18, 10, 'Up'),
    ]
    for target in path_to_stairs_1f:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()
            
    print("Stepping UP to enter 1F East stairs and go UP to 2F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)

pos = mgba.get_coordinates()
print("Position on 2F East after climbing stairs:", pos)
mgba.take_screenshot()
