import mgba
import time

print("Starting Cinnabar walk to the East side...")

# We are at (9, 10).
# Path: Left to 8, Down to 12, Right to 15
path = [
    ('Left', 8, 10),
    ('Down', 8, 11),
    ('Down', 8, 12),
    ('Right', 9, 12),
    ('Right', 10, 12),
    ('Right', 11, 12),
    ('Right', 12, 12),
    ('Right', 13, 12),
    ('Right', 14, 12),
    ('Right', 15, 12)
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
