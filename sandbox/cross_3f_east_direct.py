import mgba
import sys

def get_pos():
    return mgba.get_coordinates()

def walk_step(direction):
    pos_before = get_pos()
    mgba.press_buttons([direction, "sleep 450"])
    pos_after = get_pos()
    return pos_before, pos_after

def walk_to_clean(target_x, target_y):
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
            # Try a second time (handles turning in place)
            pos_before, pos_after = walk_step(direction)
            if pos_before == pos_after:
                print(f"BLOCKED at {pos_before} when trying to go {direction}!")
                return False
        steps += 1
    return False

print("Starting on 3F West at:", get_pos())

# Phase 1: Walk LEFT from (5, 11) to (1, 11)
if not walk_to_clean(1, 11):
    print("Failed to walk to (1, 11)")
    sys.exit(1)

# Phase 2: Walk UP Column 1 to Row 6
if not walk_to_clean(1, 6):
    print("Failed to walk to (1, 6)")
    sys.exit(1)

# Phase 3: Walk RIGHT along Row 6 to Column 26
if not walk_to_clean(26, 6):
    print("Failed to walk to (26, 6)")
    sys.exit(1)

# Phase 4: Step RIGHT onto the pitfall to drop to 1F East inside fenced room
print("Stepping onto pitfall...")
mgba.press_buttons(["Right", "sleep 2500"])
print("Position after drop (should be 1F East fenced room):", get_pos())
mgba.take_screenshot()
