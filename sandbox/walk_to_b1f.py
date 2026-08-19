import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

print("Starting 1F to B1F stairs routing script...")
pos = mgba.get_coordinates()
print("Initial position:", pos)

# Target path from (22, 6) to B1F stairs (21, 24)
# First we go Left to column 19 on row 6
# Then Down column 19 to row 24
# Then Right to column 21 on row 24
# Then Down into the stairs at (21, 24)
path = [
    ('Left', 21, 6),
    ('Left', 20, 6),
    ('Left', 19, 6),
    ('Down', 19, 7),
    ('Down', 19, 8),
    ('Down', 19, 9),
    ('Down', 19, 10),
    ('Down', 19, 11),
    ('Down', 19, 12),
    ('Down', 19, 13),
    ('Down', 19, 14),
    ('Down', 19, 15),
    ('Down', 19, 16),
    ('Down', 19, 17),
    ('Down', 19, 18),
    ('Down', 19, 19),
    ('Down', 19, 20),
    ('Down', 19, 21),
    ('Down', 19, 22),
    ('Down', 19, 23),
    ('Down', 19, 24),
    ('Right', 20, 24),
    ('Right', 21, 24),
    ('Down', 21, 25) # Enter the B1F stairs!
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
                print("Failed again. Let's inspect surroundings or wait.")
                time.sleep(0.5)
                break

print("Final Position:", mgba.get_coordinates())
mgba.take_screenshot()
