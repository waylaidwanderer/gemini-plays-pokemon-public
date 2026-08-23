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

print("Starting cross_2f_west_to_3f_east from:", mgba.get_coordinates())

# 1. Warp UP to 3F West from (6, 13)
print("Walking to (7, 11)...")
walk_to(7, 11)
print("Stepping UP to warp...")
walk_step("Up")
time.sleep(1.0)
print("Position on 3F West:", mgba.get_coordinates())

# 2. Cross horizontally to 3F East (12, 11) -> (14, 11) -> (15, 11)
print("Crossing horizontally on Row 11...")
walk_to(12, 11)
walk_to(14, 11)
print("Stepping Right to warp down...")
walk_step("Right")
time.sleep(1.0)

print("Final position on 2F East:", mgba.get_coordinates())
screenshot_file = mgba.take_screenshot()
print("Screenshot saved to:", screenshot_file)
