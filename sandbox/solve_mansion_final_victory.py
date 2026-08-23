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

# Starting on 3F West in State A (7, 10)
print("1. Walking to 3F West switch (2, 11) from (7, 10)...")
walk_to(7, 13)
walk_to(1, 13)
walk_to(1, 11)

# Face Right and press A to toggle switch to State B
print("Toggling 3F West switch to State B...")
mgba.press_buttons(["Right", "sleep 200", "A", "sleep 500"])

# Verify we can walk to (12, 9) in State B
print("2. Walking to 3F East (12, 9) in State B...")
walk_to(1, 12)
walk_to(6, 12)
walk_to(6, 9)
walk_to(12, 9)
print("Arrived on 3F East! Position:", mgba.get_coordinates())

# 3. Walk to the Mewtwo switch at (12, 11) and toggle back to State A
print("3. Walking to switch at (12, 11)...")
walk_to(12, 10)
# Face Down and press A to toggle switch back to State A
print("Toggling 3F East switch to State A...")
mgba.press_buttons(["Down", "sleep 200", "A", "sleep 500"])

# 4. Walk to Row 6, then to Column 19, then to Balcony
print("4. Walking to balcony in State A...")
walk_to(12, 6)
walk_to(19, 6)
walk_to(19, 18)

# Drop down balcony
print("Dropping down the balcony at (19, 18)...")
mgba.press_buttons(["Down", "sleep 800"])
time.sleep(1.5)

print("Arrived on B1F East! Position:", mgba.get_coordinates())

