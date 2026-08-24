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
    
    if button_count > 60:
        print("Button count limit reached. Exiting.")
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
            if button_count > 60:
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
    max_steps = 30
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

# 1. Walk to Column 8 Row 11 via Row 12 / Column 5
walk_to(1, 12)
walk_to(5, 12)
walk_to(5, 11)
walk_to(8, 11)

# 2. Test walk UP Column 8 to Row 6 (8, 6)
print("At (8, 11). Testing walk UP to (8, 6)...")
walk_to(8, 6)

print("Final position reached:", get_pos())
sc = mgba.take_screenshot()
print("Screenshot:", sc)
