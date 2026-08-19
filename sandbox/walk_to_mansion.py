import mgba
import time

print("Walking to the north-east side of Cinnabar Island...")

# We are at (15, 12).
# Walk Right 3 steps to (18, 12)
# Walk Up 9 steps to (18, 3)
# Then Walk Left to explore the top area!
path = [
    ('Right', 16, 12),
    ('Right', 17, 12),
    ('Right', 18, 12),
    ('Up', 18, 11),
    ('Up', 18, 10),
    ('Up', 18, 9),
    ('Up', 18, 8),
    ('Up', 18, 7),
    ('Up', 18, 6),
    ('Up', 18, 5),
    ('Up', 18, 4),
    ('Up', 18, 3)
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

# Now walk Left from (18, 3) to explore and find the Mansion entrance
pos = mgba.get_coordinates()
if pos['x'] == 18 and pos['y'] == 3:
    print("At (18, 3). Walking LEFT...")
    for col in range(17, 1, -1):
        curr = mgba.get_coordinates()
        print(f"At {curr}, trying to walk Left to {col}")
        mgba.press_buttons(["Left"])
        time.sleep(0.3)
        new_pos = mgba.get_coordinates()
        if new_pos['x'] == curr['x']:
            print(f"Blocked at column {curr['x']}. Stopping.")
            break

print("Final position:", mgba.get_coordinates())
img = mgba.take_screenshot()
print("Screenshot:", img)
