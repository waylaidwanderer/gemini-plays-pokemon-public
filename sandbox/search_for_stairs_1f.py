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

# We are currently at (14, 6) inside the Mansion 1F.
# Let's systematically test walking onto every tile on Row 6, Row 5, Row 7 to find if any of them is a staircase/warp!
pos = mgba.get_coordinates()
print("Starting search for stairs on 1F from:", pos)

# We will walk left along Row 6 and test walking Up onto Row 5/4/3 and Down onto Row 7
# At each column from 14 down to 2:
for col in range(14, 1, -1):
    # Walk left to Column col
    cur = mgba.get_coordinates()
    if cur['x'] > col:
        for c in range(cur['x'] - 1, col - 1, -1):
            walk_step(c, 6, 'Left')
            
    cur = mgba.get_coordinates()
    if cur['x'] == col and cur['y'] == 6:
        print(f"Testing Column {col}...")
        
        # Test walking UP to Row 5 (if not blocked)
        if walk_step(col, 5, 'Up'):
            # Test walking UP to Row 4 (if not blocked)
            if walk_step(col, 4, 'Up'):
                # Test walking UP to Row 3 (if not blocked)
                if walk_step(col, 3, 'Up'):
                    # Walk back down to Row 5
                    walk_step(col, 4, 'Down')
                    walk_step(col, 5, 'Down')
                # Walk back down to Row 5
                walk_step(col, 5, 'Down')
            # Walk back down to Row 6
            walk_step(col, 6, 'Down')
            
        # Test walking DOWN to Row 7 (if not blocked)
        if walk_step(col, 7, 'Down'):
            # Walk back up to Row 6
            walk_step(col, 6, 'Up')

print("Finished stairs search. Current position:", mgba.get_coordinates())
mgba.take_screenshot()
