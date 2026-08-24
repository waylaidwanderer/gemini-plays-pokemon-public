import mgba
import time
import sys

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("In battle! Running...")
    # Press B to dismiss any dialogue
    for _ in range(3):
        mgba.press_buttons(["B", "sleep 100"])
    # Press Right, Down, A to select RUN
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 800"])
    # Clear "Got away safely!" text
    for _ in range(3):
        mgba.press_buttons(["B", "sleep 100"])

button_count = 0

def walk_step_robust(direction):
    global button_count
    pos_before = mgba.get_coordinates()
    
    if button_count > 60:
        print("Button count near limit! Exiting script to prevent abort.")
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
                print("Button count limit reached! Exiting.")
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
    max_steps = 40
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

# 1. Walk from (7, 8) to (6, 8)
print("1. Walking to (6, 8)...")
walk_to(6, 8)

# 2. Walk to (6, 11)
print("2. Walking to (6, 11)...")
walk_to(6, 11)

# 3. Walk to (5, 11)
print("3. Walking to (5, 11)...")
walk_to(5, 11)

# 4. Walk to (5, 13)
print("4. Walking to (5, 13)...")
walk_to(5, 13)

# 5. Walk to (1, 13)
print("5. Walking to (1, 13)...")
walk_to(1, 13)

# 6. Walk UP Column 1 to Row 6 (1, 6)
print("6. Walking UP Column 1 to (1, 6)...")
walk_to(1, 6)

# 7. Walk Right along Row 6 to 3F East pitfall at (26, 6)
print("7. Walking horizontally along Row 6 to pitfall at (26, 6)...")
walk_to(26, 6)

# Wait for falling animation to finish
print("Fell through pit! Waiting 3.5 seconds...")
time.sleep(3.5)
landing_pos = get_pos()
print("Landed on 1F East inside fenced room:", landing_pos)
