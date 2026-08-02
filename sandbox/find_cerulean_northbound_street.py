import mgba
import time

print("=== STARTING CERULEAN CITY ALL-COLUMN NORTHBOUND PROBE ===")

start_pos = mgba.get_coordinates()
print(f"Start position: {start_pos}")

open_north_cols = []

# Probe columns from x=0 to x=35 on Row 20
cols_to_test = list(range(0, 36))

for test_x in cols_to_test:
    # Get current position
    curr = mgba.get_coordinates()
    
    # Return to Row 20 if needed
    if curr['y'] < 20:
        mgba.press_buttons(["Down"] * (20 - curr['y']) + ["sleep 50"])
    elif curr['y'] > 20:
        mgba.press_buttons(["Up"] * (curr['y'] - 20) + ["sleep 50"])
        
    curr = mgba.get_coordinates()
    
    # Move horizontally to test_x
    if curr['x'] < test_x:
        mgba.press_buttons(["Right"] * (test_x - curr['x']) + ["sleep 50"])
    elif curr['x'] > test_x:
        mgba.press_buttons(["Left"] * (curr['x'] - test_x) + ["sleep 50"])
        
    pos_at_col = mgba.get_coordinates()
    if pos_at_col['x'] != test_x or pos_at_col['y'] != 20:
        print(f"Col {test_x}: Blocked on Row 20 at {pos_at_col}")
        continue
        
    # Attempt walking Up 8 steps towards Row 12
    mgba.press_buttons(["Up"] * 8 + ["sleep 100"])
    pos_after_up = mgba.get_coordinates()
    
    delta_y = pos_at_col['y'] - pos_after_up['y']
    print(f"Col {test_x}: Moved Up {delta_y} steps (reached y={pos_after_up['y']})")
    
    if pos_after_up['y'] <= 12:
        open_north_cols.append((test_x, pos_after_up['y']))
        print(f"*** FOUND NORTHBOUND STREET AT COL {test_x}! Reached y={pos_after_up['y']} ***")
        
    # Return to Row 20
    curr_y = pos_after_up['y']
    if curr_y < 20:
        mgba.press_buttons(["Down"] * (20 - curr_y) + ["sleep 50"])

print("=== PROBE COMPLETE ===")
print(f"Summary of Northbound Openings (col, min_y): {open_north_cols}")
