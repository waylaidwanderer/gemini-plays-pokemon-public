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

# Path on 3F East (State B) from (12, 12) to (20, 18) via Row 6
path_to_drop = [
    # Walk UP Column 12 to Row 6
    (12, 11, 'Up'),
    (12, 10, 'Up'),
    (12, 9, 'Up'),
    (12, 8, 'Up'),
    (12, 7, 'Up'),
    (12, 6, 'Up'),
    # Walk RIGHT along Row 6 to Column 20
    (13, 6, 'Right'),
    (14, 6, 'Right'),
    (15, 6, 'Right'),
    (16, 6, 'Right'),
    (17, 6, 'Right'),
    (18, 6, 'Right'),
    (19, 6, 'Right'),
    (20, 6, 'Right'),
    # Walk DOWN Column 20 to Row 18 (passing open gate at (20, 17))
    (20, 7, 'Down'),
    (20, 8, 'Down'),
    (20, 9, 'Down'),
    (20, 10, 'Down'),
    (20, 11, 'Down'),
    (20, 12, 'Down'),
    (20, 13, 'Down'),
    (20, 14, 'Down'),
    (20, 15, 'Down'),
    (20, 16, 'Down'),
    (20, 17, 'Down'),
    (20, 18, 'Down'),
]

print("Executing State B balcony drop path via Row 6...")
success = True
for target in path_to_drop:
    tx, ty, d = target
    if not walk_step(tx, ty, d):
        print(f"Failed to reach target ({tx}, {ty})")
        success = False
        break

if success:
    print("At (20, 18)! Stepping LEFT to drop over the balcony...")
    mgba.press_buttons(["Left"])
    time.sleep(3.0) # Wait for drop transition
    print("Landed on B1F! Current position:", mgba.get_coordinates())
    mgba.take_screenshot()
