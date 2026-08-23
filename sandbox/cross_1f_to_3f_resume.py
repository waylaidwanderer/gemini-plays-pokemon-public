import mgba
import time

def run_from_battle():
    print("Stuck! Attempting to run from battle...")
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 150"])
    mgba.press_buttons(["Right", "sleep 150", "Down", "sleep 150", "A", "sleep 600"])
    for _ in range(4):
        mgba.press_buttons(["B", "sleep 150"])

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction, "sleep 150"])
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        mgba.press_buttons([direction, "sleep 150"])
        pos_after = mgba.get_coordinates()
        
        attempts = 0
        while pos_before == pos_after and attempts < 10:
            run_from_battle()
            mgba.press_buttons([direction, "sleep 150"])
            pos_after = mgba.get_coordinates()
            attempts += 1

def walk_to(target_x, target_y):
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

print("Starting State A B1F descent...")
# First press B to clear the battle text
mgba.press_buttons(["B", "sleep 300"])

# 1. Walk down Column 18 to Row 10 and warp to 1F East
walk_to(18, 10)
walk_step("Down") # step onto stairs to warp
time.sleep(1.0)
print("Position after warping to 1F East:", mgba.get_coordinates())

# 2. Walk Right to Column 22 on 1F East
walk_to(22, 10)

# 3. Walk UP Column 22 to Row 2
walk_to(22, 2)

# 4. Step UP to warp to B1F East
walk_step("Up")
time.sleep(1.5)
print("Arrived on B1F East! Position:", mgba.get_coordinates())
