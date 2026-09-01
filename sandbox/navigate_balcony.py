import mgba
import time

def step(direction):
    current = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.35)
    next_pos = mgba.get_coordinates()
    if next_pos == current:
        print(f"Blocked at {current} trying to move {direction}")
        return False
    return next_pos

def walk_path(path_steps):
    for direction, count in path_steps:
        print(f"Moving {direction} {count} times...")
        for _ in range(count):
            res = step(direction)
            if not res:
                return False
            print(f"Moved to {res}")
    return True

# Current position is (10, 6).
# Path to (3, 11):
path = [
    ("Down", 5),    # (10, 6) -> (10, 11)
    ("Left", 7)     # (10, 11) -> (3, 11)
]

print("Walking from (10, 6) to (3, 11)...")
success = walk_path(path)
if success:
    print("Reached (3, 11) successfully! Facing Left to prepare for switch toggle...")
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
    print("Current coordinates:", mgba.get_coordinates())
    mgba.take_screenshot()
else:
    print("Navigation interrupted. Current coordinates:")
    print(mgba.get_coordinates())
    mgba.take_screenshot()
