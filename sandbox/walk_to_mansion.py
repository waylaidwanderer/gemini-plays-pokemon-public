import mgba
import time

print("Walking to the east side on row 12...")
path_right = [
    ('Right', 7, 12),
    ('Right', 8, 12),
    ('Right', 9, 12),
    ('Right', 10, 12),
    ('Right', 11, 12),
    ('Right', 12, 12),
    ('Right', 13, 12),
    ('Right', 14, 12),
    ('Right', 15, 12),
    ('Right', 16, 12),
    ('Right', 17, 12),
    ('Right', 18, 12)
]

for btn, tx, ty in path_right:
    pos = mgba.get_coordinates()
    mgba.press_buttons([btn])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == tx and new_pos['y'] == ty:
        pass
    else:
        print(f"Failed to step to ({tx}, {ty}). Current coordinate: {new_pos}")
        break

# Now walk UP column 18 to row 6
print("Walking UP column 18 to row 6...")
path_up = [
    ('Up', 18, 11),
    ('Up', 18, 10),
    ('Up', 18, 9),
    ('Up', 18, 8),
    ('Up', 18, 7),
    ('Up', 18, 6)
]

for btn, tx, ty in path_up:
    pos = mgba.get_coordinates()
    mgba.press_buttons([btn])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == tx and new_pos['y'] == ty:
        pass
    else:
        print(f"Failed UP step to ({tx}, {ty}). Current coordinate: {new_pos}")
        break

# Try to walk LEFT on row 6 to column 6
print("Walking LEFT on row 6 towards the west side...")
path_left = [
    ('Left', 17, 6),
    ('Left', 16, 6),
    ('Left', 15, 6),
    ('Left', 14, 6),
    ('Left', 13, 6),
    ('Left', 12, 6),
    ('Left', 11, 6),
    ('Left', 10, 6),
    ('Left', 9, 6),
    ('Left', 8, 6),
    ('Left', 7, 6),
    ('Left', 6, 6)
]

blocked_col = None
for btn, tx, ty in path_left:
    pos = mgba.get_coordinates()
    mgba.press_buttons([btn])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == tx and new_pos['y'] == ty:
        pass
    else:
        print(f"Row 6: Blocked at column {pos['x']} when trying to go Left to {tx}")
        blocked_col = pos['x']
        break

print("Final position after Row 6 test:", mgba.get_coordinates())
img = mgba.take_screenshot()
print("Screenshot:", img)
