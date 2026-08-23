import mgba
import time

def run_from_battle():
    print("In battle! Running...")
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 100"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 500"])
    for _ in range(4):
        mgba.press_buttons(["B", "sleep 100"])

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction, "sleep 150"])
    pos_after = mgba.get_coordinates()
    if pos_before == pos_after:
        mgba.press_buttons([direction, "sleep 150"])
        pos_after = mgba.get_coordinates()
        attempts = 0
        while pos_before == pos_after and attempts < 5:
            run_from_battle()
            mgba.press_buttons([direction, "sleep 150"])
            pos_after = mgba.get_coordinates()
            attempts += 1
    return pos_after

# Starting from (13, 12)
print("Starting switch test on the Mewtwo statue at (13, 11)...")

# 1. Walk Left to (12, 12)
print("1. Walking Left to (12, 12)...")
walk_step("Left")

# 2. Walk Up to (12, 11)
print("2. Walking Up to (12, 11)...")
walk_step("Up")

# 3. Turn Right to face (13, 11)
print("3. Facing Right towards (13, 11)...")
walk_step("Right") # This will bump/face Right

# Take screenshot before pressing A
mgba.take_screenshot()

# 4. Press A
print("4. Pressing A to check for switch...")
mgba.press_buttons(["A", "sleep 500", "B", "sleep 150"])

# Take screenshot
mgba.take_screenshot()

print("Final position:", mgba.get_coordinates())
