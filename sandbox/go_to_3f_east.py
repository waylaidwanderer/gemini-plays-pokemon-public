import mgba
import time

def handle_battle():
    print("Coordinates did not change. Likely a battle! Attempting to flee...")
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.0)
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
            print(f"Bumped at {pos} going {direction}. Attempting battle escape...")
            handle_battle()
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
        else:
            if new_pos['x'] == tx and new_pos['y'] == ty:
                return True
        attempts += 1
    return False

# 1. Walk from (24, 17) to (24, 15)
print("Walking to (24, 15)...")
walk_step(24, 16, "Up")
walk_step(24, 15, "Up")

# 2. Walk LEFT along Row 15 to Column 15
path_left = [
    (23, 15, 'Left'),
    (22, 15, 'Left'),
    (21, 15, 'Left'),
    (20, 15, 'Left'),
    (19, 15, 'Left'),
    (18, 15, 'Left'),
    (17, 15, 'Left'),
    (16, 15, 'Left'),
    (15, 15, 'Left'),
]
print("Walking left along Row 15...")
for target in path_left:
    tx, ty, d = target
    if not walk_step(tx, ty, d):
        print(f"Failed to reach target at ({tx}, {ty})")
        exit()

# 3. Walk UP Column 15 to Row 11
path_up = [
    (15, 14, 'Up'),
    (15, 13, 'Up'),
    (15, 12, 'Up'),
    (15, 11, 'Up'),
]
print("Walking up Column 15 to stairs...")
for target in path_up:
    tx, ty, d = target
    if not walk_step(tx, ty, d):
        print(f"Failed to reach target at ({tx}, {ty})")
        exit()

# 4. Step UP to enter the stairs
print("Stepping UP to enter 3F East stairs...")
mgba.press_buttons(["Up"])
time.sleep(2.0)

print("Final position:", mgba.get_coordinates())
mgba.take_screenshot()
