import mgba
import time

print("Walking to Mansion from (10, 6) via Column 10...")

# Start at (10, 6)
path = [
    ('Up', 10, 5),
    ('Up', 10, 4),
    ('Left', 9, 4),
    ('Left', 8, 4),
    ('Left', 7, 4),
    ('Left', 6, 4),
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
