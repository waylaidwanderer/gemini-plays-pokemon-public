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

# Starting at (24, 11) on 2F East
pos = mgba.get_coordinates()
print("Starting Row 3 test from:", pos)

if pos['x'] == 24 and pos['y'] == 11:
    path = [
        # Walk RIGHT to Column 26
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
        # Try to walk LEFT along Row 3 to Column 2
        (25, 3, 'Left'),
        (24, 3, 'Left'),
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
        (11, 3, 'Left'),
        (10, 3, 'Left'),
        (9, 3, 'Left'),
        (8, 3, 'Left'),
        (7, 3, 'Left'),
        (6, 3, 'Left'),
        (5, 3, 'Left'),
        (4, 3, 'Left'),
        (3, 3, 'Left'),
        (2, 3, 'Left'),
    ]
    
    print("Walking path...")
    for target in path:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()
            
print("Successfully reached (2, 3) on Row 3!")
mgba.take_screenshot()
