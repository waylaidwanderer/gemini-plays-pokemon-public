import mgba
import time

def run_from_battle():
    print("In battle! Attempting to run...")
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 100"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 500"])
    for _ in range(4):
        mgba.press_buttons(["B", "sleep 100"])

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction, "sleep 150"])
    pos_after = mgba.get_coordinates()
    if pos_before == pos_after:
        mgba.press_buttons([direction, "sleep 150"])
        pos_after = mgba.get_coordinates()
        attempts = 0
        while pos_before == pos_after and attempts < 5:
            run_from_battle()
            mgba.press_buttons([direction, "sleep 150"])
            pos_after = mgba.get_coordinates()
            attempts += 1
    return pos_after

# 1. Walk UP Column 12 from current (12, 10) to Row 6 (12, 6)
print("1. Walking UP Column 12 to Row 6...")
pos = mgba.get_coordinates()
while pos['y'] > 6:
    pos = walk_step("Up")
print("Arrived on Row 6:", pos)

# 2. Test each column from 14 to 21
open_column = None
for col in range(14, 22):
    print(f"\n--- Testing Column {col} ---")
    # Walk horizontally on Row 6 to col
    pos = mgba.get_coordinates()
    curr_x = pos['x']
    while curr_x != col:
        if curr_x < col:
            pos = walk_step("Right")
        else:
            pos = walk_step("Left")
        curr_x = pos['x']
    print(f"Arrived at Row 6 Column {col}:", pos)
    
    # Try to walk DOWN to Row 8
    print("Attempting to walk DOWN 2 steps...")
    y_before = pos['y']
    pos = walk_step("Down")
    if pos['y'] == 7:
        pos = walk_step("Down")
        if pos['y'] == 8:
            print(f"SUCCESS: Column {col} is OPEN down to Row 8!")
            open_column = col
            # Walk back UP to Row 6
            walk_step("Up")
            walk_step("Up")
            break
        else:
            print(f"Blocked at Row 7 Column {col}.")
            # Walk back UP to Row 6
            walk_step("Up")
    else:
        print(f"Blocked at Row 6 Column {col}.")

if open_column is not None:
    print(f"FOUND OPEN PATH ON COLUMN {open_column}!")
else:
    print("All Columns 14-21 are BLOCKED on Row 7 on 3F East in State B.")
