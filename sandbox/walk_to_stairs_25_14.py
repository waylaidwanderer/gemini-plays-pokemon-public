import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

print("Walking from (21, 15) to stairs at (25, 14)...")
pos = mgba.get_coordinates()
print("Current position:", pos)

# Path to stairs:
# UP to (21, 3)
# RIGHT to (25, 3)
# DOWN to (25, 14) (or onto stairs)
path = [
    ('Up', 21, 14),
    ('Up', 21, 13),
    ('Up', 21, 12),
    ('Up', 21, 11),
    ('Up', 21, 10),
    ('Up', 21, 9),
    ('Up', 21, 8),
    ('Up', 21, 7),
    ('Up', 21, 6),
    ('Up', 21, 5),
    ('Up', 21, 4),
    ('Up', 21, 3),
    ('Right', 22, 3),
    ('Right', 23, 3),
    ('Right', 24, 3),
    ('Right', 25, 3),
    ('Down', 25, 4),
    ('Down', 25, 5),
    ('Down', 25, 6),
    ('Down', 25, 7),
    ('Down', 25, 8),
    ('Down', 25, 9),
    ('Down', 25, 10),
    ('Down', 25, 11),
    ('Down', 25, 12),
    ('Down', 25, 13),
    ('Down', 25, 14)
]

for btn, tx, ty in path:
    while True:
        pos = mgba.get_coordinates()
        print(f"At {pos}, moving {btn} to ({tx}, {ty})...")
        mgba.press_buttons([btn])
        time.sleep(0.4)
        new_pos = mgba.get_coordinates()
        if new_pos['x'] == tx and new_pos['y'] == ty:
            print("Moved successfully.")
            break
        else:
            if new_pos != pos:
                print("Map transition or warp detected! Position:", new_pos)
                break
            print("Blocked or battle! Trying to escape...")
            run_from_battle()
            time.sleep(0.5)
            mgba.press_buttons([btn])
            time.sleep(0.4)
            new_pos2 = mgba.get_coordinates()
            if new_pos2['x'] == tx and new_pos2['y'] == ty:
                print("Moved successfully after battle.")
                break
            elif new_pos2 != pos:
                print("Map transition/warp detected after battle! Position:", new_pos2)
                break
            else:
                print("Failed again.")
                break

print("Final Position:", mgba.get_coordinates())
mgba.take_screenshot()
