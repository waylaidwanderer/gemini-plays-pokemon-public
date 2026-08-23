import mgba
import time

def run_from_battle():
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

# We start at (15, 1). Let's systematically test columns from 11 to 21
# to see if we can walk DOWN to Row 8.
print("Starting column test from Row 1...")
for c in range(14, 22):
    # Walk to (c, 1)
    if walk_to(c, 1):
        # Now try to walk down. We will try walking down to Row 8
        print(f"Testing Column {c}...")
        steps_down = 0
        for _ in range(7):
            pos_before = mgba.get_coordinates()
            walk_step("Down")
            pos_after = mgba.get_coordinates()
            if pos_before['y'] == pos_after['y']:
                # Blocked
                break
            steps_down += 1
            
        pos = mgba.get_coordinates()
        if pos['y'] >= 8:
            print(f"SUCCESS: Column {c} is OPEN down to Row {pos['y']}!")
            # Walk back up to Row 1
            walk_to(c, 1)
        else:
            print(f"BLOCKED: Column {c} only went down to Row {pos['y']}.")
            # Walk back up to Row 1
            walk_to(c, 1)

print("Final position:", mgba.get_coordinates())
