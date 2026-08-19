import mgba
import time

print("Walking to Pokémon Mansion from (14, 5)...")

path = [
    ('Up', 14, 4),
    ('Left', 13, 4),
    ('Left', 12, 4),
    ('Left', 11, 4),
    ('Left', 10, 4),
    ('Left', 9, 4),
    ('Left', 8, 4),
    ('Left', 7, 4),
    ('Left', 6, 4),
    ('Up', 6, 3)
]

for btn, tx, ty in path:
    pos = mgba.get_coordinates()
    print(f"Current: {pos}, Next: {btn} to ({tx}, {ty})")
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
        print(f"FAILED. Expected ({tx}, {ty}), got {new_pos}")
        break

print("Final position:", mgba.get_coordinates())
mgba.take_screenshot()
