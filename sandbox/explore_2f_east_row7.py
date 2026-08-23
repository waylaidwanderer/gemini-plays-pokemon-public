import mgba
import time

def run_from_battle():
    print("Stuck! Attempting to run from battle...")
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 150"])
    mgba.press_buttons(["Right", "sleep 150", "Down", "sleep 150", "A", "sleep 600"])
    for _ in range(4):
        mgba.press_buttons(["B", "sleep 150"])

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction, "sleep 150"])
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        mgba.press_buttons([direction, "sleep 150"])
        pos_after = mgba.get_coordinates()
        
        attempts = 0
        while pos_before == pos_after and attempts < 10:
            run_from_battle()
            mgba.press_buttons([direction, "sleep 150"])
            pos_after = mgba.get_coordinates()
            attempts += 1
    return pos_after

def walk_to(target_x, target_y):
    max_steps = 100
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

# Starting from (6, 10) on 2F West in State B
print("Starting position:", mgba.get_coordinates())

# 1. Walk to Row 3
print("1. Walking to (6, 3)...")
walk_to(6, 3)

# 2. Walk Right to Column 18 Row 3
print("2. Walking to (18, 3)...")
walk_to(18, 3)

# 3. Walk Down Column 18 to (18, 10) to warp DOWN to 1F East
print("3. Walking DOWN Column 18 to (18, 10) to warp to 1F East...")
walk_to(18, 10)

time.sleep(1.5) # Wait for warp
print("Position after warp attempt:", mgba.get_coordinates())

# Save screenshot to verify where we landed
screenshot_file = mgba.take_screenshot()
print("Screenshot saved to:", screenshot_file)
