import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

print("Walking to 2F and finding 3F stairs...")

# Step 1: Currently at (10, 25) on 1F
# Walk UP column 10 to (10, 10)
path_up_1f = [
    ('Up', 10, 24),
    ('Up', 10, 23),
    ('Up', 10, 22),
    ('Up', 10, 21),
    ('Up', 10, 20),
    ('Up', 10, 19),
    ('Up', 10, 18),
    ('Up', 10, 17),
    ('Up', 10, 16),
    ('Up', 10, 15),
    ('Up', 10, 14),
    ('Up', 10, 13),
    ('Up', 10, 12),
    ('Up', 10, 11),
    ('Up', 10, 10)
]

for btn, tx, ty in path_up_1f:
    pos = mgba.get_coordinates()
    print(f"1F: At {pos}, moving {btn} to ({tx}, {ty})...")
    mgba.press_buttons([btn])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == tx and new_pos['y'] == ty:
        print("Moved successfully.")
    else:
        print("Blocked or in battle, checking...")
        run_from_battle()
        time.sleep(0.5)
        # Try again
        mgba.press_buttons([btn])
        time.sleep(0.3)
        new_pos2 = mgba.get_coordinates()
        if new_pos2['x'] == tx and new_pos2['y'] == ty:
            print("Moved successfully after battle.")
        else:
            print("Failed again. Position:", new_pos2)
            break

# Step 2: From (10, 10) on 1F, walk LEFT to (5, 10) and warp to 2F
path_left_1f = [
    ('Left', 9, 10),
    ('Left', 8, 10),
    ('Left', 7, 10),
    ('Left', 6, 10),
    ('Left', 5, 10) # Warp to 2F (lands at (5, 11))
]

print("Walking LEFT to warp to 2F...")
for btn, tx, ty in path_left_1f:
    pos = mgba.get_coordinates()
    print(f"1F: At {pos}, moving {btn} to ({tx}, {ty})...")
    mgba.press_buttons([btn])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == tx and new_pos['y'] == ty:
        print("Moved successfully.")
    else:
        # Check if we warped to 2F
        if tx == 5 and ty == 10 and new_pos['y'] == 11 and new_pos['x'] == 5:
            print("Warped to 2F successfully!")
            break
        print("Blocked or in battle, checking...")
        run_from_battle()
        time.sleep(0.5)
        # Try again
        mgba.press_buttons([btn])
        time.sleep(0.3)
        new_pos2 = mgba.get_coordinates()
        if new_pos2['x'] == tx and new_pos2['y'] == ty:
            print("Moved successfully after battle.")
        else:
            print("Failed again. Position:", new_pos2)
            break

time.sleep(1.0)
pos = mgba.get_coordinates()
print("Arrived on 2F at:", pos)

# Step 3: From (5, 11) on 2F, walk:
# - Right to (6, 11)
# - Up column 6 as far as possible (to row 5 or 6)
# - Left to column 5
path_bypass_2f = [
    ('Right', 6, 11),
    ('Up', 6, 10),
    ('Up', 6, 9),
    ('Up', 6, 8),
    ('Up', 6, 7),
    ('Up', 6, 6),
    ('Left', 5, 6),
    ('Up', 5, 5)
]

print("Executing bypass up column 6 on 2F...")
for btn, tx, ty in path_bypass_2f:
    pos = mgba.get_coordinates()
    print(f"2F: At {pos}, moving {btn} to ({tx}, {ty})...")
    mgba.press_buttons([btn])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == tx and new_pos['y'] == ty:
        print("Moved successfully.")
    else:
        # Check if we warped to 3F
        if new_pos['y'] < 5 or new_pos['x'] != tx:
            print("Unexpected position change (possible warp!):", new_pos)
            break
        print("Blocked or in battle, checking...")
        run_from_battle()
        time.sleep(0.5)
        # Try again
        mgba.press_buttons([btn])
        time.sleep(0.3)
        new_pos2 = mgba.get_coordinates()
        if new_pos2['x'] == tx and new_pos2['y'] == ty:
            print("Moved successfully after battle.")
        else:
            print("Failed again. Position:", new_pos2)
            break

print("Final Position:", mgba.get_coordinates())
mgba.take_screenshot()
