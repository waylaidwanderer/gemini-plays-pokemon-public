import mgba
import time

def handle_battle():
    print("Coordinates did not change. Battle or obstacle detected! Attempting to flee...")
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    mgba.press_buttons(["B", "sleep 100", "B", "sleep 100", "B"])
    time.sleep(1.0)

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.35)
    pos_after = mgba.get_coordinates()
    if pos_before == pos_after:
        print(f"BUMPED at {pos_before} going {direction}")
    else:
        print(f"Moved to {pos_after}")
    return pos_after

# Dismiss "Who wouldn't?" text first
print("Dismissing text...")
mgba.press_buttons(["B"])
time.sleep(0.5)

# Starting from (2, 12) on 3F West (State B)
pos = mgba.get_coordinates()
print("Starting position:", pos)

# Step 1: Walk to Column 6 Row 6 in State B
# We must walk DOWN to Row 13 first (since 2,12 and 3,12 gates are closed in State B),
# then Right to Column 5, then UP Column 5 to Row 11, Right to Column 6, UP Column 6 to Row 6 (gate at 6,7 is open!)
print("1. Walking to Column 6 Row 6...")
targets_to_6 = [(2, 13), (5, 13), (5, 12), (5, 11), (6, 11), (6, 6)]
for target in targets_to_6:
    while pos['x'] != target[0] or pos['y'] != target[1]:
        dx = target[0] - pos['x']
        dy = target[1] - pos['y']
        if dx < 0:
            pos = walk_step("Left")
        elif dx > 0:
            pos = walk_step("Right")
        elif dy < 0:
            pos = walk_step("Up")
        elif dy > 0:
            pos = walk_step("Down")

# Step 2: Walk Right along Row 6 to Column 19 on 3F East
print("2. Walking Right to Column 19 on 3F East...")
while pos['x'] < 19:
    pos = walk_step("Right")

# Step 3: Walk Down Column 19 to Row 15 (should be open now in State B!)
print("3. Walking Down Column 19...")
while pos['y'] < 15:
    pos_before = pos
    pos = walk_step("Down")
    if pos == pos_before:
        print("CRITICAL: Column 19 is still blocked!")
        handle_battle()
        pos = mgba.get_coordinates()

# Step 4: Walk to the balcony and drop to B1F East
print("4. Walking to balcony and dropping...")
targets_balcony = [(21, 15), (20, 15), (20, 18), (19, 18)]
for target in targets_balcony:
    while pos['x'] != target[0] or pos['y'] != target[1]:
        dx = target[0] - pos['x']
        dy = target[1] - pos['y']
        if dx < 0:
            pos = walk_step("Left")
        elif dx > 0:
            pos = walk_step("Right")
        elif dy < 0:
            pos = walk_step("Up")
        elif dy > 0:
            pos = walk_step("Down")
time.sleep(2.0)

# Land on B1F East at (19, 16)
pos_b1f = mgba.get_coordinates()
print("Position on B1F East:", pos_b1f)

# Step 5: Walk to B1F West NORTH room via open gate at (9, 5)
if pos_b1f['x'] == 19 and pos_b1f['y'] == 16:
    print("5. Walking to B1F West NORTH room...")
    targets_b1f = [(10, 16), (10, 5), (1, 5)]
    for target in targets_b1f:
        while pos['x'] != target[0] or pos['y'] != target[1]:
            dx = target[0] - pos['x']
            dy = target[1] - pos['y']
            if dx < 0:
                pos = walk_step("Left")
            elif dx > 0:
                pos = walk_step("Right")
            elif dy < 0:
                pos = walk_step("Up")
            elif dy > 0:
                pos = walk_step("Down")

# Step 6: Retrieve Secret Key at (1, 4)
pos_key = mgba.get_coordinates()
print("Position near Secret Key:", pos_key)
if pos_key['x'] == 1 and pos_key['y'] == 5:
    print("6. Facing UP and retrieving Secret Key...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    mgba.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "B", "sleep 200"])
    time.sleep(1.0)

print("Coordinates at end of script:", mgba.get_coordinates())
mgba.take_screenshot()
