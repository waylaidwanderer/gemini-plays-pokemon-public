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

# --- FINAL STAGE: RETRIEVE SECRET KEY ---
pos = mgba.get_coordinates()
print("Starting pos on 3F East (State A):", pos)

# We are at (21, 6) on 3F East.
# Walk Left to Column 19
while pos['x'] > 19:
    pos = walk_step("Left", pos['x'] - 1, pos['y'])

# Walk Down Column 19 to Row 16: (19, 16)
while pos['y'] < 16:
    pos = walk_step("Down", pos['x'], pos['y'] + 1)

# Drop off the balcony by stepping Left to (18, 16)
print("At (19, 16). Stepping Left to drop from balcony...")
mgba.press_buttons(["Left"])
time.sleep(3.0)

pos_b1f = mgba.get_coordinates()
print("Landed on B1F East! Position:", pos_b1f)

# Step 2: Walk to B1F West switch stand tile at (2, 12)
targets_to_switch = [(10, 16), (10, 11), (3, 11), (3, 12), (2, 12)]
for tx, ty in targets_to_switch:
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

# Step 3: Toggle B1F switch to State B
print("At (2, 12) on B1F West. Facing UP to toggle switch...")
mgba.press_buttons(["Up"])
time.sleep(0.5)

print("Toggling Mewtwo statue switch to State B...")
mgba.press_buttons(["A", "sleep 300", "A", "sleep 500", "B"])
time.sleep(1.5)

# Step 4: Walk to the Secret Key room standing at (1, 5)
pos_b1f = mgba.get_coordinates()
targets_to_key = [(3, 12), (3, 11), (10, 11), (10, 5), (1, 5)]
for tx, ty in targets_to_key:
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

# Step 5: Retrieve the Secret Key at (1, 4)
print("At (1, 5). Facing UP and retrieving Secret Key...")
mgba.press_buttons(["Up"])
time.sleep(0.5)
mgba.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "B", "sleep 200"])
time.sleep(1.0)

print("Final position at end of script:", mgba.get_coordinates())
mgba.take_screenshot()
