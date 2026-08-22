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

def walk_step(tx, ty, d):
    attempts = 0
    while attempts < 15:
        pos = mgba.get_coordinates()
        if pos['x'] == tx and pos['y'] == ty:
            return True
        mgba.press_buttons([d])
        time.sleep(0.55)
        new_pos = mgba.get_coordinates()
        
        if new_pos == pos:
            print(f"Bumped at {pos} going {d} towards ({tx}, {ty}). Attempting battle escape...")
            handle_battle()
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
        else:
            if new_pos['x'] == tx and new_pos['y'] == ty:
                return True
        attempts += 1
    return False

# Starting at (2, 7) inside 1F West
pos = mgba.get_coordinates()
print("Starting safe Switch B toggle run from:", pos)

if pos['x'] == 2 and pos['y'] == 7:
    print("--- STEP 1: WALKING TO 1F WEST STAIRS ---")
    path_1f = [
        (2, 6, 'Up'),
        (3, 6, 'Right'),
        (4, 6, 'Right'),
        (5, 6, 'Right'),
        (6, 6, 'Right'),
        (7, 6, 'Right'),
        (8, 6, 'Right'),
        (9, 6, 'Right'),
        (10, 6, 'Right'),
        (11, 6, 'Right'),
        (12, 6, 'Right'),
        (12, 5, 'Up'),
        (12, 4, 'Up'),
        (12, 3, 'Up'),
    ]
    for target in path_1f:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach 1F target at ({tx}, {ty})")
            exit()
            
    print("Warping UP to 2F West...")
    mgba.press_buttons(["Up"])
    time.sleep(2.5)

# Land on 2F West (should be at (12, 3) or similar)
pos = mgba.get_coordinates()
print("Position on 2F West:", pos)

# In case we landed at some other coordinate, let's walk to (12, 6)
if pos['y'] < 6:
    for r in range(pos['y'] + 1, 7):
        walk_step(pos['x'], r, 'Down')

pos = mgba.get_coordinates()
if pos['x'] == 12 and pos['y'] == 6:
    print("--- STEP 2: WALKING TO 2F WEST SWITCH BYPASSING PIT ---")
    path_2f = [
        # Walk left along Row 6 to Column 3 (bypassing Pit on Column 2)
        (11, 6, 'Left'),
        (10, 6, 'Left'),
        (9, 6, 'Left'),
        (8, 6, 'Left'),
        (7, 6, 'Left'),
        (6, 6, 'Left'),
        (5, 6, 'Left'),
        (4, 6, 'Left'),
        (3, 6, 'Left'),
        # Walk DOWN Column 3 to Row 12 (bypassing Pit on Row 8 Column 2)
        (3, 7, 'Down'),
        (3, 8, 'Down'),
        (3, 9, 'Down'),
        (3, 10, 'Down'),
        (3, 11, 'Down'),
        (3, 12, 'Down'),
        # Walk LEFT to Column 2 on Row 12 (below the pit)
        (2, 12, 'Left'),
    ]
    for target in path_2f:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach 2F target at ({tx}, {ty})")
            exit()
            
    print("At (2, 12) on 2F West. Facing UP to toggle switch to State B...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    mgba.press_buttons(["A", "sleep 300", "A", "sleep 500", "B"])
    time.sleep(1.5)

print("Final position after toggle script:", mgba.get_coordinates())
mgba.take_screenshot()
