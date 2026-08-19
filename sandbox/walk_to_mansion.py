import mgba
import time

print("Bypassing Lab to reach Pokémon Mansion...")

# Start at (6, 10) on Cinnabar Island
path = [
    ('Down', 6, 11),
    ('Down', 6, 12),
    ('Right', 7, 12),
    ('Right', 8, 12),
    ('Right', 9, 12),
    ('Right', 10, 12),
    ('Right', 11, 12),
    ('Right', 12, 12),
    ('Right', 13, 12),
    ('Right', 14, 12),
    ('Right', 15, 12),
    ('Right', 16, 12),
    ('Right', 17, 12),
    ('Right', 18, 12),
    ('Up', 18, 11),
    ('Up', 18, 10),
    ('Up', 18, 9),
    ('Up', 18, 8),
    ('Up', 18, 7),
    ('Left', 17, 7),
    ('Left', 16, 7),
    ('Left', 15, 7),
    ('Left', 14, 7),
    ('Left', 13, 7),
    ('Left', 12, 7),
    ('Left', 11, 7),
    ('Left', 10, 7),
    ('Left', 9, 7),
    ('Left', 8, 7),
    ('Left', 7, 7),
    ('Left', 6, 7),
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
            time.sleep(1.0) # Wait for warp
            print("Warped into Mansion successfully! Position:", mgba.get_coordinates())
            break
            
        print(f"Failed to step to ({tx}, {ty}). Current coordinate: {new_pos}")
        time.sleep(0.5)
        pos_check = mgba.get_coordinates()
        if pos_check == new_pos:
            print("Blocked. Stopping.")
            break
        else:
            print("Position changed, continuing...")

print("Final position:", mgba.get_coordinates())
mgba.take_screenshot()
