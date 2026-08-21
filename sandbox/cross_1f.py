import mgba
import time

# We are at (5, 9) on 2F West.
# Let's walk UP to Row 5, then Right to (10, 5) to test the staircase there!
path = ["Up", "Up", "Up", "Up", "Right", "Right", "Right", "Right", "Right"]

print("Walking to (10, 5) staircase...")
for idx, direction in enumerate(path):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.3)
    pos_after = mgba.get_coordinates()
    print(f"Step {idx} ({direction}): {pos_before} -> {pos_after}")
    if pos_before == pos_after:
        print(f"Blocked trying to move {direction} from {pos_before}")
        break

print("Final position:", mgba.get_coordinates())
mgba.take_screenshot()
