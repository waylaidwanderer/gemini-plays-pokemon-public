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

# Starting outside on Cinnabar Island at (15, 12) (State A)
pos = mgba.get_coordinates()
print("Starting definitive State A Mansion Part 1 from outside (15, 12):", pos)

if pos['x'] == 15 and pos['y'] == 12:
    path_enter = [
        # Walk LEFT along Row 12 to Column 5 (completely safe edge)
        (14, 12, 'Left'),
        (13, 12, 'Left'),
        (12, 12, 'Left'),
        (11, 12, 'Left'),
        (10, 12, 'Left'),
        (9, 12, 'Left'),
        (8, 12, 'Left'),
        (7, 12, 'Left'),
        (6, 12, 'Left'),
        (5, 12, 'Left'),
        # Walk UP Column 5 to Row 4
        (5, 11, 'Up'),
        (5, 10, 'Up'),
        (5, 9, 'Up'),
        (5, 8, 'Up'),
        (5, 7, 'Up'),
        (5, 6, 'Up'),
        (5, 5, 'Up'),
        (5, 4, 'Up'),
        # Walk RIGHT along Row 4 to Column 6
        (6, 4, 'Right'),
        # Step UP to enter Mansion
        (6, 3, 'Up'),
    ]
    print("Step 1: Entering the Mansion...")
    for target in path_enter:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to enter Mansion at ({tx}, {ty})")
            exit()
            
    time.sleep(2.0) # Wait for transition
    pos_inside = mgba.get_coordinates()
    print("Landed inside Mansion! Position:", pos_inside)
    
    # Walk UP immediately to clear exit warp
    mgba.press_buttons(["Up"])
    time.sleep(0.55)
    mgba.press_buttons(["Up"])
    time.sleep(0.55)
    mgba.press_buttons(["Up"])
    time.sleep(0.55)
    mgba.press_buttons(["Up"])
    time.sleep(0.55)
    
# Inside Mansion 1F West at (5, 23) in State A.
pos = mgba.get_coordinates()
if pos['x'] == 5 and pos['y'] == 23:
    path_to_stairs = [
        (7, 23, 'Right'),
        (7, 11, 'Down'),
        # Since we are in State A, the Row 11 gate is open!
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
    print("Step 2: Walking to 1F East alternate stairs...")
    for target in path_to_stairs:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach stairs at ({tx}, {ty})")
            exit()
            
    print("Stepping UP to enter alternate stairs and go UP to 2F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)

pos = mgba.get_coordinates()
print("Final position after climbing stairs (expected 22, 7 on 2F East):", pos)
mgba.take_screenshot()
