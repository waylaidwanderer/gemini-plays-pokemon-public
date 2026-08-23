import mgba
import time

def run_from_battle():
    print("In battle! Running...")
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 100"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 500"])
    for _ in range(4):
        mgba.press_buttons(["B", "sleep 100"])

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction, "sleep 150"])
    pos_after = mgba.get_coordinates()
    if pos_before == pos_after:
        mgba.press_buttons([direction, "sleep 150"])
        pos_after = mgba.get_coordinates()
        attempts = 0
        while pos_before == pos_after and attempts < 5:
            run_from_battle()
            mgba.press_buttons([direction, "sleep 150"])
            pos_after = mgba.get_coordinates()
            attempts += 1
    return pos_after

def walk_to(target_x, target_y):
    max_steps = 30
    steps = 0
    while steps < max_steps:
        pos = mgba.get_coordinates()
        x, y = pos['x'], pos['y']
        if x == target_x and y == target_y:
            return True
        if x < target_x:
            walk_step("Right")
        elif x > target_x:
            walk_step("Left")
        elif y < target_y:
            walk_step("Down")
        elif y > target_y:
            walk_step("Up")
        steps += 1
    return False

# Start grid search of the room (x: 14 to 21, y: 8 to 12)
# We are currently at (15, 11).
print("Starting search of the room for any stairs...")

# Walk to each tile in a grid
for y in range(8, 13):
    for x in range(14, 22):
        print(f"Trying to walk to: ({x}, {y})")
        # Try to walk to (x, y)
        success = walk_to(x, y)
        pos = mgba.get_coordinates()
        print(f"  Reached: ({pos['x']}, {pos['y']})")
        # If we warped, our coordinates will change or we will see a map transition.
        # But wait! On 2F, the coordinates of the landing are (15, 11) or similar.
        # How do we know we warped? If our y coordinate or our map changes.
        # Let's check if the coordinates are in B1F or 2F.
        # Usually, a warp transition resets the step/mansion state or coordinate systems, or coordinates become 2F coordinates.
        # Since 2F and 3F coordinates are very similar, let's take a screenshot or print coordinates.
        if pos['y'] == 11 and pos['x'] == 15:
            # Wait, did we warp to 2F (15, 11)?
            # Let's take a screenshot to check if the surrounding is different!
            # On 2F, there are different tiles. Let's just check if we can walk to other rows.
            pass

print("Search completed. Final position:", mgba.get_coordinates())
