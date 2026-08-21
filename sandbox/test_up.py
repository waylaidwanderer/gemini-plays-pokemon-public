import mgba
import time

# We are at (9, 11) on 3F West.
# Let's test walking Up to see if we can get past row 11/10/9/8/7.
path = ["Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up"]

print("Testing walking Up on Column 9...")
for idx, direction in enumerate(path):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.3)
    pos_after = mgba.get_coordinates()
    print(f"Step {idx} ({direction}): {pos_before} -> {pos_after}")
    if pos_before == pos_after:
        print(f"Blocked at {pos_before}")
        break

print("Final position:", mgba.get_coordinates())
mgba.take_screenshot()
