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

def walk_to(target_x, target_y):
    max_steps = 30
    steps = 0
    while steps < max_steps:
        pos = mgba.get_coordinates()
        x, y = pos['x'], pos['y']
        if x == target_x and y == target_y:
            return True
        if x < target_x:
            walk_step("Right")
        elif x > target_x:
            walk_step("Left")
        elif y < target_y:
            walk_step("Down")
        elif y > target_y:
            walk_step("Up")
        steps += 1
    return False

# Starting from (19, 7) in State A
print("Starting switch test at (12, 12)...")
print("Initial position:", mgba.get_coordinates())

# 1. Walk LEFT on Row 7 to Column 16
print("1. Walking LEFT to Column 16...")
pos = mgba.get_coordinates()
while pos['x'] > 16:
    pos = walk_step("Left")

# 2. Walk DOWN Column 16 to Row 9
print("2. Walking DOWN to Row 9...")
while pos['y'] < 9:
    pos = walk_step("Down")

# 3. Walk LEFT on Row 9 to Column 12
print("3. Walking LEFT to Column 12...")
while pos['x'] > 12:
    pos = walk_step("Left")

# 4. Walk DOWN Column 12 to Row 11
print("4. Walking DOWN to Row 11...")
while pos['y'] < 11:
    pos = walk_step("Down")

print("Arrived at:", mgba.get_coordinates())

# Face DOWN (to look at (12, 12))
print("Facing DOWN...")
walk_step("Down") # Should bump and face Down
print("Final position before pressing A:", mgba.get_coordinates())

# Take screenshot
mgba.take_screenshot()

# Press A
print("Pressing A to check for secret switch...")
mgba.press_buttons(["A", "sleep 300", "A", "sleep 300"])

# Take screenshot to capture text box
mgba.take_screenshot()
