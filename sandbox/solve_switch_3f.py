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

print("Current coordinates:", mgba.get_coordinates())

# 1. Walk to switch at (2, 11) avoiding stairs at (5, 10)
print("Walking to (6, 12)...")
walk_to(6, 12)
print("Walking to (2, 12)...")
walk_to(2, 12)

# 2. Turn UP to face switch at (2, 11) and toggle to State B
print("Toggling switch to State B...")
mgba.press_buttons(["Up", "sleep 150", "A", "sleep 500"]) # Press A on switch
mgba.press_buttons(["A", "sleep 500"]) # Select YES
mgba.press_buttons(["B", "sleep 200", "B", "sleep 200"]) # Clear text

# 3. Walk to 2F East Row 3 Column 18
print("Walking back to Column 6...")
walk_to(6, 12)
print("Walking UP Column 6 to Row 3...")
walk_to(6, 3)
print("Walking horizontally on Row 3 to Column 18...")
walk_to(18, 3)

# 4. Walk DOWN Column 18 to stairs at (18, 10) to warp DOWN to 1F East
print("Walking DOWN Column 18 to warp to 1F East...")
walk_to(18, 10)

time.sleep(1.5)
print("Final coordinates after script:", mgba.get_coordinates())
screenshot_file = mgba.take_screenshot()
print("Screenshot saved to:", screenshot_file)
