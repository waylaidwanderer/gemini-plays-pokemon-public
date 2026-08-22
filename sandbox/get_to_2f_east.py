import mgba
import time

def walk_step(tx, ty, direction):
    attempts = 0
    while attempts < 15:
        pos = mgba.get_coordinates()
        if pos['x'] == tx and pos['y'] == ty:
            return True
            
        mgba.press_buttons([direction])
        time.sleep(0.55)
        new_pos = mgba.get_coordinates()
        
        if new_pos == pos:
            # We bumped! Let's just return False so the script stops and we can see what happened.
            print(f"Bumped at {pos} going {direction} towards ({tx}, {ty})")
            return False
        else:
            if new_pos['x'] == tx and new_pos['y'] == ty:
                return True
        attempts += 1
    return False

# Starting at (10, 7) on 1F West
pos = mgba.get_coordinates()
print("Starting definitive 1F East alternate stairs run from:", pos)

if pos['x'] == 10 and pos['y'] == 7:
    path = [
        # Walk UP to Row 5
        (10, 6, 'Up'),
        (10, 5, 'Up'),
        # Walk RIGHT along Row 5 to Column 21
        (11, 5, 'Right'),
        (12, 5, 'Right'),
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
        # Walk RIGHT along Row 3 to Column 26 (crossing Column 22)
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
        # Walk UP onto stairs at (18, 10)
        (18, 10, 'Up'),
    ]
    
    for target in path:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()
            
    print("At (18, 10) on 1F East alternate stairs. Stepping UP to go to 2F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.5)

print("Final position of 1F script:", mgba.get_coordinates())
mgba.take_screenshot()
