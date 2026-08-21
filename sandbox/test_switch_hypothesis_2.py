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
        handle_battle()
        pos_after = mgba.get_coordinates()
    else:
        print(f"Moved to {pos_after}")
    return pos_after

# Current position is (2, 13)
pos = mgba.get_coordinates()

# Step 1: Walk to (1, 11) via Column 1
print("Walking to (1, 11)...")
if pos['x'] == 2 and pos['y'] == 13:
    pos = walk_step("Left")
while pos['y'] > 11:
    pos = walk_step("Up")

# Step 2: Face Right and toggle the Mewtwo statue switch at (2, 11)
if pos['x'] == 1 and pos['y'] == 11:
    print("Facing Right towards the statue switch...")
    mgba.press_buttons(["Right"])
    time.sleep(0.5)
    
    print("Toggling the switch...")
    mgba.press_buttons(["A", "sleep 600", "A", "sleep 600", "B", "sleep 200"])
    time.sleep(1.0)

# Step 3: Walk back to (12, 11) on Row 11
# Path: (1, 11) -> (1, 13) -> (12, 13) -> (12, 11)
print("Walking to (12, 11)...")
pos = walk_step("Down")
pos = walk_step("Down")
while pos['x'] < 12:
    pos = walk_step("Right")
while pos['y'] > 11:
    pos = walk_step("Up")

# Step 4: Walk Up Column 12 to Row 6 and then Right to Column 19 Row 6
print("Crossing to 3F East...")
while pos['y'] > 6:
    pos = walk_step("Up")
while pos['x'] < 19:
    pos = walk_step("Right")

# Step 5: Try walking Down Column 19 to Row 11
print("Testing Column 19 shutter gate...")
while pos['y'] < 11:
    pos_before = pos
    pos = walk_step("Down")
    if pos == pos_before:
        print("Column 19 gate is still closed.")
        break

print("Final position at end of script:", mgba.get_coordinates())
mgba.take_screenshot()
