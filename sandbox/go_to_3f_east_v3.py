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

# We are at (26, 7) on 2F East in State B.
pos = mgba.get_coordinates()
print("Starting go_to_3f_east_v3 from:", pos)

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
    print("Walking to 2F East stairs...")
    for target in path_to_stairs:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach 2F East stairs at ({tx}, {ty})")
            exit()
            
    print("Stepping UP to enter 3F East stairs...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)

print("Final position after 2F East walk:", mgba.get_coordinates())
mgba.take_screenshot()
