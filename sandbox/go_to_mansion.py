import mgba
import time

# Walk from (6, 10) on Cinnabar Island to Mansion entrance at (6, 3) via the west shoreline on Column 3
path = ["Left"]*3 + ["Up"]*7 + ["Right"]*3 + ["Up"]*2

for idx, direction in enumerate(path):
    pos_before = mgba.get_coordinates()
    print(f"Step {idx}: trying to move {direction} from {pos_before}")
    mgba.press_buttons([direction])
    time.sleep(0.3)
    pos_after = mgba.get_coordinates()
    if pos_before == pos_after:
        print(f"Blocked at {pos_before} trying to move {direction}")
        break
    else:
        print(f"Moved to {pos_after}")

print("Final position:", mgba.get_coordinates())
mgba.take_screenshot()
