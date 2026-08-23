import mgba
import time

def walk_to(target_x, target_y):
    max_steps = 50
    steps = 0
    while steps < max_steps:
        pos = mgba.get_coordinates()
        x, y = pos['x'], pos['y']
        if x == target_x and y == target_y:
            return True
            
        if x < target_x:
            mgba.press_buttons(["Right", "sleep 150"])
        elif x > target_x:
            mgba.press_buttons(["Left", "sleep 150"])
        elif y < target_y:
            mgba.press_buttons(["Down", "sleep 150"])
        elif y > target_y:
            mgba.press_buttons(["Up", "sleep 150"])
        steps += 1
    return False

def test_down_on_column(col):
    # Walk horizontally on Row 6 to col
    walk_to(col, 6)
        
    # Face DOWN and try to step DOWN
    mgba.press_buttons(["Down", "sleep 150"])
    pos_after = mgba.get_coordinates()
    if pos_after['y'] == 7:
        print(f"SUCCESS: Column {col} Row 7 is OPEN!")
        # Walk back UP to Row 6
        mgba.press_buttons(["Up", "sleep 150"])
        return True
    else:
        print(f"BLOCKED: Column {col} Row 7 is CLOSED.")
        return False

print("Systematic Row 7 test on 2F East starting...")
# Walk DOWN to (15, 6)
walk_to(15, 6)

# Test columns from 15 to 21
for c in range(15, 22):
    if test_down_on_column(c):
        break

# Test columns from 14 down to 14
pos = mgba.get_coordinates()
if pos['y'] == 6:
    test_down_on_column(14)
