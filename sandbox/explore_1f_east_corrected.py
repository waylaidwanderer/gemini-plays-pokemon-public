import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

print("Starting corrected navigation from (1, 3) on 2F...")
path_to_stairs = [
    ('Right', 2, 3),
    ('Down', 2, 4),
    ('Down', 2, 5),
    ('Down', 2, 6),
    ('Down', 2, 7),
    ('Right', 3, 7)
]

for btn, tx, ty in path_to_stairs:
    pos = mgba.get_coordinates()
    print(f"2F: At {pos}, Next Step: {btn} to ({tx}, {ty})")
    mgba.press_buttons([btn])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == tx and new_pos['y'] == ty:
        print("Step succeeded.")
    else:
        print(f"Failed step to ({tx}, {ty}). Checking for battle...")
        time.sleep(0.5)
        pos_check = mgba.get_coordinates()
        if pos_check == new_pos:
            run_from_battle()
            time.sleep(1.0)
            # Try step again
            mgba.press_buttons([btn])
            time.sleep(0.3)
            new_pos_retry = mgba.get_coordinates()
            if new_pos_retry['x'] == tx and new_pos_retry['y'] == ty:
                print("Retry succeeded.")
            else:
                print("Retry failed. Stopping.")
                break

# Warp to 1F
pos = mgba.get_coordinates()
if pos['x'] == 3 and pos['y'] == 7:
    print("At stairs (3, 7) on 2F. Warping DOWN to 1F...")
    mgba.press_buttons(["Down"])
    time.sleep(1.5)
    print("Landed on 1F! Current position:", mgba.get_coordinates())
else:
    print("Failed to reach stairs (3, 7) on 2F!")

# Now explore EAST on 1F
pos = mgba.get_coordinates()
if pos['x'] == 16 and pos['y'] == 5:
    east_path = [
        ('Right', 17, 5),
        ('Right', 18, 5),
        ('Right', 19, 5),
        ('Right', 20, 5),
        ('Right', 21, 5)
    ]
    print("Exploring EAST on 1F from (16, 5)...")
    for btn, tx, ty in east_path:
        curr = mgba.get_coordinates()
        print(f"1F: At {curr}, Next Step: {btn} to ({tx}, {ty})")
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
else:
    print("We are not at (16, 5) on 1F!")

print("Final position:", mgba.get_coordinates())
