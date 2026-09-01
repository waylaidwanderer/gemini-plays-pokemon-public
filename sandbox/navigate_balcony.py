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

# Starting at (21, 15).
# Walk to (12, 11).
path = [
    ("Up", 4),      # (21, 15) -> (21, 11)
    ("Left", 9)     # (21, 11) -> (12, 11)
]

print("Walking to (12, 11)...")
success = walk_path(path)
if success:
    print("Reached (12, 11) successfully!")
    print(mgba.get_coordinates())
    mgba.take_screenshot()
else:
    print("Navigation interrupted. Current coordinates:")
    print(mgba.get_coordinates())
    mgba.take_screenshot()
