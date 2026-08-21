import mgba
import time

# We are at (14, 12).
# Let's walk Right to Column 18, then UP to Row 5, then Left to Column 6, then UP to Mansion door.
path = ["Right"]*4 + ["Up"]*7 + ["Left"]*12 + ["Up"]*2

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
