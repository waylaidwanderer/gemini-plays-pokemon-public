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

# Starting at (21, 6) on 1F East (State B)
pos = mgba.get_coordinates()
print("Starting 1F East crossing to stairs from:", pos)

if pos['x'] == 21 and pos['y'] == 6:
    path = [
        # Walk UP Column 21 to Row 3
        (21, 5, 'Up'),
        (21, 4, 'Up'),
        (21, 3, 'Up'),
        # Walk RIGHT along Row 3 to Column 26 (crossing Column 22)
        (22, 3, 'Right'),
        (23, 3, 'Right'),
        (24, 3, 'Right'),
        (25, 3, 'Right'),
        (26, 3, 'Right'),
        # Walk DOWN Column 26 to stairs at (26, 6)
        (26, 4, 'Down'),
        (26, 5, 'Down'),
        (26, 6, 'Down'),
    ]
    for target in path:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed on 1F East at ({tx}, {ty})")
            exit()
            
    print("At 1F East stairs (26, 6). Stepping UP to warp to 2F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.5)

print("Final position after script:", mgba.get_coordinates())
mgba.take_screenshot()
