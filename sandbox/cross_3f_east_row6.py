import mgba
import sys

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("In battle! Attempting to run...")
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 150"])
    mgba.press_buttons(["Right", "sleep 150", "Down", "sleep 150", "A", "sleep 600"])
    for _ in range(4):
        mgba.press_buttons(["B", "sleep 150"])

def walk_step(direction):
    pos_before = get_pos()
    mgba.press_buttons([direction, "sleep 450"])
    pos_after = get_pos()
    
    if pos_before == pos_after:
        # Try again (handles turning in place or battle screen delay)
        mgba.press_buttons([direction, "sleep 450"])
        pos_after = get_pos()
        
        attempts = 0
        while pos_before == pos_after and attempts < 10:
            run_from_battle()
            mgba.press_buttons([direction, "sleep 450"])
            pos_after = get_pos()
            attempts += 1
    return pos_after

def walk_to(target_x, target_y):
    max_steps = 100
    steps = 0
    while steps < max_steps:
        pos = get_pos()
        x, y = pos['x'], pos['y']
        if x == target_x and y == target_y:
            print(f"Successfully arrived at ({target_x}, {target_y})!")
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

print("Starting at:", get_pos())

# 1. Walk UP Column 5 to Row 6 (5, 6)
if not walk_to(5, 6):
    print("Failed to walk to (5, 6)")
    sys.exit(1)

# 2. Walk RIGHT along Row 6 to (26, 6)
if not walk_to(26, 6):
    print("Failed to walk to (26, 6)")
    sys.exit(1)

# 3. Step RIGHT to drop down!
print("Stepping onto pitfall at (26, 6)...")
mgba.press_buttons(["Right", "sleep 2500"])
print("Position after drop:", get_pos())
mgba.take_screenshot()
