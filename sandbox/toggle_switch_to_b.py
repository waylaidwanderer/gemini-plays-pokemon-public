import mgba
import time

def handle_battle():
    print("Coordinates did not change. Likely a battle! Mashing B and fleeing...")
    # Clear dialogue
    for _ in range(3):
        mgba.press_buttons(["B"])
        time.sleep(0.25)
    # Flee (Down, Right, A)
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A"])
    time.sleep(1.5)
    # Mash B to clear any post-battle text
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

# Currently at (12, 5) on 1F West
pos = mgba.get_coordinates()
print("Starting definitive Mansion 2F toggle run from:", pos)

if pos['x'] == 12 and pos['y'] == 5:
    print("--- STEP 1: CLIMBING STAIRS TO 2F WEST ---")
    path_1f = [
        (12, 4, 'Up'),
        (12, 3, 'Up'),
    ]
    for target in path_1f:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed on 1F at ({tx}, {ty})")
            exit()
            
    print("Warping UP to 2F West...")
    mgba.press_buttons(["Up"])
    time.sleep(2.5)

# Land on 2F West (expected at (12, 3))
pos = mgba.get_coordinates()
print("Position on 2F West:", pos)

# In case we land at (12, 3), walk down to Row 6
if pos['x'] == 12 and pos['y'] < 6:
    for r in range(pos['y'] + 1, 7):
        walk_step(12, r, 'Down')

pos = mgba.get_coordinates()
if pos['x'] == 12 and pos['y'] == 6:
    print("--- STEP 2: WALKING TO SWITCH BYPASSING PIT ---")
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
        # Walk DOWN Column 3 to Row 12 (bypassing Pit on Column 2 Row 8)
        (3, 7, 'Down'),
        (3, 8, 'Down'),
        (3, 9, 'Down'),
        (3, 10, 'Down'),
        (3, 11, 'Down'),
        (3, 12, 'Down'),
        # Walk LEFT to Column 2 on Row 12
        (2, 12, 'Left'),
    ]
    for target in path_2f:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed on 2F at ({tx}, {ty})")
            exit()
            
    print("At (2, 12) on 2F West. Facing UP and toggling switch to State B...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    # Interact with Mewtwo switch
    mgba.press_buttons(["A", "sleep 300", "A", "sleep 500", "B"])
    time.sleep(1.5)

print("Final position after toggle script:", mgba.get_coordinates())
mgba.take_screenshot()
