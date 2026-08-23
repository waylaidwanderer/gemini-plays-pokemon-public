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

# Stand at (5, 8)
print("Walking to (5, 8)...")
walk_to(5, 8)

# Try columns 5, 4, 3, 2, 1
for col in [5, 4, 3, 2, 1]:
    print(f"Testing Column {col} for vertical passage to Row 6...")
    walk_to(col, 8)
    
    # Try to walk UP to Row 6
    success = False
    for step in range(3):
        pos_before = mgba.get_coordinates()
        walk_step("Up")
        pos_after = mgba.get_coordinates()
        if pos_before == pos_after:
            print(f"  Blocked at Row {pos_before['y']}")
            break
        if pos_after['y'] <= 6:
            print(f"  SUCCESS! Reached Row {pos_after['y']} on Column {col}!")
            success = True
            break
            
    if success:
        print(f"Verified Route: Column {col} is open to Row 6!")
        break
        
    # Reset back to Row 8
    walk_to(col, 8)
