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

# Flee from Ponyta battle
print("Fleeing from wild Ponyta battle...")
handle_battle()
time.sleep(1.5)

pos = mgba.get_coordinates()
print("Position after fleeing battle:", pos)

# Walk from 1F East (23, 11) to 1F West stairs (7, 10) via Row 3
if pos['x'] == 23 and pos['y'] == 11:
    path = [
        # Walk RIGHT to Column 26
        (24, 11, 'Right'),
        (25, 11, 'Right'),
        (26, 11, 'Right'),
        # Walk UP Column 26 to Row 3
        (26, 10, 'Up'),
        (26, 9, 'Up'),
        (26, 8, 'Up'),
        (26, 7, 'Up'),
        (26, 6, 'Up'),
        (26, 5, 'Up'),
        (26, 4, 'Up'),
        (26, 3, 'Up'),
        # Walk LEFT along Row 3 to Column 21
        (25, 3, 'Left'),
        (24, 3, 'Left'),
        (23, 3, 'Left'),
        (22, 3, 'Left'),
        (21, 3, 'Left'),
        # Walk DOWN Column 21 to Row 5
        (21, 4, 'Down'),
        (21, 5, 'Down'),
        # Walk LEFT along Row 5 to Column 12
        (20, 5, 'Left'),
        (19, 5, 'Left'),
        (18, 5, 'Left'),
        (17, 5, 'Left'),
        (16, 5, 'Left'),
        (15, 5, 'Left'),
        (14, 5, 'Left'),
        (13, 5, 'Left'),
        (12, 5, 'Left'),
        # Walk DOWN Column 12 to Row 10
        (12, 6, 'Down'),
        (12, 7, 'Down'),
        (12, 8, 'Down'),
        (12, 9, 'Down'),
        (12, 10, 'Down'),
        # Walk LEFT to Column 7
        (11, 10, 'Left'),
        (10, 10, 'Left'),
        (9, 10, 'Left'),
        (8, 10, 'Left'),
        (7, 10, 'Left'),
    ]
    
    print("Walking path to 1F West stairs...")
    for target in path:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()
            
    print("Stepping UP onto 1F West stairs to warp to 2F West...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)

print("Final position after script:", mgba.get_coordinates())
mgba.take_screenshot()
