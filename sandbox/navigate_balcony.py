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

# Starting at (21, 4).
# Goal: reach (19, 18) and drop to B1F West.

path = [
    ("Left", 3),    # (21, 4) -> (18, 4)
    ("Down", 2),    # (18, 4) -> (18, 6)
    ("Right", 3),   # (18, 6) -> (21, 6)
    ("Down", 12),   # (21, 6) -> (21, 18)
    ("Left", 2)     # (21, 18) -> (19, 18) (drop!)
]

print("Starting direct balcony drop navigation route...")
success = walk_path(path)
if success:
    print("Drop executed successfully! Checking current location:")
    time.sleep(1.0) # wait for map transition / screen load
    print(mgba.get_coordinates())
    mgba.take_screenshot()
else:
    print("Navigation interrupted or blocked. Current coordinates:")
    print(mgba.get_coordinates())
    mgba.take_screenshot()
