import mgba
import sys
import time

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("Wild battle detected! Waiting for battle menu to load...")
    time.sleep(2.0)
    for _ in range(3):
        mgba.press_buttons(["B", "sleep 150"])
    print("Sending escape inputs...")
    mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 1000"])
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 150"])
    print("Escape sequence complete.")

def walk_step(direction):
    pos_before = get_pos()
    mgba.press_buttons([direction, "sleep 450"])
    pos_after = get_pos()
    if pos_before == pos_after:
        print("Blocked/Battle! Attempting run from battle...")
        run_from_battle()
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
            print(f"Failed step at {pos_before} going {direction}")
            return False
        steps += 1
    return False

print("--- CORRECT 3F EAST CROSSING SCRIPT ---")
print("Starting from:", get_pos())

# Phase 1: Walk to 3F East pitfall and drop
print("PHASE 1: Walking to pitfall at (26, 4)...")
if not walk_to(7, 10): sys.exit(1)
if not walk_to(7, 7): sys.exit(1)
if not walk_to(12, 7): sys.exit(1)
if not walk_to(12, 6): sys.exit(1)
if not walk_to(19, 6): sys.exit(1)
if not walk_to(19, 3): sys.exit(1)
if not walk_to(26, 3): sys.exit(1)

print("Stepping DOWN onto pitfall...")
mgba.press_buttons(["Down", "sleep 2500"])
print("Landing position on 1F East:", get_pos())

# Phase 2: Walk to B1F stairs on 1F East inside fenced room
print("PHASE 2: Walking to B1F stairs on 1F East...")
if not walk_to(26, 3): sys.exit(1)
if not walk_to(22, 3): sys.exit(1)
print("Warping DOWN to B1F East...")
mgba.press_buttons(["Up", "sleep 2500"])
print("Landing position on B1F East:", get_pos())
