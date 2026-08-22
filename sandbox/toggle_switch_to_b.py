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
            print(f"Bumped at {pos} going {d} towards ({tx}, {ty}). Handling battle...")
            handle_battle()
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
        else:
            if new_pos['x'] == tx and new_pos['y'] == ty:
                return True
        attempts += 1
    return False

# Starting at (10, 7) on 2F West
pos = mgba.get_coordinates()
print("Starting safe Switch B toggle from 2F West:", pos)

if pos['x'] == 10 and pos['y'] == 7:
    print("--- STEP 1: RETURNING TO COLUMN 12 ---")
    path_to_col12 = [
        (10, 6, 'Up'),
        (11, 6, 'Right'),
        (12, 6, 'Right'),
    ]
    for target in path_to_col12:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()

pos = mgba.get_coordinates()
if pos['x'] == 12 and pos['y'] == 6:
    print("--- STEP 2: WALKING TO SWITCH BYPASSING PIT AND WALLS ---")
    path_2f = [
        # Walk DOWN Column 12 to Row 11
        (12, 7, 'Down'),
        (12, 8, 'Down'),
        (12, 9, 'Down'),
        (12, 10, 'Down'),
        (12, 11, 'Down'),
        # Walk LEFT along Row 11 to Column 3 (bypassing stairs and pit)
        (11, 11, 'Left'),
        (10, 11, 'Left'),
        (9, 11, 'Left'),
        (8, 11, 'Left'),
        (7, 11, 'Left'),
        (6, 11, 'Left'),
        (5, 11, 'Left'),
        (4, 11, 'Left'),
        (3, 11, 'Left'),
        # Walk DOWN Column 3 to Row 12
        (3, 12, 'Down'),
        # Walk LEFT to Column 2 on Row 12 (below the pit)
        (2, 12, 'Left'),
    ]
    for target in path_2f:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed on 2F West at ({tx}, {ty})")
            exit()
            
    print("At (2, 12) on 2F West. Facing UP and toggling switch to State B...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    # Interact with switch
    mgba.press_buttons(["A", "sleep 300", "A", "sleep 500", "B"])
    time.sleep(1.5)

print("Final position after toggle script:", mgba.get_coordinates())
mgba.take_screenshot()
