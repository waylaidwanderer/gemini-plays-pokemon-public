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

# Path on 3F East (State B) from (26, 2) to (20, 18) via Column 25, Row 15, and Column 16
path_to_drop = [
    # Walk DOWN Column 26 to Row 12
    (26, 3, 'Down'),
    (26, 4, 'Down'),
    (26, 5, 'Down'),
    (26, 6, 'Down'),
    (26, 7, 'Down'),
    (26, 8, 'Down'),
    (26, 9, 'Down'),
    (26, 10, 'Down'),
    (26, 11, 'Down'),
    (26, 12, 'Down'),
    # Walk LEFT to Column 25
    (25, 12, 'Left'),
    # Walk DOWN Column 25 to Row 15
    (25, 13, 'Down'),
    (25, 14, 'Down'),
    (25, 15, 'Down'),
    # Walk LEFT along Row 15 to Column 16
    (24, 15, 'Left'),
    (23, 15, 'Left'),
    (22, 15, 'Left'),
    (21, 15, 'Left'),
    (20, 15, 'Left'),
    (19, 15, 'Left'),
    (18, 15, 'Left'),
    (17, 15, 'Left'),
    (16, 15, 'Left'),
    # Walk DOWN Column 16 to Row 18
    (16, 16, 'Down'),
    (16, 17, 'Down'),
    (16, 18, 'Down'),
    # Walk RIGHT along Row 18 to Column 20
    (17, 18, 'Right'),
    (18, 18, 'Right'),
    (19, 18, 'Right'),
    (20, 18, 'Right'),
]

print("Executing State B balcony drop path via Column 25 and Row 15...")
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
