import mgba
import time

def handle_battle():
    # If coordinates didn't change and we are in a battle, we just print and exit
    # to let the agent handle it. But to be safe, we can try to flee once.
    print("Likely battle or solid wall. Attempting to flee once...")
    for _ in range(3):
        mgba.press_buttons(["B"])
        time.sleep(0.2)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.0)
    for _ in range(3):
        mgba.press_buttons(["B"])
        time.sleep(0.2)

def walk_step(tx, ty, d):
    pos = mgba.get_coordinates()
    if pos['x'] == tx and pos['y'] == ty:
        return True
    mgba.press_buttons([d])
    time.sleep(0.55)
    new_pos = mgba.get_coordinates()
    return new_pos['x'] == tx and new_pos['y'] == ty

# We are at (15, 7) on 1F East.
# Let's walk to Row 5: (15, 6) -> (15, 5).
print("Walking UP to Row 5...")
walk_step(15, 6, 'Up')
walk_step(15, 5, 'Up')

pos = mgba.get_coordinates()
print("Currently at Row 5:", pos)

if pos['y'] == 5:
    # Now let's walk left to Column 2
    for col in range(pos['x'] - 1, 1, -1):
        if not walk_step(col, 5, 'Left'):
            print(f"Failed to walk Left to Column {col}")
            break
            
    pos = mgba.get_coordinates()
    print("Reached West side on Row 5 at:", pos)
    
    # We are on the West side. Let's find which column allows walking DOWN to Row 11!
    # We will try columns from 2 to 10.
    start_col = pos['x']
    found_col = None
    for col in range(start_col, 11):
        # Walk to Column 'col' on Row 5
        print(f"Testing Column {col}...")
        # Walk horizontally to 'col'
        cur = mgba.get_coordinates()
        if cur['x'] < col:
            for c in range(cur['x'] + 1, col + 1):
                walk_step(c, 5, 'Right')
        elif cur['x'] > col:
            for c in range(cur['x'] - 1, col - 1, -1):
                walk_step(c, 5, 'Left')
                
        # Now try walking Down from Row 5 to Row 11 on Column 'col'
        cur = mgba.get_coordinates()
        if cur['x'] == col and cur['y'] == 5:
            # Try walking Down to Row 6, 7, 8, 9, 10, 11
            blocked = False
            for r in range(6, 12):
                if not walk_step(col, r, 'Down'):
                    print(f"  Column {col} is BLOCKED at Row {r}")
                    blocked = True
                    break
            if not blocked:
                print(f"  -> SUCCESS! Column {col} is fully walkable to Row 11!")
                found_col = col
                break
            else:
                # Walk back UP to Row 5 if we moved down a bit
                cur = mgba.get_coordinates()
                if cur['y'] > 5:
                    for r in range(cur['y'] - 1, 4, -1):
                        walk_step(col, r, 'Up')
                        
    if found_col:
        print(f"FOUND WALKABLE COLUMN TO ROW 11: {found_col}")
    else:
        print("No columns between current and 10 are fully walkable to Row 11 on Row 5.")

print("Final position after probe:", mgba.get_coordinates())
mgba.take_screenshot()
