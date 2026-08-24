import mgba
import sys
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

print("Starting at:", get_pos())

# 1. Walk from (2, 10) to (1, 11) via (1, 12)
if not walk_to_clean(1, 10): sys.exit(1)
if not walk_to_clean(1, 12): sys.exit(1)
if not walk_to_clean(1, 11): sys.exit(1)

# Currently at (1, 11) facing UP.
# 2. Face RIGHT and toggle switch using the EXACT working sequence from get_secret_key_complete.py!
print("Facing Right towards (2, 11) and interacting...")
mgba.press_buttons(["Right", "sleep 250", "A", "sleep 800", "A", "sleep 800", "A", "sleep 500", "B", "sleep 300"])
print("State B toggled! Position:", get_pos())

# 3. Walk UP Column 1 to Row 6 (since State B is active, Row 9 gate is open!)
if not walk_to_clean(1, 6): sys.exit(1)

# 4. Walk RIGHT along Row 6 to Column 26 (26, 6)
if not walk_to_clean(26, 6): sys.exit(1)

# 5. Drop through pitfall
print("Stepping onto pitfall...")
mgba.press_buttons(["Right", "sleep 2500"])
print("Position after drop (should be 1F East fenced room):", get_pos())
mgba.take_screenshot()
