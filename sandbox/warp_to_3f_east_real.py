import mgba
import sys
import time

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

# Phase 2: Walk to Row 3 and cross to 2F East
print("1. Walking to (6, 9)...")
walk_to(6, 9)
print("2. Walking UP Column 6 to (6, 3)...")
walk_to(6, 3)
print("3. Crossing horizontally to (18, 3)...")
walk_to(18, 3)

# Phase 3: Walk DOWN Column 18 to (18, 10)
print("4. Walking DOWN Column 18 to (18, 10)...")
walk_to(18, 10)

# Phase 4: Walk LEFT to (15, 11) and warp UP to 3F East
print("5. Walking LEFT to stairs at (15, 11)...")
walk_to(15, 11)
print("Stepping UP to warp UP to 3F East...")
walk_step("Up")
time.sleep(1.5)
print("Position after warp:", get_pos())
mgba.take_screenshot()
