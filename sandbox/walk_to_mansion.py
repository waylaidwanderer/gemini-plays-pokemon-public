import mgba
import time

print("Closing the locked door dialogue box...")
mgba.press_buttons(["B"])
time.sleep(0.5)

# Verify we are at (18, 4)
pos = mgba.get_coordinates()
print("Position after closing dialogue:", pos)

# Walk Left on row 4 from column 18 to column 6
path_left = [
    ('Left', 17, 4),
    ('Left', 16, 4),
    ('Left', 15, 4),
    ('Left', 14, 4),
    ('Left', 13, 4),
    ('Left', 12, 4),
    ('Left', 11, 4),
    ('Left', 10, 4),
    ('Left', 9, 4),
    ('Left', 8, 4),
    ('Left', 7, 4),
    ('Left', 6, 4)
]

print("Walking Left towards the Mansion...")
for btn, tx, ty in path_left:
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

# Now we are at (6, 4) or similar. Let's try to walk UP to enter the Mansion!
pos = mgba.get_coordinates()
print(f"At {pos}. Let's find the Mansion door by walking UP...")

# Try walking UP on column 6
for row in [3, 2, 1]:
    curr = mgba.get_coordinates()
    print(f"At {curr}, trying to walk UP to row {row}...")
    mgba.press_buttons(["Up"])
    time.sleep(1.5) # Wait for possible map transition warp!
    new_pos = mgba.get_coordinates()
    if new_pos['x'] != curr['x'] or new_pos['y'] != curr['y']:
        print(f"Warp or step succeeded! Landed at: {new_pos}")
        break
    else:
        print("Step failed or blocked.")

print("Final position:", mgba.get_coordinates())
img = mgba.take_screenshot()
print("Screenshot:", img)
