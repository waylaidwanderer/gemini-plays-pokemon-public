import mgba
import time

def handle_battle():
    print("Coordinates did not change. Battle or obstacle detected! Attempting to flee...")
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    mgba.press_buttons(["B", "sleep 100", "B", "sleep 100", "B"])
    time.sleep(1.0)

def walk_step(direction, tx, ty):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.35)
    pos_after = mgba.get_coordinates()
    
    attempts = 0
    while pos_after['x'] != tx or pos_after['y'] != ty:
        if pos_after == pos_before:
            print(f"BUMPED at {pos_before} going {direction}. Handling battle...")
            handle_battle()
            mgba.press_buttons([direction])
            time.sleep(0.35)
            pos_after = mgba.get_coordinates()
        else:
            print(f"Unexpected move: expected ({tx}, {ty}), got {pos_after}. Readjusting...")
            return pos_after
            
        attempts += 1
        if attempts > 5:
            print(f"Failed to step to ({tx}, {ty})")
            break
            
    return pos_after

pos = mgba.get_coordinates()
print("Starting pos inside 3F East:", pos)

# Path from (21, 6) to balcony drop at (19, 18)
# We must walk UP to Row 3 first because Column 22 is blocked by a wall on Row 6!
path_to_drop = [
    ('Up', 21, 5), ('Up', 21, 4), ('Up', 21, 3),
    ('Right', 22, 3), ('Right', 23, 3),
    ('Down', 23, 4), ('Down', 23, 5), ('Down', 23, 6), ('Down', 23, 7), ('Down', 23, 8), ('Down', 23, 9), ('Down', 23, 10), ('Down', 23, 11),
    ('Left', 22, 11), ('Left', 21, 11),
    ('Down', 21, 12), ('Down', 21, 13), ('Down', 21, 14), ('Down', 21, 15),
    ('Left', 20, 15),
    ('Down', 20, 16), ('Down', 20, 17), ('Down', 20, 18)
]

print("Walking to the 3F balcony drop...")
for d, tx, ty in path_to_drop:
    if pos['x'] == tx and pos['y'] == ty:
        continue
    pos = walk_step(d, tx, ty)

# Drop off the balcony by stepping Left to (19, 18)
print("At (20, 18). Stepping Left to drop from balcony...")
mgba.press_buttons(["Left"])
time.sleep(3.0)

pos_b1f = mgba.get_coordinates()
print("Landed on B1F! Position:", pos_b1f)

# Step 2: Navigate B1F to the Secret Key room standing at (1, 5)
targets_b1f = [(10, 16), (10, 5), (1, 5)]
for tx, ty in targets_b1f:
    while pos_b1f['x'] != tx or pos_b1f['y'] != ty:
        dx = tx - pos_b1f['x']
        dy = ty - pos_b1f['y']
        if dx < 0:
            pos_b1f = walk_step("Left", pos_b1f['x'] - 1, pos_b1f['y'])
        elif dx > 0:
            pos_b1f = walk_step("Right", pos_b1f['x'] + 1, pos_b1f['y'])
        elif dy < 0:
            pos_b1f = walk_step("Up", pos_b1f['x'], pos_b1f['y'] - 1)
        elif dy > 0:
            pos_b1f = walk_step("Down", pos_b1f['x'], pos_b1f['y'] + 1)

# Step 3: Retrieve the Secret Key at (1, 4)
print("At (1, 5). Facing UP and retrieving Secret Key...")
mgba.press_buttons(["Up"])
time.sleep(0.5)
mgba.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "B", "sleep 200"])
time.sleep(1.0)

print("Final position at end of script:", mgba.get_coordinates())
mgba.take_screenshot()
