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

# We are at (2, 12) on 2F West in State B
print("Current position:", mgba.get_coordinates())

# Walk to 2F West (5, 11) then up Column 5 to Row 3
print("Walking to (5, 3)...")
walk_to(5, 11)
walk_to(5, 3)
print("Position on 2F West Row 3:", mgba.get_coordinates())

# Cross to 2F East at (15, 3)
print("Crossing horizontally on Row 3 to 2F East...")
walk_to(15, 3)
print("Position on 2F East:", mgba.get_coordinates())

# Now we systematically test Columns 21, 20, 19, 18, 17, 16, 15 from Row 3 down to Row 11
for col in [21, 20, 19, 18, 17, 16, 15]:
    print(f"Testing Column {col}...")
    walk_to(col, 3)
    col_success = True
    for row in range(4, 12):
        pos_before = mgba.get_coordinates()
        walk_step("Down")
        pos_after = mgba.get_coordinates()
        if pos_before['y'] == pos_after['y']:
            print(f"  Column {col} blocked at Row {pos_before['y']}!")
            col_success = False
            break
    if col_success:
        print(f"SUCCESS! Column {col} is fully open from Row 3 to Row 11! Current position:", mgba.get_coordinates())
        # Let's save screenshot
        screenshot_file = mgba.take_screenshot()
        print("Screenshot saved to:", screenshot_file)
        break
    else:
        # Move back to Row 3
        walk_to(col, 3)

print("Final position:", mgba.get_coordinates())
