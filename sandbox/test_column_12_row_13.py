import mgba
import time

def step(direction):
    current = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.5)
    return mgba.get_coordinates()

# Walk from (10, 16) to (12, 12)
path_to_test = [
    {'x': 10, 'y': 15},
    {'x': 10, 'y': 14},
    {'x': 10, 'y': 13},
    {'x': 10, 'y': 12},
    {'x': 11, 'y': 12},
    {'x': 12, 'y': 12}
]

print("Walking to (12, 12)...")
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
    else:
        print(f"Skipping disjoint target: {target}")
        continue
    res = step(pdir)
    if res != target:
        print(f"Failed to reach {target}, at {res}")
        break

curr = mgba.get_coordinates()
if curr == {'x': 12, 'y': 12}:
    print("Reached (12, 12)! Testing step Down to (12, 13)...")
    res = step("Down")
    print("Step Down result:", res)
else:
    print("Could not reach (12, 12) to perform test.")
mgba.take_screenshot()
