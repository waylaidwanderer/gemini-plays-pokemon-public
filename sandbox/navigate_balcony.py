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

# Starting at (21, 11).
# Walk final chunk: 7 steps Down to (21, 18), 2 steps Left to (19, 18) (drop!)
path = [
    ("Down", 7),
    ("Left", 2)
]

print("Starting final Chunk 5 balcony drop path...")
success = walk_path(path)
if success:
    print("Drop executed successfully! Checking current location:")
    time.sleep(1.0) # wait for map transition / screen load
    print(mgba.get_coordinates())
    mgba.take_screenshot()
else:
    print("Chunk 5 interrupted. Current coordinates:")
    print(mgba.get_coordinates())
    mgba.take_screenshot()
