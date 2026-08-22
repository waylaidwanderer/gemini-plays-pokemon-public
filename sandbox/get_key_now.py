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

# Path to the balcony drop-off at (24, 14) from (24, 18) in State A
path_to_switch = [
    # Walk UP Column 24 to Row 3
    (24, 17, 'Up'),
    (24, 16, 'Up'),
    (24, 15, 'Up'),
    (24, 14, 'Up'),
    (24, 13, 'Up'),
    (24, 12, 'Up'),
    (24, 11, 'Up'),
    (24, 10, 'Up'),
    (24, 9, 'Up'),
    (24, 8, 'Up'),
    (24, 7, 'Up'),
    (24, 6, 'Up'),
    (24, 5, 'Up'),
    (24, 4, 'Up'),
    (24, 3, 'Up'),
    # Walk LEFT to Column 12 on Row 3
    (23, 3, 'Left'),
    (22, 3, 'Left'),
    (21, 3, 'Left'),
    (20, 3, 'Left'),
    (19, 3, 'Left'),
    (18, 3, 'Left'),
    (17, 3, 'Left'),
    (16, 3, 'Left'),
    (15, 3, 'Left'),
    (14, 3, 'Left'),
    (13, 3, 'Left'),
    (12, 3, 'Left'),
    # Walk DOWN Column 12 to Row 11
    (12, 4, 'Down'),
    (12, 5, 'Down'),
    (12, 6, 'Down'),
    (12, 7, 'Down'),
    (12, 8, 'Down'),
    (12, 9, 'Down'),
    (12, 10, 'Down'),
    (12, 11, 'Down'),
    # Walk LEFT to Column 11
    (11, 11, 'Left'),
]

print("Executing walk to 3F West switch in State A...")
success = True
for target in path_to_switch:
    tx, ty, d = target
    if not walk_step(tx, ty, d):
        print(f"Failed to reach target ({tx}, {ty})")
        success = False
        break

if success:
    print("Reached (11, 11)! Facing RIGHT and toggling switch to State B...")
    mgba.press_buttons(["Right"])
    time.sleep(0.5)
    mgba.press_buttons(["A", "sleep 600", "A", "sleep 600", "B"])
    time.sleep(1.5)
    print("Toggled switch to State B! Current position:", mgba.get_coordinates())
    
    # 2. Walk to the balcony drop-off at (20, 18) in State B
    path_to_drop = [
        # Walk RIGHT along Row 11 to Column 20
        (12, 11, 'Right'),
        (13, 11, 'Right'),
        (14, 11, 'Right'),
        (15, 11, 'Right'),
        (16, 11, 'Right'),
        (17, 11, 'Right'),
        (18, 11, 'Right'),
        (19, 11, 'Right'),
        (20, 11, 'Right'),
        # Walk DOWN Column 20 to Row 18
        (20, 12, 'Down'),
        (20, 13, 'Down'),
        (20, 14, 'Down'),
        (20, 15, 'Down'),
        (20, 16, 'Down'),
        (20, 17, 'Down'),
        (20, 18, 'Down'),
    ]
    
    print("Walking to the State B balcony drop-off...")
    for target in path_to_drop:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target ({tx}, {ty})")
            success = False
            break

if success:
    print("At (20, 18)! Stepping LEFT to drop over the balcony...")
    mgba.press_buttons(["Left"])
    time.sleep(3.0) # Wait for drop transition
    print("Landed on B1F! Current position:", mgba.get_coordinates())
    mgba.take_screenshot()
