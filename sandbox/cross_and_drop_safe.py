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
            mgba.press_buttons(["sleep 150"])
            pos_now = get_pos()
            if pos_now == pos_before:
                run_from_battle()
        steps += 1
    return False

# Currently in battle screen with "Got away safely!" at (5, 11)
print("PHASE 1: Clearing battle screen...")
mgba.press_buttons(["B", "sleep 2000"]) # Clear battle text, wait for overworld

# Walk to (1, 11) using Column 4 -> Row 13 -> Column 1 to avoid the statue at (2, 11) and gate at (3, 12)
print("PHASE 2: Walking to (1, 11)...")
if not walk_to(4, 11): sys.exit(1)
if not walk_to(4, 13): sys.exit(1)
if not walk_to(1, 13): sys.exit(1)
if not walk_to(1, 11): sys.exit(1)

# Walk to (26, 6) in State B via Column 1 -> Row 9
print("PHASE 3: Walking to 3F East pitfall at (26, 6)...")
if not walk_to(1, 9): sys.exit(1)
if not walk_to(12, 9): sys.exit(1)
if not walk_to(12, 6): sys.exit(1)
if not walk_to(26, 6): sys.exit(1)

print("Stepping RIGHT onto the pitfall to drop...")
mgba.press_buttons(["Right", "sleep 2500"])
print("Position after drop (should be 1F East fenced room):", get_pos())
mgba.take_screenshot()
