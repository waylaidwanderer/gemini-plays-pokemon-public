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

# We are at (25, 21) on 2F East in State B.
pos = mgba.get_coordinates()
print("Starting explore_east_balcony from:", pos)

if pos['x'] == 25 and pos['y'] == 21:
    path = [
        # Walk to Row 20
        (25, 20, 'Up'),
        # Walk LEFT along Row 20 to Column 20
        (24, 20, 'Left'),
        (23, 20, 'Left'),
        (22, 20, 'Left'),
        (21, 20, 'Left'),
        (20, 20, 'Left'),
        # Walk UP Column 20 to Row 18 (Shutter gate is OPEN in State B)
        (20, 19, 'Up'),
        (20, 18, 'Up'),
        # Walk LEFT along Row 18 to Column 15
        (19, 18, 'Left'),
        (18, 18, 'Left'),
        (17, 18, 'Left'),
        (16, 18, 'Left'),
        (15, 18, 'Left'),
        # Walk UP Column 15 to Row 11
        (15, 17, 'Up'),
        (15, 16, 'Up'),
        (15, 15, 'Up'),
        (15, 14, 'Up'),
        (15, 13, 'Up'),
        (15, 12, 'Up'),
        (15, 11, 'Up'),
    ]
    
    print("Walking path to 2F East stairs...")
    for target in path:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()
            
    print("Stepping UP onto the stairs to 3F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)

print("Final coordinates after script:", mgba.get_coordinates())
mgba.take_screenshot()
