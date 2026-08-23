import mgba
import time

def run_from_battle():
    print("In battle! Running...")
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
    return pos_after

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

# Starting at (1, 10) on 2F West in State A
print("Starting 2F East Exploration in State B...")
print("Initial position:", mgba.get_coordinates())

# 1. Walk to 2F West stairs at (7, 10) and warp UP to 3F West
print("Walking to stairs to 3F West...")
walk_to(4, 10)
walk_to(7, 10)
mgba.press_buttons(["Up", "sleep 400"]) # warp UP
time.sleep(1.5)
print("Position on 3F West:", mgba.get_coordinates())

# 2. Walk to Mewtwo statue on 3F West and toggle to State B
print("Walking to Mewtwo statue switch at (2, 11)...")
walk_to(3, 11)
walk_to(3, 13)
walk_to(1, 13)
walk_to(1, 11)
# Face Right and toggle
print("Toggling Mewtwo statue switch to State B...")
mgba.press_buttons(["Right", "sleep 200", "A", "sleep 500", "B", "sleep 200"])

# 3. Walk to stairs on 3F West at (5, 10) and warp DOWN to 2F West
print("Walking to stairs to 2F West...")
walk_to(1, 13)
walk_to(5, 13)
walk_to(5, 10)
mgba.press_buttons(["Left", "sleep 400"]) # Step LEFT onto (5, 10) to warp
time.sleep(1.5)
print("Position on 2F West (State B):", mgba.get_coordinates())

# 4. Cross to 2F East Row 3
print("Crossing to 2F East on Row 3...")
walk_to(5, 3)
walk_to(21, 3)
print("Arrived on 2F East! Position:", mgba.get_coordinates())

# 5. Save screenshot and look around
sc = mgba.take_screenshot()
print("Screenshot saved to:", sc)
