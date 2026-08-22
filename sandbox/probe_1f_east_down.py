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

# Start at (17, 5)
pos = mgba.get_coordinates()
print("Starting East side DOWN probe from:", pos)

# We will test columns 11, 12, 13, 14, 15, 16, 17
for col in range(17, 10, -1):
    print(f"\n--- PROBING EAST COLUMN {col} ---")
    # Walk to (col, 5)
    cur = mgba.get_coordinates()
    if cur['x'] < col:
        for c in range(cur['x'] + 1, col + 1):
            walk_step(c, 5, 'Right')
    elif cur['x'] > col:
        for c in range(cur['x'] - 1, col - 1, -1):
            walk_step(c, 5, 'Left')
            
    cur = mgba.get_coordinates()
    if cur['x'] == col and cur['y'] == 5:
        # Try walking Down to Row 11
        reached = 5
        for r in range(6, 12):
            if walk_step(col, r, 'Down'):
                reached = r
            else:
                break
        print(f"East Column {col} can reach down to Row {reached}")
        
        # Walk back UP to Row 5 if we moved down
        cur = mgba.get_coordinates()
        if cur['y'] > 5:
            for r in range(cur['y'] - 1, 4, -1):
                walk_step(col, r, 'Up')

print("\nFinal position after East probe:", mgba.get_coordinates())
mgba.take_screenshot()
