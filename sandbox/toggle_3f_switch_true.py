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

print("Starting at:", get_pos())

# 1. Walk to (2, 12) via (2, 13)
if not walk_to_clean(6, 13): sys.exit(1)
if not walk_to_clean(2, 13): sys.exit(1)
if not walk_to_clean(2, 12): sys.exit(1)

# Currently at (2, 12) facing UP. Let's try to interact with (2, 11) by pressing A
print("Trying to interact with (2, 11) from (2, 12) facing UP...")
mgba.press_buttons(["A", "sleep 1200"])
sc = mgba.take_screenshot()
# Let's check if the screen changed or if there's dialogue (we can close it with B just in case)
mgba.press_buttons(["B", "sleep 400"])

# Let's try to walk to (1, 11)
print("Walking to (1, 11)...")
if not walk_to_clean(1, 12): sys.exit(1)
if not walk_to_clean(1, 11): sys.exit(1)

# Now we are at (1, 11) facing UP. Let's press Right and A to toggle!
# Wait, to face RIGHT without walking to (2, 11), let's use a short press or face right
print("Facing RIGHT and toggling...")
mgba.press_buttons(["Right", "sleep 150"])
mgba.press_buttons(["A", "sleep 1200"]) # A secret switch!
mgba.press_buttons(["A", "sleep 1200"]) # Press it?
mgba.press_buttons(["A", "sleep 1200"]) # YES
mgba.press_buttons(["A", "sleep 1200"]) # Who wouldn't?
mgba.press_buttons(["B", "sleep 500"])  # Close

# Check if we moved to (2, 11)
print("Position after toggle:", get_pos())
mgba.take_screenshot()
