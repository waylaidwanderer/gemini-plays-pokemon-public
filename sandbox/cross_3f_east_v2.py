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

# Current position is (6, 14) on 3F West
pos = mgba.get_coordinates()
print("Starting position:", pos)

# Step 1: Walk to Column 5 Row 11
print("Walking to Column 5 Row 11...")
if pos['x'] == 6 and pos['y'] == 14:
    pos = walk_step("Left")
while pos['y'] > 11:
    pos = walk_step("Up")

# Step 2: Walk Right on Row 11 to (7, 11)
while pos['x'] < 7:
    pos = walk_step("Right")

print("Arrived at (7, 11). Ready to bypass Hiker...")

# Step 3: Wait and bypass Hiker
# The Hiker wanders between (8, 11) and (9, 11)
# We want to walk Right to (8, 11), then Up to Row 10 (8, 10) to bypass him
stuck_count = 0
while pos['x'] < 8:
    pos_before = pos
    pos = walk_step("Right")
    if pos == pos_before:
        # Bumped, meaning Hiker is at (8, 11). Let's wait and try again.
        stuck_count += 1
        if stuck_count > 10:
            handle_battle()
            stuck_count = 0
            pos = mgba.get_coordinates()
        else:
            time.sleep(0.5)

# We are at (8, 11) now!
# Walk Up to (8, 10) to bypass him
pos = walk_step("Up")

# Walk Right along Row 10 to Column 12
while pos['x'] < 12:
    pos = walk_step("Right")

# Walk Down to (12, 11)
pos = walk_step("Down")

# Step 4: Walk Up Column 12 to Row 6 and then Right to Column 19
print("Walking to (19, 6)...")
while pos['y'] > 6:
    pos = walk_step("Up")
while pos['x'] < 19:
    pos = walk_step("Right")

# Step 5: Walk Down Column 19 to Row 11
print("Walking Down Column 19...")
while pos['y'] < 11:
    pos = walk_step("Down")

# Step 6: Walk Left to (15, 11) (the stairs) and warp
print("Walking to East stairs...")
while pos['x'] > 15:
    pos = walk_step("Left")

# Step 7: Step Left onto the stairs warp
print("Stepping onto stairs...")
pos = walk_step("Left")

print("Final position:", mgba.get_coordinates())
mgba.take_screenshot()
