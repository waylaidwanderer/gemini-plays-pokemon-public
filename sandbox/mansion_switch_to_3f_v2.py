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

def walk_to_local(tx, ty):
    # Safe simple walk_to for obstacle-free straight lines
    pos = mgba.get_coordinates()
    attempts = 0
    while (pos['x'] != tx or pos['y'] != ty) and attempts < 30:
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

# Currently at (24, 11) on 1F East inside the Mansion
pos = mgba.get_coordinates()
print("Starting mansion_switch_to_3f_v2 from:", pos)

if pos['x'] == 24 and pos['y'] == 11:
    print("--- STEP 1: GO TO 1F EAST STAIRS AT (26, 6) ---")
    path_to_stairs = [
        (25, 11, 'Right'),
        (26, 11, 'Right'),
        (26, 10, 'Up'),
        (26, 9, 'Up'),
        (26, 8, 'Up'),
        (26, 7, 'Up'),
        (26, 6, 'Up'),
    ]
    for target in path_to_stairs:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()
            
    print("Stepping UP to enter 1F East stairs and go UP to 2F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)

pos = mgba.get_coordinates()
print("Position on 2F East after climbing stairs:", pos)

if pos['x'] == 26 and pos['y'] == 7:
    print("--- STEP 2: TRYING TO CROSS 2F EAST TO WEST ---")
    # Walk to (24, 11) on 2F East
    if not walk_to_local(24, 11):
        print("Failed to reach (24, 11) on 2F East")
        exit()
        
    # We are at (24, 11) on 2F East.
    # Let's test Row 15 horizontal crossing
    print("Testing Row 15 horizontal crossing...")
    if walk_to_local(24, 15):
        print("Successfully reached (24, 15). Trying to walk LEFT to Column 15...")
        if walk_to_local(15, 15):
            print("Row 15 is OPEN! Successfully reached (15, 15)!")
            # Walk UP Column 15 to stairs at (15, 11)
            walk_to_local(15, 11)
            exit()
            
    # If Row 15 failed, we try Row 16
    print("Row 15 failed. Testing Row 16 horizontal crossing...")
    if walk_to_local(24, 16):
        print("Successfully reached (24, 16). Trying to walk LEFT to Column 15...")
        if walk_to_local(15, 16):
            print("Row 16 is OPEN! Successfully reached (15, 16)!")
            # Walk UP Column 15 to stairs at (15, 11)
            walk_to_local(15, 11)
            exit()
            
    # If Row 16 failed, we try Row 14
    print("Row 16 failed. Testing Row 14 horizontal crossing...")
    if walk_to_local(24, 14):
        print("Successfully reached (24, 14). Trying to walk LEFT to Column 15...")
        if walk_to_local(15, 14):
            print("Row 14 is OPEN! Successfully reached (15, 14)!")
            # Walk UP Column 15 to stairs at (15, 11)
            walk_to_local(15, 11)
            exit()

print("All horizontal rows failed to cross to Column 15 on 2F East in State B.")
mgba.take_screenshot()
