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

# Starting from (9, 10) on 3F West
pos = mgba.get_coordinates()
print("Starting position:", pos)

# Step 1: Walk to the switch at (2, 12) on 3F West
print("Walking to switch at (2, 12)...")
# Path: Walk Left to Column 3, Down to Row 12, Left to Column 2
targets_switch = [(3, 10), (3, 12), (2, 12)]
for target in targets_switch:
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

# Face UP and toggle the switch to State B
pos = mgba.get_coordinates()
if pos['x'] == 2 and pos['y'] == 12:
    print("Facing Up towards the switch...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    print("Toggling the switch to State B...")
    mgba.press_buttons(["A", "sleep 600", "A", "sleep 600", "B", "sleep 200"])
    time.sleep(1.0)

# Step 2: Walk to Column 5 Row 6 in State B
# We must walk DOWN to Row 13 first (since 2,12 and 3,12 gates are closed in State B),
# then Right to Column 5, then UP Column 5 to Row 6 (gate at 5,7 is open!)
print("Walking to Column 5 Row 6...")
targets_to_5 = [(2, 13), (5, 13), (5, 12), (5, 6)]
for target in targets_to_5:
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

# Step 3: Walk Right along Row 6 to Column 19 on 3F East
print("Walking Right to Column 19 on 3F East...")
while pos['x'] < 19:
    pos = walk_step("Right")

# Step 4: Systematically test all columns on Row 8 from 12 to 19 to find the open one!
print("Testing columns on Row 8 on the East side...")
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
    stuck = False
    while pos['y'] < 11:
        pos_before = pos
        pos = walk_step("Down")
        if pos == pos_before:
            print(f"Column {col} is BLOCKED at Row {pos['y'] + 1}")
            stuck = True
            break
            
    if not stuck:
        print(f"SUCCESS: Column {col} is completely open to Row 11 in State B!")
        open_column = col
        break
    else:
        # Walk back UP to Row 6 to test next column
        while pos['y'] > 6:
            pos = walk_step("Up")

# Step 5: Walk to the East stairs (15, 11) and warp
if open_column is not None:
    pos = mgba.get_coordinates()
    print("Walking to East stairs...")
    while pos['x'] > 15:
        pos = walk_step("Left")
    while pos['x'] < 15:
        pos = walk_step("Right")
        
    print("Stepping onto stairs...")
    pos = walk_step("Left")

print("Final position at end of script:", mgba.get_coordinates())
mgba.take_screenshot()
