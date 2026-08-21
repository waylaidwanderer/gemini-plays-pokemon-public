import mgba
import time

# We are at (8, 10) on 3F West.
# Let's walk Left along Row 10 to see how far we can go.
# We will walk Left until we hit a wall or reach Column 1.

path = ["Left"] * 10

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
