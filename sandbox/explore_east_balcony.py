import mgba
import time

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

# Starting from (21, 15) on 3F East (State B)
pos = mgba.get_coordinates()
print("Starting position:", pos)

# Step 1: Walk UP to Row 6
print("Walking UP to Row 6...")
while pos['y'] > 6:
    pos = walk_step("Up")

# Step 2: Walk Right to Column 25
print("Walking Right to Column 25...")
while pos['x'] < 25:
    pos = walk_step("Right")

# Step 3: Walk Down Column 25 to Row 15
print("Walking Down Column 25 to Row 15...")
while pos['y'] < 15:
    pos = walk_step("Down")

# Step 4: Test walking Down from Column 25, 24, 26 to find where the drop is!
test_cols = [25, 24, 26]
for col in test_cols:
    # Walk to Column `col` on Row 15
    while pos['x'] > col:
        pos = walk_step("Left")
    while pos['x'] < col:
        pos = walk_step("Right")
        
    print(f"Testing Column {col} Row 15 going Down...")
    pos_before = pos
    pos = walk_step("Down")
    if pos != pos_before:
        print(f"SUCCESS: Moved/Dropped! New position: {pos}")
        if abs(pos['y'] - pos_before['y']) > 2 or pos['y'] >= 16:
            print("DROP DETECTED!")
            break
        else:
            # Walk back UP
            pos = walk_step("Up")
    else:
        print(f"Column {col} is blocked.")

print("Final position at end of script:", mgba.get_coordinates())
mgba.take_screenshot()
