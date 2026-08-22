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

# Currently at (22, 7) on 2F East (State B)
pos = mgba.get_coordinates()
print("Starting Row 7 path on 2F East from:", pos)

if pos['x'] == 22 and pos['y'] == 7:
    path = [
        # Walk LEFT along Row 7 to Column 15
        (21, 7, 'Left'),
        (20, 7, 'Left'),
        (19, 7, 'Left'),
        (18, 7, 'Left'),
        (17, 7, 'Left'),
        (16, 7, 'Left'),
        (15, 7, 'Left'),
        # Walk DOWN Column 15 to Row 11
        (15, 8, 'Down'),
        (15, 9, 'Down'),
        (15, 10, 'Down'),
        (15, 11, 'Down'),
    ]
    print("Walking to 2F East stairs...")
    for target in path:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()
            
    print("At (15, 11) on 2F East. Stepping UP to go UP to 3F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)

print("Final position after climbing stairs:", mgba.get_coordinates())
mgba.take_screenshot()
