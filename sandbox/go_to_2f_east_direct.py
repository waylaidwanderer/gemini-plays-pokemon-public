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

# Starting at (23, 11) on 1F East inside the Mansion
pos = mgba.get_coordinates()
print("Starting go_to_2f_east_direct from:", pos)

if pos['x'] == 23 and pos['y'] == 11:
    path = [
        # Walk RIGHT to Column 24 on Row 11
        (24, 11, 'Right'),
        # Walk DOWN Column 24 to Row 15
        (24, 12, 'Down'),
        (24, 13, 'Down'),
        (24, 14, 'Down'),
        (24, 15, 'Down'),
        # Walk LEFT along Row 15 to Column 18
        (23, 15, 'Left'),
        (22, 15, 'Left'),
        (21, 15, 'Left'),
        (20, 15, 'Left'),
        (19, 15, 'Left'),
        (18, 15, 'Left'),
        # Walk UP Column 18 to Row 10
        (18, 14, 'Up'),
        (18, 13, 'Up'),
        (18, 12, 'Up'),
        (18, 11, 'Up'),
        (18, 10, 'Up'),
    ]
    
    print("Walking path to 1F East stairs...")
    for target in path:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()
            
    print("Stepping UP to enter 1F East stairs...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)

print("Final position after 1F East stairs warp:", mgba.get_coordinates())
mgba.take_screenshot()
