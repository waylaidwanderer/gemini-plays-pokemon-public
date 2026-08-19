import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

print("Walking to Pokémon Mansion from (11, 12)...")

path = [
    ('Left', 10, 12),
    ('Left', 9, 12),
    ('Left', 8, 12),
    ('Left', 7, 12),
    ('Left', 6, 12),
    ('Up', 6, 11),
    ('Up', 6, 10),
    ('Up', 6, 9),
    ('Up', 6, 8),
    ('Up', 6, 7),
    ('Up', 6, 6),
    ('Up', 6, 5),
    ('Up', 6, 4),
    ('Up', 6, 3)
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
        # Check if we warped into the Mansion
        if tx == 6 and ty == 3 and new_pos['y'] == 27:
            print("Warped into Mansion successfully!")
            break
        print(f"Failed to reach ({tx}, {ty}). Current coordinate: {new_pos}")
        time.sleep(0.5)
        pos_check = mgba.get_coordinates()
        if pos_check == new_pos:
            print("Blocked. Stopping.")
            break
        else:
            print("Position changed, continuing...")

print("Final position:", mgba.get_coordinates())
mgba.take_screenshot()
