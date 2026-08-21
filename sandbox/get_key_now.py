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
print("Starting pos on 3F:", pos)

# We are at (12, 8).
# Step 1: Walk to the balcony on 3F East
path_to_balcony = [
    ('Left', 11, 8),
    ('Up', 11, 7), ('Up', 11, 6), ('Up', 11, 5),
    ('Right', 12, 5), ('Right', 13, 5), ('Right', 14, 5), ('Right', 15, 5), ('Right', 16, 5),
    ('Right', 17, 5), ('Right', 18, 5), ('Right', 19, 5), ('Right', 20, 5), ('Right', 21, 5),
    ('Right', 22, 5), ('Right', 23, 5), ('Right', 24, 5),
    ('Down', 24, 6), ('Down', 24, 7), ('Down', 24, 8), ('Down', 24, 9), ('Down', 24, 10),
    ('Down', 24, 11), ('Down', 24, 12), ('Down', 24, 13), ('Down', 24, 14)
]

print("Walking to the 3F balcony drop...")
for d, tx, ty in path_to_balcony:
    if pos['x'] == tx and pos['y'] == ty:
        continue
    pos = walk_step(d, tx, ty)

# Drop off the balcony
print("At (24, 14). Stepping Left to drop from balcony...")
mgba.press_buttons(["Left"])
time.sleep(3.0)

pos_b1f = mgba.get_coordinates()
print("Landed on B1F! Position:", pos_b1f)

# Step 2: Navigate B1F to the Secret Key room
# We land somewhere on B1F East. Let's walk to (10, 16)
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

# Step 3: Retrieve the Secret Key
print("At (1, 5). Facing UP and retrieving Secret Key...")
mgba.press_buttons(["Up"])
time.sleep(0.5)
mgba.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "B", "sleep 200"])
time.sleep(1.0)

print("Final position at end of script:", mgba.get_coordinates())
mgba.take_screenshot()
