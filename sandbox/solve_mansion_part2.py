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

# --- PART 2: GO DOWN TO 1F WEST, CROSS TO 2F EAST, AND GO UP TO 3F EAST ---

print("Step 1: Fleeing wild Muk battle...")
handle_battle()
time.sleep(1.5)

pos = mgba.get_coordinates()
print("Position after fleeing battle:", pos)

# A. We are standing at (2, 12) on 2F West in State B
if pos['x'] == 2 and pos['y'] == 12:
    path_to_stairs = [
        (2, 11, 'Up'),
        (7, 11, 'Right'),
        (7, 10, 'Up'),
    ]
    print("Step 2: Going DOWN the stairs to 1F West...")
    for target in path_to_stairs:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach 1F West stairs at ({tx}, {ty})")
            exit()
            
    time.sleep(2.0) # Wait for stairs transition

# B. We land on 1F West at (7, 10) in State B. Cross to 1F East stairs
pos = mgba.get_coordinates()
if pos['x'] == 7 and pos['y'] == 10:
    path_to_stairs = [
        (7, 11, 'Down'),
        (11, 11, 'Right'),
        (11, 10, 'Up'),
        (12, 10, 'Right'),
        (12, 5, 'Up'),
        (21, 5, 'Right'),
        (21, 3, 'Up'),
        (26, 3, 'Right'),
        (26, 6, 'Down'),
    ]
    print("Step 3: Crossing 1F to East stairs...")
    for target in path_to_stairs:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach 1F East stairs at ({tx}, {ty})")
            exit()
            
    time.sleep(2.0) # Wait for stairs transition

# C. We land on 2F East at (26, 7) in State B. Walk to 2F East stairs (15, 11) using open gate
pos = mgba.get_coordinates()
if pos['x'] == 26 and pos['y'] == 7:
    path_to_stairs = [
        (25, 7, 'Left'),
        (24, 7, 'Left'),
        (24, 8, 'Down'),
        (24, 9, 'Down'),
        (24, 10, 'Down'),
        (24, 11, 'Down'),
        (24, 12, 'Down'),
        (24, 13, 'Down'),
        (24, 14, 'Down'),
        (24, 15, 'Down'),
        (24, 16, 'Down'),
        (23, 16, 'Left'),
        (22, 16, 'Left'),
        (21, 16, 'Left'),
        (20, 16, 'Left'),
        (20, 17, 'Down'),
        (20, 18, 'Down'),
        # Row 18 is open green grass
        (19, 18, 'Left'),
        (18, 18, 'Left'),
        (17, 18, 'Left'),
        (16, 18, 'Left'),
        (15, 18, 'Left'),
        # Column 15 is open vertically
        (15, 17, 'Up'),
        (15, 16, 'Up'),
        (15, 15, 'Up'),
        (15, 14, 'Up'),
        (15, 13, 'Up'),
        (15, 12, 'Up'),
        (15, 11, 'Up'),
    ]
    print("Step 4: Walking to 2F East stairs...")
    for target in path_to_stairs:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach 2F East stairs at ({tx}, {ty})")
            exit()
            
    print("Stepping UP to enter 3F East stairs...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)

print("Finished Mansion Part 2 successfully! Current position:", mgba.get_coordinates())
mgba.take_screenshot()
