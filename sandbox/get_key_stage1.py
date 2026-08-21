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

# --- STAGE 1: CINNABAR ISLAND TO B1F EAST LANDING IN STATE A ---
pos = mgba.get_coordinates()
print("Starting outside:", pos)

# 1. Walk from (11, 7) to Mansion entrance at (6, 3)
path_to_mansion = [
    ('Left', 10, 7),
    ('Up', 10, 6), ('Up', 10, 5), ('Up', 10, 4),
    ('Left', 9, 4), ('Left', 8, 4), ('Left', 7, 4), ('Left', 6, 4),
    ('Up', 6, 3)
]

print("Walking to the Pokemon Mansion entrance...")
for d, tx, ty in path_to_mansion:
    if pos['x'] == tx and pos['y'] == ty:
        continue
    pos = walk_step(d, tx, ty)

# Step UP into the Mansion
print("Entering Pokemon Mansion...")
pos = walk_step("Up", 5, 26)
time.sleep(1.5)

print("Coordinates inside Mansion 1F West:", mgba.get_coordinates())

# 2. Walk UP Column 5, Right to (7, 11), and UP to 2F stairs
path_on_1f = [
    ('Up', 5, 25), ('Up', 5, 24), ('Up', 5, 23), ('Up', 5, 22), ('Up', 5, 21),
    ('Up', 5, 20), ('Up', 5, 19), ('Up', 5, 18), ('Up', 5, 17), ('Up', 5, 16),
    ('Up', 5, 15), ('Up', 5, 14), ('Up', 5, 13), ('Up', 5, 12), ('Up', 5, 11),
    ('Right', 6, 11), ('Right', 7, 11)
]

print("Walking to the 1F West stairs...")
for d, tx, ty in path_on_1f:
    pos = walk_step(d, tx, ty)

# Step UP to warp to 2F West
print("Stepping onto 1F stairs to warp UP...")
pos = walk_step("Up", 7, 10)
time.sleep(1.5)

# On 2F West, land on (7, 10). Step Down to (7, 11) then Up to (7, 10) to warp to 3F West
pos = mgba.get_coordinates()
print("Arrived on 2F West:", pos)
if pos['x'] == 7 and pos['y'] == 10:
    pos = walk_step("Down", 7, 11)
    print("Stepping onto 2F stairs to warp UP to 3F...")
    pos = walk_step("Up", 7, 10)
    time.sleep(1.5)

# On 3F West (State A), land on (7, 11) (or (7, 10))
pos = mgba.get_coordinates()
print("Arrived on 3F West (State A):", pos)

# Cross from 3F West to 3F East using Row 6:
path_on_3f = [
    ('Right', 8, 11), ('Right', 9, 11), ('Right', 10, 11), ('Right', 11, 11), ('Right', 12, 11),
    ('Up', 12, 10), ('Up', 12, 9), ('Up', 12, 8), ('Up', 12, 7), ('Up', 12, 6),
    ('Right', 13, 6), ('Right', 14, 6), ('Right', 15, 6), ('Right', 16, 6), ('Right', 17, 6), ('Right', 18, 6), ('Right', 19, 6),
    ('Down', 19, 7), ('Down', 19, 8), ('Down', 19, 9), ('Down', 19, 10), ('Down', 19, 11), ('Down', 19, 12), ('Down', 19, 13), ('Down', 19, 14), ('Down', 19, 15), ('Down', 19, 16)
]

print("Crossing 3F West to 3F East balcony area...")
for d, tx, ty in path_on_3f:
    if pos['x'] == tx and pos['y'] == ty:
        continue
    pos = walk_step(d, tx, ty)

# Drop off the balcony by stepping Left to (18, 16)
print("At (19, 16) on 3F East (State A). Stepping Left to drop from balcony...")
mgba.press_buttons(["Left"])
time.sleep(3.0)

print("Coordinates after drop sequence:", mgba.get_coordinates())
mgba.take_screenshot()
