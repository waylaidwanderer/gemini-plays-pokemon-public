import mgba
import time

print("Starting bypass walk to Mansion entrance...")

# We are at (14, 5).
# Path goes around the NPC at (12, 5) via row 4
path = [
    ('Left', 13, 5),
    ('Up', 13, 4),
    ('Left', 12, 4),
    ('Left', 11, 4),
    ('Down', 11, 5),
    ('Left', 10, 5),
    ('Left', 9, 5),
    ('Left', 8, 5),
    ('Left', 7, 5),
    ('Left', 6, 5),
    ('Up', 6, 4),
    ('Up', 6, 3)
]

for btn, tx, ty in path:
    pos = mgba.get_coordinates()
    print(f"Overworld: At {pos}, Next Step: {btn} to ({tx}, {ty})")
    mgba.press_buttons([btn])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == tx and new_pos['y'] == ty:
        print("Step succeeded.")
    else:
        # Check if we warped into the Mansion
        if tx == 6 and ty == 3 and new_pos['y'] == 27:
            time.sleep(1.5) # Wait for warp
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
img = mgba.take_screenshot()
print("Screenshot:", img)
