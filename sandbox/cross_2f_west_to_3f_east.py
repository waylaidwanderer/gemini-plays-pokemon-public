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

print("Phase 2 Part 2: Walking from (10, 3) on 2F East back to 3F West, and crossing to 3F East (12, 9)...")

# 1. Walk DOWN Column 10 to Row 11
walk_to(10, 11)
# 2. Walk LEFT along Row 11 to Column 7
walk_to(7, 11)
# 3. Step UP onto stairs to warp UP to 3F West
walk_step("Up")
time.sleep(1.0)
print("Arrived on 3F West. Position:", mgba.get_coordinates())

# 4. Walk UP Column 7 to Row 9
walk_to(7, 9)
# 5. Walk RIGHT along Row 9 to Column 12 on 3F East (OPEN in State B!)
walk_to(12, 9)

print("Successfully crossed to 3F East! Position:", mgba.get_coordinates())
