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

# Phase 1: Walk to 3F West stairs at (7, 10) to warp DOWN to 2F West
print("Phase 1: Navigating to 3F West stairs...")
walk_to(1, 13)
walk_to(5, 13)
walk_to(7, 11)
print("Stepping UP to warp down to 2F West...")
walk_step("Up") # Step UP to warp down
time.sleep(1.5)
print("Position after warp down to 2F West (should be 7, 11):", get_pos())

# Phase 2: Walk UP to Row 3 and cross to 2F East (18, 3)
print("Phase 2: Navigating to Row 3 and crossing to 2F East...")
walk_to(7, 11) # make sure we are off the stairs
walk_to(6, 11)
walk_to(6, 3)
walk_to(18, 3)

# Phase 3: Walk DOWN Column 18 to Row 10 on 2F East (18, 10)
print("Phase 3: Navigating DOWN Column 18 to Row 10...")
walk_to(18, 10)

# Phase 4: Walk LEFT along Row 10 to Column 15 (15, 11) and warp UP to 3F East
print("Phase 4: Navigating to 3F East stairs at (15, 11)...")
walk_to(15, 11)
print("Stepping UP to warp UP to 3F East...")
walk_step("Up") # Step UP to warp UP
time.sleep(1.5)
print("Position after warp UP to 3F East:", get_pos())
mgba.take_screenshot()
