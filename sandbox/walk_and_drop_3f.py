import mgba
import sys
import time

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("Wild battle detected! Fleeing...")
    time.sleep(2.0)
    for _ in range(3):
        mgba.press_buttons(["B", "sleep 150"])
    mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 2500"])
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 150"])

def walk_step(direction):
    pos_before = get_pos()
    mgba.press_buttons([direction, "sleep 450"])
    pos_after = get_pos()
    return pos_before, pos_after

def walk_to(target_x, target_y):
    print(f"Walking to ({target_x}, {target_y})...")
    max_steps = 40
    steps = 0
    while steps < max_steps:
        pos = get_pos()
        x, y = pos['x'], pos['y']
        if x == target_x and y == target_y:
            print(f"Arrived at ({target_x}, {target_y})!")
            return True
        if x < target_x: direction = "Right"
        elif x > target_x: direction = "Left"
        elif y < target_y: direction = "Down"
        elif y > target_y: direction = "Up"
        pos_before, pos_after = walk_step(direction)
        if pos_before == pos_after:
            time.sleep(0.1)
            pos_now = get_pos()
            if pos_now == pos_before:
                run_from_battle()
        steps += 1
    return False

# Starting at (2, 12)
print("Start position on 3F West:", get_pos())

# 1. Walk to (1, 12)
if not walk_to(1, 12): sys.exit(1)

# 2. Walk UP to (1, 6)
if not walk_to(1, 6): sys.exit(1)

# 3. Walk RIGHT to (26, 6) (triggers drop)
print("Walking to (26, 6) to drop...")
# We use custom walk loop to handle drop triggering on the last step
for x_target in range(2, 27):
    if not walk_to(x_target, 6):
        # If we got dropped or warped, check position
        pos = get_pos()
        if pos['y'] != 6:
            print("Warped or dropped early! Position:", pos)
            break

print("Final position:", get_pos())
mgba.take_screenshot()
