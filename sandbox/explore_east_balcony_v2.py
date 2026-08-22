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

def walk_to_local(tx, ty):
    pos = mgba.get_coordinates()
    attempts = 0
    while (pos['x'] != tx or pos['y'] != ty) and attempts < 40:
        dx = tx - pos['x']
        dy = ty - pos['y']
        if dx < 0: d = "Left"
        elif dx > 0: d = "Right"
        elif dy < 0: d = "Up"
        else: d = "Down"
        
        pos_before = pos
        mgba.press_buttons([d])
        time.sleep(0.55)
        pos = mgba.get_coordinates()
        if pos == pos_before:
            handle_battle()
            pos = mgba.get_coordinates()
        attempts += 1
    return pos['x'] == tx and pos['y'] == ty

# Start at (21, 6) on 2F East (State B)
pos = mgba.get_coordinates()
print("Starting Row 14 test from:", pos)

if pos['x'] == 21 and pos['y'] == 6:
    # Walk left along Row 6 to Column 14
    path = [
        (20, 6, 'Left'),
        (19, 6, 'Left'),
        (18, 6, 'Left'),
        (17, 6, 'Left'),
        (16, 6, 'Left'),
        (15, 6, 'Left'),
        (14, 6, 'Left'),
    ]
    for target in path:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()
            
    print("At (14, 6). Testing walking DOWN Column 14...")
    col14_path = [
        (14, 7, 'Down'),
        (14, 8, 'Down'),
        (14, 9, 'Down'),
        (14, 10, 'Down'),
        (14, 11, 'Down'),
    ]
    for target in col14_path:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Blocked on Column 14 at target ({tx}, {ty})")
            break
            
    print("Final position after Column 14 test:", mgba.get_coordinates())
    mgba.take_screenshot()
