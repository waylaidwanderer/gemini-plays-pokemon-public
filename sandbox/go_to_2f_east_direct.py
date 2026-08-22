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

# 1. Flee from wild Grimer battle
print("Fleeing battle...")
handle_battle()
time.sleep(1.5)

pos = mgba.get_coordinates()
print("Position after fleeing battle:", pos)

# We are standing on Column 10 (or 11 or 12). Let's walk to (12, 10)
if pos['x'] >= 9 and pos['x'] <= 12:
    print("Walking to (12, 10) on 1F West...")
    # Walk vertically to Row 11
    current_y = mgba.get_coordinates()['y']
    if current_y > 11:
        for y in range(current_y - 1, 10, -1):
            walk_step(mgba.get_coordinates()['x'], y, 'Up')
            
    # From Column 10 or 11, walk to (11, 11)
    walk_step(11, 11, 'Right')
    
    # Walk to (12, 10)
    walk_step(11, 10, 'Up')
    walk_step(12, 10, 'Right')

# 2. Walk UP Column 12 to Row 5
pos = mgba.get_coordinates()
if pos['x'] == 12 and pos['y'] == 10:
    path_to_stairs = [
        (12, 9, 'Up'),
        (12, 8, 'Up'),
        (12, 7, 'Up'),
        (12, 6, 'Up'),
        (12, 5, 'Up'),
        # Cross on Row 5 to Column 16
        (13, 5, 'Right'),
        (14, 5, 'Right'),
        (15, 5, 'Right'),
        (16, 5, 'Right'),
        # Walk DOWN Column 16 to stairs at (16, 11)
        (16, 6, 'Down'),
        (16, 7, 'Down'),
        (16, 8, 'Down'),
        (16, 9, 'Down'),
        (16, 10, 'Down'),
        (16, 11, 'Down'),
    ]
    print("Walking direct path to 1F East stairs...")
    for target in path_to_stairs:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()
            
    print("Stepping DOWN/UP to enter the stairs...")
    mgba.press_buttons(["Down"]) # Try down first, if not, try up
    time.sleep(2.0)
    
print("Final coordinates:", mgba.get_coordinates())
mgba.take_screenshot()
