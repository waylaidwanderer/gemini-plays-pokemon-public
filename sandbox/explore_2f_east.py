import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

print("Navigating to eastern 2F...")

# Start at (7, 11)
path = [
    ('Left', 6, 11),
    ('Up', 6, 10),
    ('Up', 6, 9),
    ('Up', 6, 8),
    ('Up', 6, 7),
    ('Right', 7, 7),
    ('Right', 8, 7),
    ('Right', 9, 7),
    ('Right', 10, 7),
    ('Right', 11, 7),
    ('Right', 12, 7),
    ('Right', 13, 7),
    ('Right', 14, 7),
    ('Right', 15, 7),
    ('Right', 16, 7),
    ('Right', 17, 7)
]

for btn, tx, ty in path:
    pos = mgba.get_coordinates()
    print(f"Current Pos: {pos}, Next Step: {btn} to ({tx}, {ty})")
    mgba.press_buttons([btn])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == tx and new_pos['y'] == ty:
        print("Moved successfully.")
    else:
        print(f"Failed. Expected ({tx}, {ty}), got {new_pos}")
        time.sleep(0.5)
        pos_check = mgba.get_coordinates()
        if pos_check == new_pos:
            run_from_battle()
            time.sleep(1.0)
            break
        else:
            print("Position changed, stopping.")
            break

print("Final position:", mgba.get_coordinates())
mgba.take_screenshot()
