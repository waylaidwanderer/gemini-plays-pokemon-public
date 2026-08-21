import mgba
import time

# We are at (9, 11) on 3F West.
# Let's test walking Up to Row 8, and then Right to cross Column 10/11.
# We will print the coordinates after each move to trace the exact open path!

path = ["Up", "Up", "Up", "Right", "Right", "Right"]

print("Testing crossing 3F to the East...")
for idx, direction in enumerate(path):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.3)
    pos_after = mgba.get_coordinates()
    print(f"Step {idx} ({direction}): {pos_before} -> {pos_after}")
    if pos_before == pos_after:
        print(f"Blocked at {pos_before} trying to move {direction}")
        break

print("Final position:", mgba.get_coordinates())
mgba.take_screenshot()
