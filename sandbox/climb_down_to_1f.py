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

pos = mgba.get_coordinates()
print("Starting safe descent to 1F East from 2F East:", pos)

if pos['x'] == 23 and pos['y'] == 11:
    path = [
        # Walk UP to Row 7
        (23, 10, 'Up'),
        (23, 9, 'Up'),
        (23, 8, 'Up'),
        (23, 7, 'Up'),
        # Walk RIGHT to Column 26
        (24, 7, 'Right'),
        (25, 7, 'Right'),
        (26, 7, 'Right'),
        # Walk UP onto stairs at (26, 6)
        (26, 6, 'Up'),
    ]
    for target in path:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()
            
    print("At 2F East stairs (26, 6). Stepping UP to warp DOWN to 1F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.5)

print("Final position of climb_down_to_1f.py script:", mgba.get_coordinates())
mgba.take_screenshot()
