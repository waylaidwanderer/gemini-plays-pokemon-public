import mgba
import time

def handle_battle():
    print("Coordinates did not change. Likely a battle! Attempting to flee...")
    # Press Down, Right, A to run
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.0)
    # Mash B to clear transition back to overworld
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
            # Did not move!
            print(f"Bumped at {pos} going {direction}. Attempting battle escape...")
            handle_battle()
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                # Still didn't move, maybe try moving opposite direction? Or just retry
                pass
        else:
            # We moved!
            if new_pos['x'] == tx and new_pos['y'] == ty:
                return True
        attempts += 1
    return False

# Path to 2F West stairs
path = [
    (5, 26, 'Up'),
    (5, 25, 'Up'),
    (5, 24, 'Up'),
    (5, 23, 'Up'),
    (5, 22, 'Up'),
    (6, 22, 'Right'),
    (7, 22, 'Right'),
    (7, 21, 'Up'),
    (7, 20, 'Up'),
    (7, 19, 'Up'),
    (7, 18, 'Up'),
    (7, 17, 'Up'),
    (7, 16, 'Up'),
    (7, 15, 'Up'),
    (7, 14, 'Up'),
    (7, 13, 'Up'),
    (7, 12, 'Up'),
    (7, 11, 'Up'),
    (7, 10, 'Up'),
]

print("Starting walk to 2F West stairs...")
success = True
for target in path:
    tx, ty, d = target
    if not walk_step(tx, ty, d):
        print(f"Failed to reach target ({tx}, {ty})")
        success = False
        break

if success:
    print("Reached (7, 10) stairs! Taking the stairs UP to 2F...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)
    print("Position on 2F:", mgba.get_coordinates())
    mgba.take_screenshot()
