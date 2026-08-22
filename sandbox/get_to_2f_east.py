import mgba
import time

def handle_battle():
    print("Coordinates did not change. Likely a battle! Attempting to flee...")
    # Clear dialogue
    for _ in range(3):
        mgba.press_buttons(["B"])
        time.sleep(0.2)
    # Flee
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

# Starting inside Mansion 1F West at (2, 7)
pos = mgba.get_coordinates()
print("Starting definitive Mansion run from:", pos)

if pos['x'] == 2 and pos['y'] == 7:
    path = [
        # Walk UP to clear exit warp
        (2, 6, 'Up'),
        # Walk RIGHT along Row 6 to Column 7
        (3, 6, 'Right'),
        (4, 6, 'Right'),
        (5, 6, 'Right'),
        (6, 6, 'Right'),
        (7, 6, 'Right'),
        # Walk DOWN Column 7 to Row 11
        (7, 7, 'Down'),
        (7, 8, 'Down'),
        (7, 9, 'Down'),
        (7, 10, 'Down'),
        (7, 11, 'Down'),
        # Walk RIGHT along Row 11 to Column 18
        (8, 11, 'Right'),
        (9, 11, 'Right'),
        (10, 11, 'Right'),
        (11, 11, 'Right'),
        (12, 11, 'Right'),
        (13, 11, 'Right'),
        (14, 11, 'Right'),
        (15, 11, 'Right'),
        (16, 11, 'Right'),
        (17, 11, 'Right'),
        (18, 11, 'Right'),
        # Walk UP onto stairs at (18, 10)
        (18, 10, 'Up'),
    ]
    for target in path:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()
            
    print("At (18, 10) on 1F East stairs. Stepping UP to go to 2F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.5)

print("Final position after script (should be on 2F East):", mgba.get_coordinates())
mgba.take_screenshot()
