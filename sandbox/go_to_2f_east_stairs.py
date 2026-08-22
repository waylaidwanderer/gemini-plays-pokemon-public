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

# Starting at (12, 12) on 1F West (State B)
pos = mgba.get_coordinates()
print("Starting go_to_2f_east_stairs from:", pos)

if pos['x'] == 12 and pos['y'] == 12:
    path = [
        # Walk UP Column 12 to Row 8
        (12, 11, 'Up'),
        (12, 10, 'Up'),
        (12, 9, 'Up'),
        (12, 8, 'Up'),
        # Walk RIGHT along Row 8 to cross open gate at (15, 8)
        (13, 8, 'Right'),
        (14, 8, 'Right'),
        (15, 8, 'Right'),
        (16, 8, 'Right'), # Land south of Row 7 closed gate on 1F East!
        # Walk DOWN Column 16 to Row 11
        (16, 9, 'Down'),
        (16, 10, 'Down'),
        (16, 11, 'Down'),
    ]
    
    print("Walking path to 1F East stairs...")
    for target in path:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()
            
    print("Stepping DOWN to enter 1F East stairs and go UP to 2F East...")
    mgba.press_buttons(["Down"])
    time.sleep(2.0)

print("Final coordinates after script:", mgba.get_coordinates())
mgba.take_screenshot()
