import mgba
import time

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("In battle! Running...")
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 100"])
    mgba.press_buttons(["Right", "sleep 150", "Down", "sleep 150", "A", "sleep 500"])
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
    print(f"Walking to: ({target_x}, {target_y})")
    max_steps = 100
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

# Starting at (9, 10) on 2F East in State A facing DOWN
print("PHASE 1: Warping UP to 3F East...")
mgba.press_buttons(["Down", "sleep 400"]) # Steps DOWN onto stairs at (9, 11) to warp
time.sleep(1.5)
print("Position on 3F East (should be 12, 11):", get_pos())

# PHASE 2: Walk Left to 3F West (7, 11) in State A
print("PHASE 2: Walking Left to 3F West (7, 11)...")
walk_to(7, 11)

# PHASE 3: Walk Row 13 detour to switch at (2, 11) on 3F West
print("PHASE 3: Walking detour to switch at (2, 11)...")
walk_to(7, 13)
walk_to(1, 13)
walk_to(1, 11)

# PHASE 4: Toggle switch to State B
print("PHASE 4: Toggling switch to State B...")
mgba.press_buttons(["Right", "sleep 250", "A", "sleep 500", "B", "sleep 250"])
print("State B active! Position:", get_pos())
sc = mgba.take_screenshot()
print("Screenshot:", sc)
