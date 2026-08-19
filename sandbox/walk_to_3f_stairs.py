import mgba
import time

print("Testing 2F stairs to 3F at (7, 10)...")

# Current position is (5, 11) on 2F.
path = [
    ('Right', 6, 11),
    ('Right', 7, 11),
    ('Up', 7, 10)
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
        # Check if we warped to 3F
        print("Position after step:", new_pos)
        break

print("Final position:", mgba.get_coordinates())
mgba.take_screenshot()
