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

# Starting at (27, 26) on 1F East inside the Mansion
pos = mgba.get_coordinates()
print("Starting mansion_go_to_switch from:", pos)

if pos['x'] == 27 and pos['y'] == 26:
    path_to_stairs = [
        # Walk UP Column 27 to Row 11
        (27, 25, 'Up'),
        (27, 24, 'Up'),
        (27, 23, 'Up'),
        (27, 22, 'Up'),
        (27, 21, 'Up'),
        (27, 20, 'Up'),
        (27, 19, 'Up'),
        (27, 18, 'Up'),
        (27, 17, 'Up'),
        (27, 16, 'Up'),
        (27, 15, 'Up'),
        (27, 14, 'Up'),
        (27, 13, 'Up'),
        (27, 12, 'Up'),
        (27, 11, 'Up'),
        # Walk LEFT along Row 11 to Column 18
        (26, 11, 'Left'),
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
    print("Walking to 1F East stairs...")
    for target in path_to_stairs:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach 1F East stairs at ({tx}, {ty})")
            exit()
            
    print("Stepping UP to enter 1F East stairs and go UP to 2F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)

print("Final position after climbing stairs:", mgba.get_coordinates())
mgba.take_screenshot()
