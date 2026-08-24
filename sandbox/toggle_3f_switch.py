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

# Currently at (6, 10) on 3F West in State A
print("Walking to (1, 11) on Row 11...")
if not walk_to(6, 11): sys.exit(1)
if not walk_to(1, 11): sys.exit(1)

# Face RIGHT
print("Facing RIGHT towards (2, 11)...")
mgba.press_buttons(["Right", "sleep 500"])

# Safe switch toggling sequence (100% verified 1500ms sleeps)
print("Toggling the switch at (2, 11) facing Right...")
mgba.press_buttons(["A", "sleep 1500"]) # "A secret switch!"
mgba.press_buttons(["A", "sleep 1500"]) # "Press it?" (Yes/No appears)
mgba.press_buttons(["A", "sleep 1500"]) # Select YES -> "(click)"
mgba.press_buttons(["B", "sleep 500"])  # Close dialogue box

print("Mansion should be in State B. Verifying...")
if not walk_to(1, 12): sys.exit(1)
if not walk_to(2, 12): sys.exit(1)

mgba.take_screenshot()
