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

# Dismiss any open text first
print("Dismissing any text...")
mgba.press_buttons(["B"])
time.sleep(0.5)

# Current position is (2, 12)
pos = mgba.get_coordinates()
print("Starting position:", pos)

# Step 1: Walk Down to Row 13, and Right to Column 12 Row 13, then UP to (12, 11)
print("Walking to (12, 11)...")
targets_12_11 = [(2, 13), (12, 13), (12, 11)]
for target in targets_12_11:
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

# Step 2: Try to walk Right towards the stairs at (15, 11)
print("Testing horizontal path to stairs on Row 11...")
for col in [13, 14, 15]:
    pos_before = pos
    pos = walk_step("Right")
    if pos == pos_before:
        print(f"Blocked trying to walk Right at Column {pos['x']}")
        break

print("Final position at end of script:", mgba.get_coordinates())
mgba.take_screenshot()
