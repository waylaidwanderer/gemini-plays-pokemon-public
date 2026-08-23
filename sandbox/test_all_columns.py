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

# Starting from (5, 11) on 2F West in State B
print("1. Walking to 2F East Row 3 Column 15...")
walk_to(5, 3)
walk_to(15, 3)
print("Arrived on 2F East Row 3. Position:", mgba.get_coordinates())

# 2. Walk to Column 21 Row 3
print("2. Walking to Column 21 Row 3...")
walk_to(21, 3)

# 3. Walk DOWN Column 21 to Row 11
print("3. Attempting to walk DOWN Column 21 to Row 11...")
success = True
for target_y in range(4, 12):
    pos_before = mgba.get_coordinates()
    walk_step("Down")
    pos_after = mgba.get_coordinates()
    if pos_before['y'] == pos_after['y']:
        print(f"  Blocked at Row {pos_before['y']} on Column 21!")
        success = False
        break

if success:
    print("SUCCESS! Column 21 is fully open vertically down to Row 11! Position:", mgba.get_coordinates())
    # Walk left to stairs at (15, 11)
    print("4. Walking left to stairs at (15, 11)...")
    walk_to(15, 11)
    print("Arrived at stairs! Position:", mgba.get_coordinates())
else:
    print("Column 21 was blocked. Let's try testing other columns (20, 19, 18) from Row 3 down...")
    for col in [20, 19, 18]:
        print(f"Testing Column {col}...")
        walk_to(col, 3)
        col_success = True
        for target_y in range(4, 12):
            pos_before = mgba.get_coordinates()
            walk_step("Down")
            pos_after = mgba.get_coordinates()
            if pos_before['y'] == pos_after['y']:
                print(f"  Column {col} blocked at Row {pos_before['y']}!")
                col_success = False
                break
        if col_success:
            print(f"SUCCESS! Column {col} is fully open! Position:", mgba.get_coordinates())
            break
        # Go back to Row 3
        walk_to(col, 3)

