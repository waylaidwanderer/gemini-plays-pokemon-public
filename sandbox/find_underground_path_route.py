import mgba
import time

print("Starting Cerulean City Northbound Street Probe...")

# Step 1: Exit current building
mgba.press_buttons(["Down", "Down", "Down", "sleep 1000"])

pos = mgba.get_coordinates()
print(f"Position outside building: {pos}")
s_out = mgba.take_screenshot()
print(f"Outside screenshot: {s_out}")

# Player is outside at (13, 16)
# Walk to Row 20 (13, 20)
mgba.press_buttons(["Down", "Down", "Down", "Down", "sleep 300"])
p20 = mgba.get_coordinates()
print(f"Position on Row 20: {p20}")

# Test every column x from 13 down to 0, then 14 up to 40
open_north_cols = []

for test_x in [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]:
    curr = mgba.get_coordinates()
    # Move horizontally on Row 20 to test_x
    if curr['x'] < test_x:
        mgba.press_buttons(["Right"] * (test_x - curr['x']) + ["sleep 100"])
    elif curr['x'] > test_x:
        mgba.press_buttons(["Left"] * (curr['x'] - test_x) + ["sleep 100"])
    
    p_start = mgba.get_coordinates()
    print(f"Testing Column {p_start['x']} northbound from Row {p_start['y']}...")
    
    # Try walking Up 8 steps
    mgba.press_buttons(["Up"] * 8 + ["sleep 300"])
    p_up = mgba.get_coordinates()
    
    if p_up['y'] <= 12:
        print(f"FOUND OPEN NORTHBOUND STREET AT COLUMN {p_start['x']}! Reached ({p_up['x']}, {p_up['y']})!")
        s_open = mgba.take_screenshot()
        print(f"Northbound street screenshot: {s_open}")
        open_north_cols.append(p_start['x'])
        break
    else:
        # Step back Down to Row 20
        if p_up['y'] < p_start['y']:
            mgba.press_buttons(["Down"] * (p_start['y'] - p_up['y']) + ["sleep 100"])

print("Probe completed! Open Northbound Columns:", open_north_cols)
