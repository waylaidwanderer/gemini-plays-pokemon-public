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

# 1. Flee from Grimer battle
print("Fleeing battle...")
handle_battle()
time.sleep(1.5)

# Verify coordinates are (20, 5)
pos = mgba.get_coordinates()
print("Position after fleeing:", pos)

# 2. Walk to 1F East stairs at (26, 6)
if pos['x'] == 20 and pos['y'] == 5:
    path_to_stairs = [
        (21, 5, 'Right'),
        (21, 4, 'Up'),
        (21, 3, 'Up'),
        (22, 3, 'Right'),
        (23, 3, 'Right'),
        (24, 3, 'Right'),
        (25, 3, 'Right'),
        (26, 3, 'Right'),
        (26, 4, 'Down'),
        (26, 5, 'Down'),
        (26, 6, 'Down'),
    ]
    print("Walking to 1F East stairs...")
    for target in path_to_stairs:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()
            
    print("Transitioning up to 2F East...")
    mgba.press_buttons(["Down"])
    time.sleep(2.0)
    
print("Final position:", mgba.get_coordinates())
mgba.take_screenshot()
