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

# Starting from (9, 11) on 2F West (State B)
pos = mgba.get_coordinates()
print("Starting position:", pos)

# Step 1: Walk to 2F West stairs at (7, 10) to warp UP to 3F West
print("1. Walking to 2F West stairs to warp UP...")
targets_stairs = [(7, 11), (7, 10)]
for target in targets_stairs:
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
time.sleep(1.5)

# Land on 3F West (should land at (7, 11))
pos = mgba.get_coordinates()
print("Position on 3F West:", pos)

# Step 2: Walk to (6, 11)
if pos['x'] == 7 and pos['y'] == 11:
    pos = walk_step("Left")

# Step 3: Walk Right along Row 11 to Column 10 (bypassing the 7,10 stairs!)
print("3. Walking Right to Column 10...")
while pos['x'] < 10:
    pos_before = pos
    pos = walk_step("Right")
    if pos == pos_before:
        # If we bump, it could be a battle or NPC. Let's wait.
        time.sleep(0.5)

# Step 4: Walk UP Column 10 to Row 6 (gate is open in State B!)
print("4. Walking UP Column 10 to Row 6...")
while pos['y'] > 6:
    pos = walk_step("Up")

# Step 5: Walk Right along Row 6 to Column 19 on 3F East
print("5. Walking Right to Column 19 on 3F East...")
while pos['x'] < 19:
    pos = walk_step("Right")

# Step 6: Walk Down Column 19 to Row 15 (should be open in State B!)
print("6. Walking Down Column 19...")
while pos['y'] < 15:
    pos_before = pos
    pos = walk_step("Down")
    if pos == pos_before:
        print("CRITICAL: Column 19 is still blocked!")
        handle_battle()
        pos = mgba.get_coordinates()

# Step 7: Walk to the balcony and drop to B1F East
print("7. Walking to balcony and dropping...")
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

# Step 8: Walk to B1F West NORTH room via open gate at (9, 5)
if pos_b1f['x'] == 19 and pos_b1f['y'] == 16:
    print("8. Walking to B1F West NORTH room...")
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

# Step 9: Retrieve Secret Key at (1, 4)
pos_key = mgba.get_coordinates()
print("Position near Secret Key:", pos_key)
if pos_key['x'] == 1 and pos_key['y'] == 5:
    print("9. Facing UP and retrieving Secret Key...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    mgba.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "B", "sleep 200"])
    time.sleep(1.0)

print("Coordinates at end of script:", mgba.get_coordinates())
mgba.take_screenshot()
