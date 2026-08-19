import mgba
import time

print("Walking to the west side on row 4 to find the Mansion entrance...")

# We are at (11, 5).
# Path: Up to (11, 4), then Left to column 4
path = [
    ('Up', 11, 4),
    ('Left', 10, 4),
    ('Left', 9, 4),
    ('Left', 8, 4),
    ('Left', 7, 4),
    ('Left', 6, 4),
    ('Left', 5, 4),
    ('Left', 4, 4)
]

for btn, tx, ty in path:
    pos = mgba.get_coordinates()
    print(f"At {pos}, Next Step: {btn} to ({tx}, {ty})")
    mgba.press_buttons([btn])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == tx and new_pos['y'] == ty:
        print("Step succeeded.")
    else:
        print(f"Failed to step to ({tx}, {ty}). Current coordinate: {new_pos}")
        time.sleep(0.5)
        pos_check = mgba.get_coordinates()
        if pos_check == new_pos:
            print("Blocked. Stopping.")
            break
        else:
            print("Position changed, continuing...")

print("Final position:", mgba.get_coordinates())
img = mgba.take_screenshot()
print("Screenshot:", img)
