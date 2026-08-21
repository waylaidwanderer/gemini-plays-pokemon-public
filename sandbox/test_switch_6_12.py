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

# Step 1: Walk to (5, 12)
print("Walking to (5, 12)...")
while pos['x'] < 5:
    pos = walk_step("Right")

# Step 2: Face Right towards the Mewtwo statue at (6, 12)
print("Facing Right...")
mgba.press_buttons(["Right"])
time.sleep(0.5)

# Step 3: Press A to interact
print("Interacting with statue at (6, 12)...")
mgba.press_buttons(["A"])
time.sleep(1.0)

# Capture screenshot to see the dialogue
print("Taking screenshot of the dialogue...")
screenshot_path = mgba.take_screenshot()
print("Screenshot saved to:", screenshot_path)
