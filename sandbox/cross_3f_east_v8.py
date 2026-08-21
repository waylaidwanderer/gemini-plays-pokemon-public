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

# Starting from (6, 11) on 3F West (State A)
pos = mgba.get_coordinates()
print("Starting position:", pos)

# Step 1: Walk to (8, 10) via (7, 11) -> (8, 11) -> (8, 10)
print("Walking to (8, 10)...")
if pos['x'] == 6 and pos['y'] == 11:
    pos = walk_step("Right")
if pos['x'] == 7 and pos['y'] == 11:
    pos = walk_step("Right")
if pos['x'] == 8 and pos['y'] == 11:
    pos = walk_step("Up")

# Step 2: Walk Right along Row 10 to Column 13
print("Walking Right to Column 13...")
while pos['x'] < 13:
    pos = walk_step("Right")

# Step 3: Walk Up Column 13 to Row 6
print("Walking Up Column 13 to Row 6...")
while pos['y'] > 6:
    pos = walk_step("Up")

# Step 4: Walk Right along Row 6 to Column 19
print("Walking Right to Column 19...")
while pos['x'] < 19:
    pos = walk_step("Right")

# Step 5: Walk Down Column 19 to Row 11
print("Walking Down Column 19...")
while pos['y'] < 11:
    pos_before = pos
    pos = walk_step("Down")
    if pos == pos_before:
        print("CRITICAL: Column 19 is still blocked!")
        handle_battle()
        pos = mgba.get_coordinates()

# Step 6: Walk Left along Row 11 to (15, 11) (the stairs) and warp
if pos['x'] == 19 and pos['y'] == 11:
    print("Walking to East stairs...")
    while pos['x'] > 15:
        pos = walk_step("Left")
    
    print("Stepping onto stairs...")
    pos = walk_step("Left")

print("Final position at end of script:", mgba.get_coordinates())
mgba.take_screenshot()
