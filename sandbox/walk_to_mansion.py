import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

print("Walking to the east side on row 12...")
path_right = [
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
        print(f"Failed step to ({tx}, {ty})")

print("Walking UP column 18 to row 5...")
path_up = [
    ('Up', 18, 11),
    ('Up', 18, 10),
    ('Up', 18, 9),
    ('Up', 18, 8),
    ('Up', 18, 7),
    ('Up', 18, 6),
    ('Up', 18, 5)
]

for btn, tx, ty in path_up:
    pos = mgba.get_coordinates()
    mgba.press_buttons([btn])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == tx and new_pos['y'] == ty:
        pass
    else:
        print(f"Failed UP step to ({tx}, {ty})")

print("Walking LEFT on row 5 to column 6...")
path_left = [
    ('Left', 17, 5),
    ('Left', 16, 5),
    ('Left', 15, 5),
    ('Left', 14, 5),
    ('Left', 13, 5),
    ('Left', 12, 5),
    ('Left', 11, 5),
    ('Left', 10, 5),
    ('Left', 9, 5),
    ('Left', 8, 5),
    ('Left', 7, 5),
    ('Left', 6, 5)
]

for btn, tx, ty in path_left:
    pos = mgba.get_coordinates()
    mgba.press_buttons([btn])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == tx and new_pos['y'] == ty:
        pass
    else:
        print(f"Failed LEFT step to ({tx}, {ty}). Current coord: {new_pos}")
        time.sleep(0.5)
        pos_check = mgba.get_coordinates()
        if pos_check == new_pos:
            # Blocked by NPC or some obstacle, let's try row 7 if blocked
            print("Blocked. Stopping path.")
            break

# Now try to enter the Mansion from (6, 5)
pos = mgba.get_coordinates()
if pos['x'] == 6 and pos['y'] == 5:
    print("At (6, 5). Entering the Mansion...")
    mgba.press_buttons(["Up"])
    time.sleep(0.3)
    mgba.press_buttons(["Up"])
    time.sleep(1.5) # Wait for warp
    print("Final position inside Mansion:", mgba.get_coordinates())
else:
    print("We did not reach (6, 5). Final position:", pos)

img = mgba.take_screenshot()
print("Screenshot:", img)
