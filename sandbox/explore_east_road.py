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

# Start at (2, 15) on 1F West (State B)
pos = mgba.get_coordinates()
print("Starting explore_east_road from 1F West:", pos)

if pos['x'] == 2 and pos['y'] == 15:
    print("--- STEP 1: WALK TO ALTERNATE STAIRS AT (18, 10) ON 1F EAST ---")
    path = [
        # Walk UP Column 2 to Row 8
        (2, 14, 'Up'),
        (2, 13, 'Up'),
        (2, 12, 'Up'),
        (2, 11, 'Up'),
        (2, 10, 'Up'),
        (2, 9, 'Up'),
        (2, 8, 'Up'),
        # Walk RIGHT along Row 8 to Column 18
        (3, 8, 'Right'),
        (4, 8, 'Right'),
        (5, 8, 'Right'),
        (6, 8, 'Right'),
        (7, 8, 'Right'),
        (8, 8, 'Right'),
        (9, 8, 'Right'),
        (10, 8, 'Right'),
        (11, 8, 'Right'),
        (12, 8, 'Right'),
        (13, 8, 'Right'),
        (14, 8, 'Right'),
        (15, 8, 'Right'), # Through the open gate at (15, 8) in State B!
        (16, 8, 'Right'),
        (17, 8, 'Right'),
        (18, 8, 'Right'),
        # Walk DOWN Column 18 to Row 10
        (18, 9, 'Down'),
        (18, 10, 'Down'),
    ]
    
    for target in path:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()
            
    print("At (18, 10) on 1F East. Stepping UP to enter alternate stairs...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)

pos = mgba.get_coordinates()
print("Position on next floor after climbing alternate stairs:", pos)

# We should land on 2F East on the correct (West-Central) side!
# Let's see if we can find the stairs to 3F East and go UP!
if pos['x'] != 2: # Check if we successfully went up
    print("--- STEP 2: WALKING TO 3F EAST STAIRS ---")
    # Walk to (15, 11) on 2F East.
    # Since we landed at (18, 10) or (20, 16) or somewhere nearby on the West-Central side,
    # let's write a robust, direct path to the stairs at (15, 11) depending on our landing!
    # Let's print out our position and let the script handle it.
    pass

mgba.take_screenshot()
