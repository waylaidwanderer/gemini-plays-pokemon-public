import mgba
import time

def handle_battle():
    print("Coordinates did not change. Likely a battle! Attempting to flee...")
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.0)
    for _ in range(4):
        mgba.press_buttons(["B"])
        time.sleep(0.3)

def walk_step(tx, ty, direction):
    pos = mgba.get_coordinates()
    if pos['x'] == tx and pos['y'] == ty:
        return True
    mgba.press_buttons([direction])
    time.sleep(0.55)
    new_pos = mgba.get_coordinates()
    if new_pos == pos:
        return False
    return True

# We are at (26, 7).
# Let's walk to Column 23, and test going Left on different rows to see which Row is open past Column 22!
print("Walking to (23, 7)...")
for x in range(25, 22, -1):
    if not walk_step(x, 7, 'Left'):
        print(f"Bumped at {mgba.get_coordinates()} going Left on Row 7")
        handle_battle()

# Let's test Row 10, Row 11, Row 12, Row 13, Row 14, Row 15, etc.
# We will walk down Column 23 and test Left at each row.
print("Testing Row Left passages...")
for y in range(7, 18):
    pos = mgba.get_coordinates()
    # If we are not at Column 23, walk back to Column 23
    if pos['x'] != 23:
        for x in range(pos['x']+1, 24):
            walk_step(x, pos['y'], 'Right')
            
    # Walk to Row y
    current_y = mgba.get_coordinates()['y']
    if current_y < y:
        for cy in range(current_y+1, y+1):
            if not walk_step(23, cy, 'Down'):
                print(f"Bumped going Down to Row {cy}")
                handle_battle()
                break
                
    pos = mgba.get_coordinates()
    if pos['y'] == y and pos['x'] == 23:
        print(f"Testing Left at Row {y}...")
        # Try to walk Left to Column 21
        if walk_step(22, y, 'Left'):
            if walk_step(21, y, 'Left'):
                print(f"SUCCESS: Row {y} is OPEN past Column 22!")
                # Walk back to Column 23
                walk_step(22, y, 'Right')
                walk_step(23, y, 'Right')
            else:
                print(f"Row {y} blocked at Column 21")
                walk_step(23, y, 'Right')
        else:
            print(f"Row {y} blocked at Column 22")
            
mgba.take_screenshot()
