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

# Starting from (6, 10) on 3F West (State B)
pos = mgba.get_coordinates()
print("Starting position:", pos)

# Step 1: Walk Right to Column 10 on Row 10
print("Walking to (10, 10)...")
while pos['x'] < 10:
    pos = walk_step("Right")

# Step 2: Walk UP Column 10 to Row 6
print("Walking to (10, 6)...")
while pos['y'] > 6:
    pos = walk_step("Up")

# Step 3: Walk Right along Row 6 to Column 19 on 3F East
print("Walking to (19, 6)...")
while pos['x'] < 19:
    pos = walk_step("Right")

# Step 4: Walk Down Column 19 to Row 15 (let's check if it's open, if blocked, we'll try other columns!)
print("Walking Down Column 19...")
stuck = False
while pos['y'] < 15:
    pos_before = pos
    pos = walk_step("Down")
    if pos == pos_before:
        print(f"Column 19 is blocked at Row {pos['y'] + 1}!")
        stuck = True
        break

# If Column 19 is blocked, systematically test all columns on Row 8 from 19 down to 12!
if stuck:
    print("Testing other columns on Row 8 on the East side...")
    columns_to_test = [19, 18, 17, 16, 15, 14, 13, 12]
    open_column = None

    for col in columns_to_test:
        # Walk to Column `col` on Row 6
        while pos['x'] > col:
            pos = walk_step("Left")
        while pos['x'] < col:
            pos = walk_step("Right")
            
        print(f"Testing Column {col} Row 8...")
        # Try walking DOWN to Row 11
        stuck_col = False
        while pos['y'] < 11:
            pos_before = pos
            pos = walk_step("Down")
            if pos == pos_before:
                print(f"Column {col} is BLOCKED at Row {pos['y'] + 1}")
                stuck_col = True
                break
                
        if not stuck_col:
            print(f"SUCCESS: Column {col} is completely open to Row 11 in State B!")
            open_column = col
            break
        else:
            # Walk back UP to Row 6 to test next column
            while pos['y'] > 6:
                pos = walk_step("Up")

    # If we found an open column, continue Down to Row 15
    if open_column is not None:
        while pos['y'] < 15:
            pos = walk_step("Down")
        # Walk back to Column 19 Row 15
        while pos['x'] < 19:
            pos = walk_step("Right")

# Step 5: Walk to the balcony and drop to B1F East
print("Walking to balcony and dropping...")
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

# Step 6: Walk to B1F West NORTH room via open gate at (9, 5)
if pos_b1f['x'] == 19 and pos_b1f['y'] == 16:
    print("Walking to B1F West NORTH room...")
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

# Step 7: Retrieve Secret Key at (1, 4)
pos_key = mgba.get_coordinates()
print("Position near Secret Key:", pos_key)
if pos_key['x'] == 1 and pos_key['y'] == 5:
    print("Facing UP and retrieving Secret Key...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    mgba.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "B", "sleep 200"])
    time.sleep(1.0)

print("Coordinates at end of script:", mgba.get_coordinates())
mgba.take_screenshot()
