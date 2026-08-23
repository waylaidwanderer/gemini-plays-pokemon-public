import mgba
import time

def test_down_on_column(col):
    # Walk horizontally on Row 6 to col
    pos = mgba.get_coordinates()
    curr_x = pos['x']
    while curr_x != col:
        if curr_x < col:
            mgba.press_buttons(["Right", "sleep 150"])
        else:
            mgba.press_buttons(["Left", "sleep 150"])
        pos = mgba.get_coordinates()
        curr_x = pos['x']
        
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

print("Starting systematic Row 7 vertical path search...")
# Test columns from 19 down to 14
for c in range(19, 13, -1):
    if test_down_on_column(c):
        break

# Test columns from 20 to 22
pos = mgba.get_coordinates()
if pos['y'] == 6: # if we are still on Row 6
    for c in range(20, 23):
        if test_down_on_column(c):
            break
