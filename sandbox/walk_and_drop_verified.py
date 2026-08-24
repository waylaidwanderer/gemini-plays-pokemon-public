import mgba
import sys
import os
import time

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

# Starting at (2, 10) in State B
print("Starting walk and drop from:", get_pos())

# 1. Walk DOWN to (2, 11)
if not walk_to_clean(2, 11): sys.exit(1)

# 2. Walk RIGHT along Row 11 to Column 6 (6, 11)
if not walk_to_clean(6, 11): sys.exit(1)

# 3. Walk UP Column 6 to (6, 6) (Row 9 gate is open!)
if not walk_to_clean(6, 6): sys.exit(1)

# 4. Walk RIGHT along Row 6 to Column 26 (26, 6)
if not walk_to_clean(26, 6): sys.exit(1)

# 5. Drop through pitfall
print("Stepping onto pitfall...")
mgba.press_buttons(["Right", "sleep 2500"])
print("Position after drop (should be 1F East inside fenced room):", get_pos())
mgba.take_screenshot()
