import mgba
import time

def step(direction):
    current = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.5)
    return mgba.get_coordinates()

# Walk from (18, 7) to (10, 16)
path_to_test = [
    {'x': 17, 'y': 7},
    {'x': 16, 'y': 7},
    {'x': 15, 'y': 7},
    {'x': 14, 'y': 7},
    {'x': 13, 'y': 7},
    {'x': 12, 'y': 7},
    {'x': 11, 'y': 7},
    {'x': 10, 'y': 7},
    # Down Column 10 to Row 16
    {'x': 10, 'y': 8},
    {'x': 10, 'y': 9},
    {'x': 10, 'y': 10},
    {'x': 10, 'y': 11},
    {'x': 10, 'y': 12},
    {'x': 10, 'y': 13},
    {'x': 10, 'y': 14},
    {'x': 10, 'y': 15},
    {'x': 10, 'y': 16}
]

print("Walking to (10, 16)...")
for target in path_to_test:
    curr = mgba.get_coordinates()
    if curr == target:
        continue
    dx = target['x'] - curr['x']
    dy = target['y'] - curr['y']
    if dx == 1: pdir = "Right"
    elif dx == -1: pdir = "Left"
    elif dy == 1: pdir = "Down"
    elif dy == -1: pdir = "Up"
    res = step(pdir)
    if res != target:
        print(f"Failed to reach {target}, at {res}")
        break

curr = mgba.get_coordinates()
if curr == {'x': 10, 'y': 16}:
    print("Reached (10, 16)! Testing step Right to (11, 16)...")
    res = step("Right")
    print("Step Right result:", res)
    if res == {'x': 11, 'y': 16}:
        print("Column 11 Row 16 is WALKABLE! Testing step Right to (12, 16)...")
        res2 = step("Right")
        print("Step Right 2 result:", res2)
else:
    print("Could not reach (10, 16) to perform test.")
mgba.take_screenshot()
