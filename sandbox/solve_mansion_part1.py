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

# --- PART 1 (CONTINUED): WALK FROM (18, 8) TO 2F WEST SWITCH AND TOGGLE TO STATE B ---

pos = mgba.get_coordinates()
print("Starting Mansion run Part 1 from:", pos)

if pos['x'] == 18 and pos['y'] == 8:
    path_enter = [
        (18, 7, 'Up'), # Walk UP Column 18 to Row 4
        (18, 6, 'Up'),
        (18, 5, 'Up'),
        (18, 4, 'Up'),
        (17, 4, 'Left'), # Walk LEFT along Row 4 to Column 6
        (16, 4, 'Left'),
        (15, 4, 'Left'),
        (14, 4, 'Left'),
        (13, 4, 'Left'),
        (12, 4, 'Left'),
        (11, 4, 'Left'),
        (10, 4, 'Left'),
        (9, 4, 'Left'),
        (8, 4, 'Left'),
        (7, 4, 'Left'),
        (6, 4, 'Left'),
        (6, 3, 'Up'), # Enter Mansion
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
    
    # Walk UP immediately to clear exit warp at (5, 27)
    mgba.press_buttons(["Up"])
    time.sleep(0.55)
    mgba.press_buttons(["Up"])
    time.sleep(0.55)
    mgba.press_buttons(["Up"])
    time.sleep(0.55)
    mgba.press_buttons(["Up"])
    time.sleep(0.55)
    
# We are inside Mansion 1F West at (5, 23) in State A.
pos = mgba.get_coordinates()
if pos['x'] == 5 and pos['y'] == 23:
    path_to_stairs = [
        (7, 23, 'Right'),
        (7, 10, 'Down'),
    ]
    print("Step 2: Going UP the stairs to 2F West...")
    for target in path_to_stairs:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach 2F West stairs at ({tx}, {ty})")
            exit()
            
    time.sleep(2.0) # Wait for stairs transition

# We are on 2F West at (7, 10) in State A.
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

print("End of Part 1! Current position:", mgba.get_coordinates())
mgba.take_screenshot()
