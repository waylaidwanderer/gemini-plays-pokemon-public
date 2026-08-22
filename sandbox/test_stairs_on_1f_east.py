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

# Starting at (2, 11) on 2F West inside the Mansion
pos = mgba.get_coordinates()
print("Starting test_stairs_on_1f_east from:", pos)

if pos['x'] == 2 and pos['y'] == 11:
    # 1. Face UP and press A to toggle switch to State B
    print("Facing UP and toggling switch to State B...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    mgba.press_buttons(["A", "sleep 600", "A", "sleep 600", "B"])
    time.sleep(1.5)

    # 2. Walk to 2F West stairs and go DOWN to 1F West
    path_to_stairs = [
        (7, 11, 'Right'),
        (7, 10, 'Up'),
    ]
    print("Going DOWN to 1F West...")
    for target in path_to_stairs:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach 1F West stairs at ({tx}, {ty})")
            exit()
            
    time.sleep(2.0) # Wait for stairs transition

# We land on 1F West at (7, 10) in State B. Cross to 1F East open gate
pos = mgba.get_coordinates()
if pos['x'] == 7 and pos['y'] == 10:
    path_cross = [
        (7, 11, 'Down'),
        (11, 11, 'Right'),
        (11, 10, 'Up'),
        (12, 10, 'Right'),
        (12, 8, 'Up'),
        (15, 8, 'Right'), # Shutter gate (15, 8) is OPEN in State B!
        (16, 8, 'Right'), # Cross to 1F East!
    ]
    print("Crossing 1F West to 1F East via open gate...")
    for target in path_cross:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()

# Now on 1F East at (16, 8). Let's walk to Column 15, and check Row 11 for stairs!
pos = mgba.get_coordinates()
if pos['x'] == 16 and pos['y'] == 8:
    path_to_potential_stairs = [
        (15, 8, 'Left'),
        (15, 9, 'Down'),
        (15, 10, 'Down'),
        (15, 11, 'Down'),
    ]
    print("Walking to potential 1F East stairs at (15, 11)...")
    for target in path_to_potential_stairs:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()
            
    # Step DOWN or UP to see if it triggers a warp!
    print("At (15, 11). Stepping DOWN to see if it triggers stairs warp...")
    mgba.press_buttons(["Down"])
    time.sleep(2.0)
    
print("Coordinates after 1F East stairs check:", mgba.get_coordinates())
mgba.take_screenshot()
