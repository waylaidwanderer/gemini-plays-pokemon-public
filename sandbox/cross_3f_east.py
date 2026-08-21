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

# Starting from (7, 15) on 3F West
pos = mgba.get_coordinates()
print("Starting position:", pos)

# Step 1: Walk to (7, 11)
print("Walking to (7, 11)...")
if pos['x'] == 7 and pos['y'] == 15:
    pos = walk_step("Up") # (7, 14)
while pos['x'] > 5:
    pos = walk_step("Left")
while pos['y'] > 11:
    pos = walk_step("Up")
while pos['x'] < 7:
    pos = walk_step("Right")

print("Arrived at (7, 11) or nearby:", pos)

# Step 2: Bypass the Hiker NPC at (8, 11)
print("Waiting and trying to walk Right to (8, 11)...")
stuck_time = 0
while pos['x'] < 8:
    # Try to walk Right
    pos_before = pos
    pos = walk_step("Right")
    if pos == pos_before:
        # We bumped, which means the NPC is still there. Let's wait a moment and try again.
        stuck_time += 1
        if stuck_time > 15:
            # If we've been stuck for too long, maybe we entered a battle
            handle_battle()
            stuck_time = 0
            pos = mgba.get_coordinates()
        else:
            time.sleep(0.5)

print("Successfully bypassed Hiker NPC! Current position:", pos)

# Step 3: Walk to (12, 11)
while pos['x'] < 12:
    pos = walk_step("Right")

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

# Step 7: Step onto the stairs at (15, 11) (by moving Right or Down if needed, wait, the landing of East stairs is at (15, 11)?)
# Actually, the stairs warp is at (15, 11). Just standing on it should trigger warp.
# If not, let's step Left or Up onto it.
print("Stepping onto stairs...")
pos = walk_step("Left")

print("Final position at end of script:", mgba.get_coordinates())
mgba.take_screenshot()
