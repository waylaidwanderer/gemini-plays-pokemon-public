import mgba
import sys

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("Wild battle detected! Fleeing...")
    mgba.press_buttons(["sleep 2000"])
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
    max_steps = 30
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
            mgba.press_buttons(["sleep 150"])
            pos_now = get_pos()
            if pos_now == pos_before:
                run_from_battle()
        steps += 1
    return False

# Start from current position (6, 10) on 3F West
print("Walking to switch at (2, 12)...")
if not walk_to(6, 13): sys.exit(1)
if not walk_to(2, 13): sys.exit(1)
if not walk_to(2, 12): sys.exit(1)

# Face UP
print("Facing UP...")
mgba.press_buttons(["Up", "sleep 500"])

# Dialogue step 1
print("Pressing A (1)...")
mgba.press_buttons(["A", "sleep 2000"])
mgba.take_screenshot()

# Dialogue step 2
print("Pressing A (2)...")
mgba.press_buttons(["A", "sleep 2000"])
mgba.take_screenshot()

# Dialogue step 3
print("Pressing A (3)...")
mgba.press_buttons(["A", "sleep 2000"])
mgba.take_screenshot()

# Dialogue step 4
print("Pressing A (4)...")
mgba.press_buttons(["A", "sleep 2000"])
mgba.take_screenshot()

# Dialogue step 5
print("Pressing B...")
mgba.press_buttons(["B", "sleep 1000"])
mgba.take_screenshot()
