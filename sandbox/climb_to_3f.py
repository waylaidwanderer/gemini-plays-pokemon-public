
import mgba
import sys

def get_pos():
    return mgba.get_coordinates()

def walk_step(direction):
    pos_before = get_pos()
    mgba.press_buttons([direction, "sleep 450"])
    pos_after = get_pos()
    return pos_before, pos_after

def walk_to(target_x, target_y):
    print(f"Walking to ({target_x}, {target_y})...")
    max_steps = 50
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
            print(f"Blocked at {pos_before} going {direction}. Stopping.")
            return False
        steps += 1
    return False

# Starting from current position (3, 11) on 2F West
print("Start position on 2F West:", get_pos())

# Walk to (7, 11)
if walk_to(7, 11):
    print("Stepping UP to warp to 3F West...")
    mgba.press_buttons(["Up", "sleep 2500"])
    print("Position after warp (should be 3F West):", get_pos())
    mgba.take_screenshot()
