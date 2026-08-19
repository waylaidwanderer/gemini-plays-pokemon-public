import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

print("Exploring down column 10 and then east on 1F...")

# Currently at (10, 15) on 1F
# Walk down column 10 to (10, 26)
path_down = [
    ('Down', 10, 16),
    ('Down', 10, 17),
    ('Down', 10, 18),
    ('Down', 10, 19),
    ('Down', 10, 20),
    ('Down', 10, 21),
    ('Down', 10, 22),
    ('Down', 10, 23),
    ('Down', 10, 24),
    ('Down', 10, 25),
    ('Down', 10, 26)
]

for btn, tx, ty in path_down:
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

# Now try to walk Right along row 26 as far as possible
print("At row 26, attempting to walk Right (East)...")
current_x = mgba.get_coordinates()['x']
while current_x < 30:
    pos = mgba.get_coordinates()
    print(f"1F: At {pos}, attempting to move RIGHT...")
    mgba.press_buttons(["Right"])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] > pos['x']:
        print("Moved Right successfully.")
        current_x = new_pos['x']
    else:
        print("Blocked or in battle, checking...")
        time.sleep(0.5)
        pos_check = mgba.get_coordinates()
        if pos_check == new_pos:
            run_from_battle()
            time.sleep(1.0)
            new_pos_after = mgba.get_coordinates()
            current_x = new_pos_after['x']
            # If still stuck at same coordinate, break
            if new_pos_after == new_pos:
                print("Physically blocked on column", current_x)
                break
        else:
            current_x = new_pos['x']

print("Final position of exploration:", mgba.get_coordinates())
mgba.take_screenshot()
