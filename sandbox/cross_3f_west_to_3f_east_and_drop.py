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

# Starting at (1, 11) on 3F West inside Mansion in State B
print("Starting on 3F West:", get_pos())

# 1. Walk to (1, 9)
walk_to(1, 9)
print("Position 1:", get_pos())

# 2. Walk Right to (12, 9) to test Column 10 walkability on Row 9
print("Attempting to cross horizontally to (12, 9)...")
walk_to(12, 9)
pos_after_cross = get_pos()
print("Position after horizontal cross attempt:", pos_after_cross)

# Check if we got stuck at Column 10 (which means x <= 9)
if pos_after_cross['x'] <= 9:
    print("Column 10 Row 9 is BLOCKED! Diverting to Row 6 bypass...")
    # Walk to Column 7 Row 9 (so we are on Column 7 to go Up to Row 6)
    walk_to(7, 9)
    # Walk Up to Row 6
    walk_to(7, 6)
    # Walk Right along Row 6 (completely open) to Column 12
    walk_to(12, 6)
    print("Bypassed to 3F East (12, 6):", get_pos())

# 3. Walk to pitfall at (26, 6) from Column 12
pos_now = get_pos()
if pos_now['y'] != 6:
    walk_to(12, 6)
print("Walking Right to pitfall at (26, 6)...")
walk_to(26, 6)

print("Should have dropped! Waiting 2 seconds...")
time.sleep(2.0)

print("Position after drop (should be 1F East inside fenced room around 25, 6):", get_pos())
sc = mgba.take_screenshot()
print("Final Screenshot:", sc)
