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
    while attempts < 15:
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

# Currently at (21, 6) on 2F East (State B)
pos = mgba.get_coordinates()
print("Starting direct stairs test from:", pos)

if pos['x'] == 21 and pos['y'] == 6:
    path = [
        # Walk UP Column 21 to Row 3
        (21, 5, 'Up'),
        (21, 4, 'Up'),
        (21, 3, 'Up'),
        # Walk LEFT along Row 3 to Column 12
        (20, 3, 'Left'),
        (19, 3, 'Left'),
        (18, 3, 'Left'),
        (17, 3, 'Left'),
        (16, 3, 'Left'),
        (15, 3, 'Left'),
        (14, 3, 'Left'),
        (13, 3, 'Left'),
        (12, 3, 'Left'),
        # Walk DOWN Column 12 to Row 11
        (12, 4, 'Down'),
        (12, 5, 'Down'),
        (12, 6, 'Down'),
        (12, 7, 'Down'),
        (12, 8, 'Down'),
        (12, 9, 'Down'),
        (12, 10, 'Down'),
        (12, 11, 'Down'),
    ]
    
    print("Walking to (12, 11)...")
    for target in path:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()
            
    print("At (12, 11). Testing walking RIGHT along Row 11 towards Column 15...")
    row11_path = [
        (13, 11, 'Right'),
        (14, 11, 'Right'),
        (15, 11, 'Right'),
    ]
    for target in row11_path:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Blocked on Row 11 at target ({tx}, {ty})")
            break
            
    print("Final position after direct stairs test:", mgba.get_coordinates())
    mgba.take_screenshot()
