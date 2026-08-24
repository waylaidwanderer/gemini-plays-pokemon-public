
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
            print(f"Blocked at {pos_before} going {direction} (possibly in battle or wall). Stopping.")
            return False
        steps += 1
    return False

# Starting from current position (3, 11) on 3F West
print("Start position:", get_pos())
if walk_to(2, 11):
    if walk_to(2, 9):
        if walk_to(12, 9):
            print("Successfully reached 3F East Row 9 Column 12!")
print("Final Position:", get_pos())
mgba.take_screenshot()
