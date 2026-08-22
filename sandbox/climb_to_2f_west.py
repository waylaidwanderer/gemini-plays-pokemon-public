import mgba
import time

def handle_battle():
    print("Coordinates did not change. Handling battle safely...")
    # Clear dialogue
    for _ in range(3):
        mgba.press_buttons(["B"])
        time.sleep(0.25)
    # Flee (Down, Right, A)
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A"])
    time.sleep(1.5)
    # Clear dialogue
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.25)

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
            print(f"Bumped at {pos} going {d} towards ({tx}, {ty}). Handling battle/obstacle...")
            handle_battle()
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
        else:
            if new_pos['x'] == tx and new_pos['y'] == ty:
                return True
        attempts += 1
    return False

# Starting at (4, 23) on 1F West (South Section)
pos = mgba.get_coordinates()
print("Starting Mansion 1F stairs climb from South Section:", pos)

if pos['x'] == 4 and pos['y'] == 23:
    print("--- STEP 1: WALKING TO 1F WEST STAIRS ---")
    path_1f = [
        # Walk UP Column 4 to Row 11
        (4, 22, 'Up'),
        (4, 21, 'Up'),
        (4, 20, 'Up'),
        (4, 19, 'Up'),
        (4, 18, 'Up'),
        (4, 17, 'Up'),
        (4, 16, 'Up'),
        (4, 15, 'Up'),
        (4, 14, 'Up'),
        (4, 13, 'Up'),
        (4, 12, 'Up'),
        (4, 11, 'Up'),
        # Walk RIGHT to Column 7
        (5, 11, 'Right'),
        (6, 11, 'Right'),
        (7, 11, 'Right'),
        # Walk UP to stairs at (7, 10)
        (7, 10, 'Up'),
    ]
    for target in path_1f:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach 1F target at ({tx}, {ty})")
            exit()
            
    print("At 1F West stairs (7, 10). Stepping UP to warp to 2F West...")
    mgba.press_buttons(["Up"])
    time.sleep(2.5)

print("Final position after 1F climb script:", mgba.get_coordinates())
mgba.take_screenshot()
