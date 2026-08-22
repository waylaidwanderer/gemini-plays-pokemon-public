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

# Starting at (12, 12) on 1F West (State B)
pos = mgba.get_coordinates()
print("Starting go_to_2f_east_stairs from:", pos)

if pos['x'] == 12 and pos['y'] == 12:
    path = [
        # Walk UP Column 12 to Row 5
        (12, 11, 'Up'),
        (12, 10, 'Up'),
        (12, 9, 'Up'),
        (12, 8, 'Up'),
        (12, 7, 'Up'),
        (12, 6, 'Up'),
        (12, 5, 'Up'),
        # Walk RIGHT along Row 5 to Column 21
        (13, 5, 'Right'),
        (14, 5, 'Right'),
        (15, 5, 'Right'),
        (16, 5, 'Right'),
        (17, 5, 'Right'),
        (18, 5, 'Right'),
        (19, 5, 'Right'),
        (20, 5, 'Right'),
        (21, 5, 'Right'),
        # Walk UP Column 21 to Row 3
        (21, 4, 'Up'),
        (21, 3, 'Up'),
        # Walk RIGHT along Row 3 to Column 26
        (22, 3, 'Right'),
        (23, 3, 'Right'),
        (24, 3, 'Right'),
        (25, 3, 'Right'),
        (26, 3, 'Right'),
        # Walk DOWN Column 26 to Row 11
        (26, 4, 'Down'),
        (26, 5, 'Down'),
        (26, 6, 'Down'),
        (26, 7, 'Down'),
        (26, 8, 'Down'),
        (26, 9, 'Down'),
        (26, 10, 'Down'),
        (26, 11, 'Down'),
        # Walk LEFT along Row 11 to Column 18
        (25, 11, 'Left'),
        (24, 11, 'Left'),
        (23, 11, 'Left'),
        (22, 11, 'Left'),
        (21, 11, 'Left'),
        (20, 11, 'Left'),
        (19, 11, 'Left'),
        (18, 11, 'Left'),
        # Walk UP to stairs at (18, 10)
        (18, 10, 'Up'),
    ]
    
    print("Walking path to 1F East stairs...")
    for target in path:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()
            
    print("Stepping UP to enter 1F East stairs and go UP to 2F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)

print("Final coordinates after script:", mgba.get_coordinates())
mgba.take_screenshot()
