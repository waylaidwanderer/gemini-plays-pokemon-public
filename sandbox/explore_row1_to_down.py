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

# Starting from (17, 8).
# Let's walk to Row 12, and then try walking DOWN Row 13 on Columns 19, 20, 21.
print("Starting Row 13 vertical test...")

for col in [19, 20, 21]:
    # Walk to (col, 12)
    print(f"Testing Column {col} Row 13...")
    if walk_to(col, 12):
        # Try to step DOWN
        pos_before = mgba.get_coordinates()
        pos = walk_step("Down")
        if pos['y'] == 13:
            print(f"SUCCESS: Column {col} Row 13 is OPEN! Position:", pos)
            # Try to step DOWN to Row 14, 15, 16, 17, 18
            reached_balcony = False
            for _ in range(5):
                pos_prev = pos
                pos = walk_step("Down")
                if pos['y'] == pos_prev['y']:
                    print(f"  Blocked walking down at: ({pos['x']}, {pos['y']})")
                    break
                print(f"  Reached Row {pos['y']}")
                if pos['y'] >= 18:
                    reached_balcony = True
                    break
            if reached_balcony:
                print("REACHED BALCONY!")
                break
            else:
                # Walk back up to Row 12
                walk_to(col, 12)
        else:
            print(f"BLOCKED: Column {col} Row 13 is CLOSED.")

print("Final position:", mgba.get_coordinates())
