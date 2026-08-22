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

# Currently at (10, 7) on 1F West
pos = mgba.get_coordinates()
print("Starting column test from:", pos)

if pos['x'] == 10 and pos['y'] == 7:
    # Walk left along Row 7 and test walking DOWN at each column
    for col in range(10, 1, -1):
        # Walk Left to column
        cur = mgba.get_coordinates()
        if cur['x'] > col:
            # We need to walk Left to 'col' on Row 7
            for c in range(cur['x'] - 1, col - 1, -1):
                walk_step(c, 7, 'Left')
        elif cur['x'] < col:
            # Walk Right to 'col' on Row 7
            for c in range(cur['x'] + 1, col + 1):
                walk_step(c, 7, 'Right')
                
        # Now we are at (col, 7). Let's test walking DOWN to Row 11
        cur = mgba.get_coordinates()
        if cur['x'] == col and cur['y'] == 7:
            reached = 7
            for r in range(8, 12):
                if walk_step(col, r, 'Down'):
                    reached = r
                else:
                    break
            print(f"Column {col} reached down to Row {reached}")
            
            if reached == 11:
                print(f"!!! SUCCESS !!! Column {col} is a fully walkable vertical passage to Row 11!")
                break
                
            # Walk back UP to Row 7 if we moved down
            cur = mgba.get_coordinates()
            if cur['y'] > 7:
                for r in range(cur['y'] - 1, 6, -1):
                    walk_step(col, r, 'Up')

print("\nFinal position of column test:", mgba.get_coordinates())
mgba.take_screenshot()
