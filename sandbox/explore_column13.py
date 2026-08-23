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

print("Testing Column 13 horizontal crossings...")
# Walk back to Column 12 on Row 6
walk_to(12, 6)

for r in range(7, 16):
    print(f"Testing Row {r} crossing...")
    # Walk DOWN Column 12 to row r
    walk_to(12, r)
    # Try to walk RIGHT to Column 13
    mgba.press_buttons(["Right", "sleep 150"])
    pos = mgba.get_coordinates()
    if pos['x'] == 13:
        print(f"SUCCESS: Row {r} Column 13 is OPEN!")
        # Walk back LEFT to Column 12
        mgba.press_buttons(["Left", "sleep 150"])
    else:
        print(f"BLOCKED: Row {r} Column 13 is CLOSED.")
