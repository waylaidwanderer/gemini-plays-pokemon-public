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

# Starting at (26, 5) on 2F East (State B)
pos = mgba.get_coordinates()
print("Starting 2F East to 3F East climb script from:", pos)

if pos['x'] == 26 and pos['y'] == 5:
    path = [
        # Walk DOWN Column 26 to Row 11
        (26, 6, 'Down'),
        (26, 7, 'Down'),
        (26, 8, 'Down'),
        (26, 9, 'Down'),
        (26, 10, 'Down'),
        (26, 11, 'Down'),
        # Walk LEFT along Row 11 to Column 15
        (25, 11, 'Left'),
        (24, 11, 'Left'),
        (23, 11, 'Left'),
        (22, 11, 'Left'),
        (21, 11, 'Left'),
        (20, 11, 'Left'),
        (19, 11, 'Left'),
        (18, 11, 'Left'),
        (17, 11, 'Left'),
        (16, 11, 'Left'),
        (15, 11, 'Left'),
        # Walk UP onto stairs at (15, 10)? Or (15, 11)?
        # Wait, if the stairs are at (15, 11), we step UP onto them.
        (15, 10, 'Up'),
    ]
    for target in path:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed on 2F East at ({tx}, {ty})")
            exit()
            
    print("At 2F East stairs. Stepping UP to warp UP to 3F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.5)

print("Final position of 2F East script:", mgba.get_coordinates())
mgba.take_screenshot()
