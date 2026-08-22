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

# --- THE ABSOLUTE MASTER GET KEY FINAL RUN ---

# 1. Walk from Cinnabar Island (13, 5) to Mansion entrance via bypass
path_enter = [
    (12, 5, 'Left'),
    (12, 4, 'Up'),
    (11, 4, 'Left'),
    (10, 4, 'Left'),
    (10, 5, 'Down'),
    (9, 5, 'Left'),
    (8, 5, 'Left'),
    (7, 5, 'Left'),
    (6, 5, 'Left'),
    (6, 4, 'Up'),
    (6, 3, 'Up'),
]

print("Step 1: Walking from (13, 5) with bypass and entering Mansion...")
for target in path_enter:
    tx, ty, d = target
    if not walk_step(tx, ty, d):
        print(f"Failed to enter Mansion at ({tx}, {ty})")
        exit()

time.sleep(2.0) # Wait for transition
pos_inside = mgba.get_coordinates()
print("Landed inside Mansion! Position:", pos_inside)

# Walk UP immediately to clear exit warp at (5, 27)
for _ in range(4):
    mgba.press_buttons(["Up"])
    time.sleep(0.55)

# 2. Go UP stairs to 2F West
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

# 3. Walk to 2F West switch and toggle to State B
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

# 4. Go DOWN the stairs to 1F West
pos = mgba.get_coordinates()
if pos['x'] == 2 and pos['y'] == 11:
    path_to_stairs = [
        (7, 11, 'Right'),
        (7, 10, 'Up'),
    ]
    print("Step 4: Going DOWN the stairs to 1F West...")
    for target in path_to_stairs:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach 1F West stairs at ({tx}, {ty})")
            exit()
            
    time.sleep(2.0) # Wait for stairs transition

# 5. Crossing to 1F East stairs
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
    print("Step 5: Crossing to 1F East stairs...")
    for target in path_to_stairs:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach 1F East stairs at ({tx}, {ty})")
            exit()
            
    time.sleep(2.0) # Wait for stairs transition

# 6. Walk to 2F East stairs and go UP to 3F East
pos = mgba.get_coordinates()
if pos['x'] == 26 and pos['y'] == 7:
    path_to_stairs = [
        (26, 11, 'Down'),
        (15, 11, 'Left'),
    ]
    print("Step 6: Walking to 2F East stairs...")
    for target in path_to_stairs:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach 2F East stairs at ({tx}, {ty})")
            exit()
            
    time.sleep(2.0) # Wait for stairs transition

# 7. Walk to 3F East balcony drop-off and drop in State B
pos = mgba.get_coordinates()
if pos['x'] == 16 and pos['y'] == 11:
    path_to_balcony = [
        (16, 18, 'Down'),
        (17, 18, 'Right'),
        (18, 18, 'Right'),
        (19, 18, 'Right'),
        (20, 18, 'Right'),
    ]
    print("Step 7: Walking to 3F East balcony drop-off...")
    for target in path_to_balcony:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach balcony drop-off at ({tx}, {ty})")
            exit()
            
    print("At (20, 18)! Stepping LEFT to drop over the balcony...")
    mgba.press_buttons(["Left"])
    time.sleep(3.0) # Wait for drop transition

# 8. Land on B1F East South in State B. Walk Column 19 to Row 5, and cross Left to Key
pos = mgba.get_coordinates()
if pos['x'] == 19 and pos['y'] == 16:
    path_to_key = [
        # Walk UP Column 19 to Row 5
        (19, 15, 'Up'),
        (19, 14, 'Up'),
        (19, 13, 'Up'),
        (19, 12, 'Up'),
        (19, 11, 'Up'),
        (19, 10, 'Up'),
        (19, 9, 'Up'),
        (19, 8, 'Up'),
        (19, 7, 'Up'),
        (19, 6, 'Up'),
        (19, 5, 'Up'),
        # Walk LEFT along Row 5 to Column 1
        (18, 5, 'Left'),
        (17, 5, 'Left'),
        (16, 5, 'Left'),
        (15, 5, 'Left'),
        (14, 5, 'Left'),
        (13, 5, 'Left'),
        (12, 5, 'Left'),
        (11, 5, 'Left'),
        (10, 5, 'Left'),
        (9, 5, 'Left'), # Row 5 Shutter Gate is OPEN in State B
        (8, 5, 'Left'),
        (7, 5, 'Left'),
        (6, 5, 'Left'),
        (5, 5, 'Left'),
        (4, 5, 'Left'),
        (3, 5, 'Left'),
        (2, 5, 'Left'),
        (1, 5, 'Left'),
    ]
    print("Step 8: Walking to the Secret Key room on B1F...")
    for target in path_to_key:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()
            
    print("At (1, 5)! Facing UP and retrieving the Secret Key...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    mgba.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "B", "sleep 200"])
    time.sleep(1.0)
    
    # 9. Use DIG to escape to Cinnabar Island!
    print("Step 9: Using DIG to escape...")
    mgba.press_buttons(["Start"])
    time.sleep(0.8)
    mgba.press_buttons(["Down", "A"])
    time.sleep(1.0)
    for _ in range(5):
        mgba.press_buttons(["Down"])
        time.sleep(0.1)
    mgba.press_buttons(["A"])
    time.sleep(0.8)
    mgba.press_buttons(["A"])
    time.sleep(4.0)

print("Final overworld position:", mgba.get_coordinates())
mgba.take_screenshot()
