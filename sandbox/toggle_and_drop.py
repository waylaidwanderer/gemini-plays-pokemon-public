import mgba
import time
import sys

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("In battle! Running...")
    for _ in range(3):
        mgba.press_buttons(["B", "sleep 100"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 800"])
    for _ in range(3):
        mgba.press_buttons(["B", "sleep 100"])

button_count = 0

def walk_step_robust(direction):
    global button_count
    pos_before = mgba.get_coordinates()
    
    if button_count > 45:
        print("Button limit reached. Exiting.")
        sys.exit(0)
        
    mgba.press_buttons([direction, "sleep 180"])
    button_count += 1
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        run_from_battle()
        button_count += 8
        mgba.press_buttons([direction, "sleep 180"])
        button_count += 1
        pos_after = mgba.get_coordinates()
        
        attempts = 0
        while pos_before == pos_after and attempts < 4:
            print(f"Blocked at {pos_before} attempting {direction}. Retrying...")
            time.sleep(0.4)
            if button_count > 45:
                print("Button limit reached! Exiting.")
                sys.exit(0)
            mgba.press_buttons([direction, "sleep 180"])
            button_count += 1
            pos_after = mgba.get_coordinates()
            if pos_before != pos_after:
                break
            run_from_battle()
            button_count += 8
            attempts += 1
    return pos_after

def walk_to(target_x, target_y):
    print(f"Walking to: ({target_x}, {target_y})")
    max_steps = 20
    steps = 0
    while steps < max_steps:
        pos = mgba.get_coordinates()
        x, y = pos['x'], pos['y']
        if x == target_x and y == target_y:
            return True
            
        if x < target_x:
            walk_step_robust("Right")
        elif x > target_x:
            walk_step_robust("Left")
        elif y < target_y:
            walk_step_robust("Down")
        elif y > target_y:
            walk_step_robust("Up")
        steps += 1
    return False

# Starting position
start_pos = get_pos()
print("Starting position:", start_pos)

# 1. Walk from (1, 11) to (1, 12)
walk_to(1, 12)

# 2. Walk to (2, 12)
walk_to(2, 12)

# Verify position is (2, 12)
pos = get_pos()
if pos['x'] != 2 or pos['y'] != 12:
    print("Failed to reach (2, 12). Current position:", pos)
    sys.exit(0)

# 3. Face UP
print("Facing UP...")
mgba.press_buttons(["Up", "sleep 200"])
button_count += 1

# 4. Toggle the switch to State B
print("4. Toggling Mewtwo switch...")
mgba.press_buttons(["A", "sleep 600"])
mgba.press_buttons(["A", "sleep 600"])
for _ in range(3):
    mgba.press_buttons(["B", "sleep 150"])
time.sleep(1.0)
button_count += 5

# 5. Walk back to (1, 12)
walk_to(1, 12)

# 6. Walk UP Column 1 to Row 6 (1, 6)
walk_to(1, 6)

print("Reached (1, 6)? Position:", get_pos())
sc = mgba.take_screenshot()
print("Screenshot:", sc)
