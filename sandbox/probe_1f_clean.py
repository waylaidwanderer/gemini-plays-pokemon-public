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

# Start at (10, 6)
pos = mgba.get_coordinates()
print("Starting clean probe from:", pos)

# 1. Walk left along Row 6 to Column 2
if pos['y'] == 6:
    for col in range(pos['x'] - 1, 1, -1):
        if not walk_step(col, 6, 'Left'):
            print(f"Failed to go Left to ({col}, 6)")
            break

# Now we are at (2, 6) or near it.
pos = mgba.get_coordinates()
print("At West side on Row 6:", pos)

# We will test Column 2, 3, 4, 5, 6, 7, 8, 9, 10
# For each column, we walk to it on Row 6, and try to walk DOWN to Row 11.
for col in range(pos['x'], 11):
    print(f"\n--- PROBING COLUMN {col} ---")
    # Walk to (col, 6)
    cur = mgba.get_coordinates()
    if cur['x'] < col:
        for c in range(cur['x'] + 1, col + 1):
            walk_step(c, 6, 'Right')
    elif cur['x'] > col:
        for c in range(cur['x'] - 1, col - 1, -1):
            walk_step(c, 6, 'Left')
            
    cur = mgba.get_coordinates()
    if cur['x'] == col and cur['y'] == 6:
        # Try to walk down to Row 11
        reached = 6
        for r in range(7, 12):
            if walk_step(col, r, 'Down'):
                reached = r
            else:
                break
        print(f"Column {col} can reach down to Row {reached}")
        
        # Walk back UP to Row 6 if we moved down
        cur = mgba.get_coordinates()
        if cur['y'] > 6:
            for r in range(cur['y'] - 1, 5, -1):
                walk_step(col, r, 'Up')

print("\nFinal position after clean probe:", mgba.get_coordinates())
mgba.take_screenshot()
