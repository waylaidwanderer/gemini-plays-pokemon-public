import mgba
import os
import time

# Cleanup obsolete scratchpad
if os.path.exists("notepads/Scratchpad/Route_8_Navigation.md"):
    os.remove("notepads/Scratchpad/Route_8_Navigation.md")
    print("Deleted obsolete scratchpad Route_8_Navigation.md")

print("Starting Master Cerulean City Northbound Street Finder...")

pos = mgba.get_coordinates()
print(f"Starting position in Cerulean City: {pos}")

# Test candidate columns on Row 20 for a clear northbound passage to Row 12
candidate_cols = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

found_col = None

for test_x in candidate_cols:
    curr = mgba.get_coordinates()
    # If we are not on Row 20, move back to Row 20
    if curr['y'] != 20:
        if curr['y'] < 20:
            mgba.press_buttons(["Down"] * (20 - curr['y']) + ["sleep 100"])
        elif curr['y'] > 20:
            mgba.press_buttons(["Up"] * (curr['y'] - 20) + ["sleep 100"])
    
    curr = mgba.get_coordinates()
    # Move horizontally to test_x
    if curr['x'] < test_x:
        mgba.press_buttons(["Right"] * (test_x - curr['x']) + ["sleep 100"])
    elif curr['x'] > test_x:
        mgba.press_buttons(["Left"] * (curr['x'] - test_x) + ["sleep 100"])
    
    p_start = mgba.get_coordinates()
    if p_start['x'] != test_x or p_start['y'] != 20:
        continue # Blocked horizontally
    
    # Try walking Up 8 steps toward Row 12
    mgba.press_buttons(["Up"] * 8 + ["sleep 200"])
    p_up = mgba.get_coordinates()
    
    # Check if we moved up successfully past y=15
    if p_up['y'] <= 12:
        print(f"FOUND OPEN NORTHBOUND STREET AT COLUMN {test_x}! Reached ({p_up['x']}, {p_up['y']})!")
        found_col = test_x
        s = mgba.take_screenshot()
        print(f"Open street screenshot: {s}")
        break
    else:
        # Step back Down to Row 20
        if p_up['y'] < 20:
            mgba.press_buttons(["Down"] * (20 - p_up['y']) + ["sleep 100"])

print("Probe completed! Open Northbound Columns:", open_north_cols if 'open_north_cols' in locals() else [found_col])
