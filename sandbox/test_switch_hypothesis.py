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

# Clear battle text
print("Clearing battle text...")
mgba.press_buttons(["B", "sleep 150"])

# We are at (12, 9). Let's test Row 10, 11, 12, 13, 14, 15 Column 13 crossings!
print("Testing crossings from Row 10 to 15...")
for r in range(10, 16):
    print(f"Testing Row {r} crossing...")
    if walk_to(12, r):
        # Try to step RIGHT to Column 13
        pos_before = mgba.get_coordinates()
        pos_after = walk_step("Right")
        if pos_after['x'] == 13:
            print(f"SUCCESS: Row {r} Column 13 is OPEN!")
            # Walk back LEFT
            walk_step("Left")
        else:
            print(f"BLOCKED: Row {r} Column 13 is CLOSED.")
            
print("Test completed. Final position:", mgba.get_coordinates())
