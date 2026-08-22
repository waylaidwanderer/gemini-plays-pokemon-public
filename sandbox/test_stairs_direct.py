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

# Path on 2F East:
# From (26, 7) down Column 26 to Row 11, then Left along Row 11 to (15, 11)
path_2f_east = [
    (26, 8, 'Down'),
    (26, 9, 'Down'),
    (26, 10, 'Down'),
    (26, 11, 'Down'),
    (25, 11, 'Left'),
    (24, 11, 'Left'),
    (23, 11, 'Left'),
    (22, 11, 'Left'),
    (21, 11, 'Left'),
    (20, 11, 'Left'),
    (19, 11, 'Left'),
    (18, 11, 'Left'),
    (17, 11, 'Left'),
    (16, 11, 'Left'),
    (15, 11, 'Left'),
]

print("Walking to the 2F East stairs in State B...")
success = True
for target in path_2f_east:
    tx, ty, d = target
    if not walk_step(tx, ty, d):
        print(f"Failed to reach target ({tx}, {ty})")
        success = False
        break

if success:
    print("At 2F East stairs! Walking UP onto stairs at (15, 11) to warp to 3F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)
    print("Position on 3F East:", mgba.get_coordinates())
    mgba.take_screenshot()
