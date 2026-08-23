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

print("Starting State A Chunk 1 Victory Route...")
# 1. Enter Mansion
walk_step("Up")
time.sleep(1.0)
print("Entered Mansion 1F West. Position:", mgba.get_coordinates())

# 2. Walk UP Column 5 to Row 11, then step UP onto stairs (5, 10) to warp to 2F West
walk_to(5, 11)
walk_step("Up")
time.sleep(1.0)
print("Arrived on 2F West. Position:", mgba.get_coordinates())

# 3. On 2F West, walk UP Column 5 to Row 3, then RIGHT to Column 21 on 2F East
walk_to(5, 3)
walk_to(21, 3)
print("Arrived on 2F East (Row 3). Position:", mgba.get_coordinates())

# 4. On 2F East, walk LEFT to Column 18, then DOWN Column 18 to Row 10
walk_to(18, 3)
walk_to(18, 10)
# Step DOWN to warp DOWN to 1F East
walk_step("Down")
time.sleep(1.0)
print("Arrived on 1F East! Position:", mgba.get_coordinates())
