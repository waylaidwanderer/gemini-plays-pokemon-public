import mgba
import time

def walk_step(tx, ty, d):
    pos = mgba.get_coordinates()
    if pos['x'] == tx and pos['y'] == ty:
        return True
    mgba.press_buttons([d])
    time.sleep(0.55)
    new_pos = mgba.get_coordinates()
    return new_pos['x'] == tx and new_pos['y'] == ty

# Start at (2, 6)
print("Starting systematic 1F West vertical probe...")

# Walk UP 1 step to (2, 6) to clear warp
walk_step(2, 6, 'Up')

pos = mgba.get_coordinates()
if pos['x'] == 2 and pos['y'] == 6:
    for col in range(2, 11):
        print(f"\n--- PROBING WEST COLUMN {col} ---")
        # Walk to Column 'col' on Row 6
        cur = mgba.get_coordinates()
        if cur['x'] < col:
            success = True
            for c in range(cur['x'] + 1, col + 1):
                if not walk_step(c, 6, 'Right'):
                    print(f"Failed to go Right to ({c}, 6)")
                    success = False
                    break
            if not success:
                continue
                
        # Try to walk down Column 'col' to Row 11
        reached = 6
        for r in range(7, 12):
            if walk_step(col, r, 'Down'):
                reached = r
            else:
                break
        print(f"Column {col} reached down to Row {reached}")
        
        if reached == 11:
            print(f"!!! SUCCESS !!! Column {col} is a fully open vertical passage to Row 11!")
            break
            
        # Walk back UP to Row 6 if we moved down
        cur = mgba.get_coordinates()
        if cur['y'] > 6:
            for r in range(cur['y'] - 1, 5, -1):
                walk_step(col, r, 'Up')

print("\nFinal position of probe:", mgba.get_coordinates())
mgba.take_screenshot()
