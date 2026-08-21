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

# 1. Clear "Got away safely!" textbox
mgba.press_buttons(["B"])
time.sleep(1.0)
pos = mgba.get_coordinates()
print("Starting position:", pos)

# Walk to switch alignment if needed (should be at (2, 12))
if pos['x'] == 2 and pos['y'] == 11:
    pos = walk_step("Down", 2, 12)

# Path to 3F East balcony
path_to_balcony = [
    ('Right', 3, 12), ('Right', 4, 12), ('Right', 5, 12), ('Right', 6, 12), ('Right', 7, 12),
    ('Down', 7, 13),
    ('Right', 8, 13), ('Right', 9, 13),
    ('Up', 9, 12), ('Up', 9, 11), ('Up', 9, 10),
    ('Right', 10, 10), ('Right', 11, 10),
    ('Up', 11, 9), ('Up', 11, 8), ('Up', 11, 7), ('Up', 11, 6), ('Up', 11, 5),
    ('Right', 12, 5), ('Right', 13, 5), ('Right', 14, 5), ('Right', 15, 5), ('Right', 16, 5),
    ('Right', 17, 5), ('Right', 18, 5), ('Right', 19, 5), ('Right', 20, 5), ('Right', 21, 5),
    ('Right', 22, 5), ('Right', 23, 5), ('Right', 24, 5),
    ('Down', 24, 6), ('Down', 24, 7), ('Down', 24, 8), ('Down', 24, 9), ('Down', 24, 10),
    ('Down', 24, 11), ('Down', 24, 12), ('Down', 24, 13), ('Down', 24, 14)
]

print("Walking to the 3F balcony drop...")
for d, tx, ty in path_to_balcony:
    # If we are already at the target coordinate, skip
    if pos['x'] == tx and pos['y'] == ty:
        continue
    pos = walk_step(d, tx, ty)

# Drop off the balcony
print("At (24, 14). Stepping Left to drop from balcony...")
mgba.press_buttons(["Left"])
time.sleep(3.0)

pos_b1f = mgba.get_coordinates()
print("Landed on B1F East! Position:", pos_b1f)
mgba.take_screenshot()
