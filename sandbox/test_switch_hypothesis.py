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

def test_column(col):
    print(f"Testing Column {col}...")
    walk_to(col, 13) # Walk to Row 13 (which is fully open)
    
    # Try to walk UP to Row 9
    max_y = 13
    for target_y in range(12, 8, -1):
        pos_before = mgba.get_coordinates()
        walk_step("Up")
        pos_after = mgba.get_coordinates()
        if pos_before['y'] == pos_after['y']:
            print(f"  Blocked at Row {pos_before['y']}!")
            break
        max_y = pos_after['y']
    
    print(f"  Column {col} reached max_y={max_y}")
    walk_to(col, 13)

# Starting from (2, 12)
print("Starting systematic State B vertical path test...")
for col in [2, 3, 4, 5, 6]:
    test_column(col)

print("Test complete! Final position:", mgba.get_coordinates())
