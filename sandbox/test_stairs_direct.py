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

# Starting from (12, 11) on 3F West (State A)
pos = mgba.get_coordinates()
print("Starting position:", pos)

# Step 1: Walk to the 3F West switch at (2, 12)
print("Walking to switch at (2, 12)...")
targets_switch = [(12, 13), (2, 13), (2, 12)]
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

# Step 2: Walk to Column 6 Row 6 in State B
print("Walking to Column 6 Row 6...")
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

# Step 3: Walk Right along Row 6 to Column 19 on 3F East
print("Walking Right to Column 19 on 3F East...")
while pos['x'] < 19:
    pos = walk_step("Right")

# Step 4: Walk Down Column 19 to Row 11
print("Walking Down Column 19...")
while pos['y'] < 11:
    pos_before = pos
    pos = walk_step("Down")
    if pos == pos_before:
        print("CRITICAL: Column 19 is still blocked!")
        handle_battle()
        pos = mgba.get_coordinates()

# Step 5: Walk Left along Row 11 to (15, 11) (the stairs) and warp
if pos['x'] == 19 and pos['y'] == 11:
    print("Walking to East stairs...")
    while pos['x'] > 15:
        pos = walk_step("Left")
    
    print("Stepping onto stairs...")
    pos = walk_step("Left")

print("Final position at end of script:", mgba.get_coordinates())
mgba.take_screenshot()
