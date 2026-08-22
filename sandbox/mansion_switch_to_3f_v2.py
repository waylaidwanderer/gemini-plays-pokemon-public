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

# Starting at (28, 21) on 1F East inside the Mansion
pos = mgba.get_coordinates()
print("Starting mansion_switch_to_3f_v2 from:", pos)

if pos['x'] == 28 and pos['y'] == 21:
    path_to_stairs = [
        # Walk LEFT along Row 21 to Column 25
        (27, 21, 'Left'),
        (26, 21, 'Left'),
        (25, 21, 'Left'),
        # Walk UP Column 25 to Row 11
        (25, 20, 'Up'),
        (25, 19, 'Up'),
        (25, 18, 'Up'),
        (25, 17, 'Up'),
        (25, 16, 'Up'),
        (25, 15, 'Up'),
        (25, 14, 'Up'),
        (25, 13, 'Up'),
        (25, 12, 'Up'),
        (25, 11, 'Up'),
        # Walk LEFT along Row 11 to Column 18
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
    print("Walking to 1F East stairs...")
    for target in path_to_stairs:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()
            
    print("Stepping UP to enter 1F East stairs and go UP to 2F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)

print("Final position after climbing stairs:", mgba.get_coordinates())
mgba.take_screenshot()
