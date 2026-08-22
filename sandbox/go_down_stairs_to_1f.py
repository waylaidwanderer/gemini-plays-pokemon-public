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

# Starting at (12, 2) on 2F West (State B)
pos = mgba.get_coordinates()
print("Starting descent to 1F West via main stairs (8, 10):", pos)

if pos['x'] == 12 and pos['y'] == 2:
    print("--- STEP 1: WALKING TO 2F WEST MAIN STAIRS AT (8, 10) ---")
    path_to_stairs = [
        # Walk DOWN Column 12 to Row 11
        (12, 3, 'Down'),
        (12, 4, 'Down'),
        (12, 5, 'Down'),
        (12, 6, 'Down'),
        (12, 7, 'Down'),
        (12, 8, 'Down'),
        (12, 9, 'Down'),
        (12, 10, 'Down'),
        (12, 11, 'Down'),
        # Walk LEFT along Row 11 to Column 8
        (11, 11, 'Left'),
        (10, 11, 'Left'),
        (9, 11, 'Left'),
        (8, 11, 'Left'),
        # Walk UP onto stairs at (8, 10)
        (8, 10, 'Up'),
    ]
    for target in path_to_stairs:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()
            
    print("At 2F West main stairs. Stepping UP to warp DOWN to 1F West...")
    mgba.press_buttons(["Up"])
    time.sleep(2.5)

print("Final position after descent:", mgba.get_coordinates())
mgba.take_screenshot()
