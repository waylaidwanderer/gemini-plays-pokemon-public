import mgba
import time

def handle_battle():
    print("Coordinates did not change. Likely a battle! Attempting to flee...")
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.0)
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.3)

def walk_step(tx, ty, direction):
    attempts = 0
    while attempts < 15:
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

# Currently at (20, 7) on 2F East (State B)
pos = mgba.get_coordinates()
print("Starting stairs check from:", pos)

if pos['x'] == 20 and pos['y'] == 7:
    path = [
        (19, 7, 'Left'),
        (19, 8, 'Down'),
    ]
    for target in path:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()
            
    print("At (19, 8) on 2F East stairs. Stepping DOWN to enter stairs...")
    mgba.press_buttons(["Down"])
    time.sleep(2.0)

print("Final position after climbing stairs:", mgba.get_coordinates())
mgba.take_screenshot()
