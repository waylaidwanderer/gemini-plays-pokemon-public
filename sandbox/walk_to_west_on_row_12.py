import mgba
import time

print("Walking south down column 18 to row 12...")
path_down = [
    ('Down', 18, 6),
    ('Down', 18, 7),
    ('Down', 18, 8),
    ('Down', 18, 9),
    ('Down', 18, 10),
    ('Down', 18, 11),
    ('Down', 18, 12)
]

for btn, tx, ty in path_down:
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

# Now walk Left along row 12 to column 6 (or until blocked)
pos = mgba.get_coordinates()
if pos['y'] == 12:
    print("Walking Left on row 12...")
    for col in range(pos['x'] - 1, 1, -1):
        curr = mgba.get_coordinates()
        print(f"At {curr}, trying to walk Left to {col}")
        mgba.press_buttons(["Left"])
        time.sleep(0.3)
        new_pos = mgba.get_coordinates()
        if new_pos['x'] == curr['x']:
            print(f"Blocked at column {curr['x']}. Stopping.")
            break
else:
    print("Failed to reach row 12!")

print("Final position:", mgba.get_coordinates())
img = mgba.take_screenshot()
print("Screenshot:", img)
