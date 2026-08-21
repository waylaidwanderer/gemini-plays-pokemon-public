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

# Starting from (6, 13) on 3F West (State A)
pos = mgba.get_coordinates()
print("Starting position:", pos)

# Step 1: Walk UP to Row 11
print("Walking UP to Row 11...")
while pos['y'] > 11:
    pos = walk_step("Up")

# Step 2: Walk Right along Row 11 to Column 15 (the stairs)
print("Walking Right to Column 15...")
while pos['x'] < 15:
    pos_before = pos
    pos = walk_step("Right")
    if pos == pos_before:
        # If we bump, let's see if it's an NPC or wall
        print(f"Bumped at {pos} going Right")
        time.sleep(0.5)

print("Standing at stairs candidate:", mgba.get_coordinates())
time.sleep(1.5)
print("Final coordinates:", mgba.get_coordinates())
mgba.take_screenshot()
