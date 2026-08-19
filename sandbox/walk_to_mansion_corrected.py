import mgba
import time

print("Starting walk to Mansion via row 5...")

# We are at (15, 6).
# 1. Step UP to (15, 5)
# 2. Step LEFT to column 11
path = [
    ('Up', 15, 5),
    ('Left', 14, 5),
    ('Left', 13, 5),
    ('Left', 12, 5),
    ('Left', 11, 5),
    ('Left', 10, 5),
    ('Left', 9, 5),
    ('Left', 8, 5),
    ('Left', 7, 5),
    ('Left', 6, 5),
    ('Left', 5, 5)
]

for btn, tx, ty in path:
    pos = mgba.get_coordinates()
    print(f"Overworld: At {pos}, Next Step: {btn} to ({tx}, {ty})")
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
