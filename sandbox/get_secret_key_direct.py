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
    for _ in range(3):
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
            print(f"Bumped at {pos} going {d} towards ({tx}, {ty})")
            # Since there are NO encounters outside on Cinnabar, a bump outside is a real block.
            # But inside, it could be a battle.
            # Let's check if our Y is < 12 (meaning we are inside).
            # But to be safe, we can try to flee once.
            handle_battle()
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
        else:
            if new_pos['x'] == tx and new_pos['y'] == ty:
                return True
        attempts += 1
    return False

# Starting inside Lab Room 2 at (2, 7)
pos = mgba.get_coordinates()
print("Starting definitive exit and entry from:", pos)

if pos['x'] == 2 and pos['y'] == 7:
    # 1. Exit Lab Room 2
    print("Exiting Lab Room 2...")
    mgba.press_buttons(["Down"])
    time.sleep(2.0)
    
pos = mgba.get_coordinates()
if pos['x'] == 12 and pos['y'] == 4:
    # 2. Walk to Lab lobby and exit to Cinnabar Island
    print("Walking to Lab lobby...")
    # Down to Row 7
    walk_step(12, 5, 'Down')
    walk_step(12, 6, 'Down')
    walk_step(12, 7, 'Down')
    # Left to Column 2
    for col in range(11, 1, -1):
        walk_step(col, 7, 'Left')
    # Down to exit
    print("Exiting Lab...")
    mgba.press_buttons(["Down"])
    time.sleep(2.0)

pos = mgba.get_coordinates()
print("Outside on Cinnabar Island:", pos)

if pos['x'] == 6 and pos['y'] == 10:
    # 3. Walk from Lab to Mansion entrance (6, 3) safely without battle flee
    print("Walking to Mansion entrance...")
    cinnabar_path = [
        (6, 11, 'Down'),
        (5, 11, 'Left'),
        (4, 11, 'Left'),
        (4, 10, 'Up'),
        (4, 9, 'Up'),
        (4, 8, 'Up'),
        (4, 7, 'Up'),
        (4, 6, 'Up'),
        (4, 5, 'Up'),
        (4, 4, 'Up'),
        (5, 4, 'Right'),
        (6, 4, 'Right'),
    ]
    # Simple walk without handle_battle for Cinnabar Island (since no wild battles)
    for target in cinnabar_path:
        tx, ty, d = target
        mgba.press_buttons([d])
        time.sleep(0.55)
        
    print("At (6, 4). Stepping UP to enter Mansion...")
    mgba.press_buttons(["Up"])
    time.sleep(2.5)

pos = mgba.get_coordinates()
print("Position inside Mansion (expected at (5, 27)):", pos)
mgba.take_screenshot()
