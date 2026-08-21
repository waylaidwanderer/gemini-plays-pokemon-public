import mgba
import time

# We are at (2, 11) on 2F.
# Let's test walking to find a path to the stairs at (5, 10) or to see if we are trapped.
# Let's first test if we can walk Up past row 9.
# We will try: Up, Up, Up, Up
path_up = ["Up", "Up", "Up", "Up"]
print("Testing walking Up:")
for step in path_up:
    before = mgba.get_coordinates()
    mgba.press_buttons([step])
    time.sleep(0.3)
    after = mgba.get_coordinates()
    print(f"Moved {step} from {before} to {after}")
    if before == after:
        break

# Let's see where we end up
curr = mgba.get_coordinates()
print("Current position:", curr)
mgba.take_screenshot()
