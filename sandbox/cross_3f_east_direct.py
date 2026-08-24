import mgba
import time

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("In battle! Running...")
    for _ in range(8):
        mgba.press_buttons(["B", "sleep 150"])
    mgba.press_buttons(["Right", "sleep 150", "Down", "sleep 150", "A", "sleep 800"])
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 150"])

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction, "sleep 150"])
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        mgba.press_buttons([direction, "sleep 150"])
        pos_after = mgba.get_coordinates()
        
        attempts = 0
        while pos_before == pos_after and attempts < 4:
            run_from_battle()
            mgba.press_buttons([direction, "sleep 150"])
            pos_after = mgba.get_coordinates()
            attempts += 1
    return pos_after

def walk_to(target_x, target_y):
    print(f"Walking to: ({target_x}, {target_y})")
    max_steps = 40
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

# Starting at (2, 11) on 3F West
print("Starting position:", get_pos())

# 1. Walk UP Column 2 to Row 6
# (2, 11) -> (2, 10) -> (2, 9) -> (2, 8) -> (2, 7) -> (2, 6)
print("Walking UP Column 2 to Row 6...")
walk_to(2, 6)
print("Position after walking UP:", get_pos())

# If we reached Row 6, then we are in State B (or Row 9 gate is open)
pos_now = get_pos()
if pos_now['y'] == 6:
    print("Row 9 gate is OPEN! Crossing to 3F East...")
    walk_to(12, 6)
    print("Arrived on 3F East (12, 6):", get_pos())
    # Walk to pitfall at (26, 6)
    walk_to(26, 6)
    print("Should have dropped! Waiting 2 seconds...")
    time.sleep(2.0)
    print("Position after drop:", get_pos())
else:
    print("Row 9 gate is CLOSED (still in State A)!")

sc = mgba.take_screenshot()
print("Final Screenshot:", sc)
