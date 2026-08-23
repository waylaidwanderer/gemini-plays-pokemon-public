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

# Starting at (5, 11) on Cinnabar Island in State A
print("Starting Master Route to B1F East...")
print("Initial position:", mgba.get_coordinates())

# 1. Walk to mansion entrance and enter
print("Walking to mansion entrance...")
walk_to(6, 11)
walk_to(6, 3)
mgba.press_buttons(["Up", "sleep 400"]) # warp into 1F West
time.sleep(1.5)
print("Position inside Mansion:", mgba.get_coordinates())

# 2. Warp UP to 2F West
print("Walking to 1F West stairs...")
walk_to(5, 11)
walk_to(8, 11)
walk_to(8, 10)
walk_to(5, 10)
mgba.press_buttons(["Left", "sleep 400"]) # warp to 2F West
time.sleep(1.5)
print("Position on 2F West:", mgba.get_coordinates())

# 3. Cross to 2F East on Row 3
print("Crossing to 2F East on Row 3...")
walk_to(5, 3)
walk_to(21, 3)
print("Position on 2F East:", mgba.get_coordinates())

# 4. Walk to (15, 12) and warp UP to 3F East
print("Walking to 2F East stairs entrance at (15, 12)...")
walk_to(15, 3)
walk_to(15, 12)
print("Stepping UP onto stairs to warp...")
walk_step("Up")
time.sleep(1.5)
print("Position on 3F East:", mgba.get_coordinates())

# 5. Walk Column 17 to Balcony (19, 18)
print("Walking to Balcony...")
walk_to(17, 11)
walk_to(17, 18)
walk_to(19, 18)
print("Arrived at Balcony! Drop over...")
walk_step("Down")
time.sleep(2.0)
print("Landed on B1F East! Position:", mgba.get_coordinates())
sc = mgba.take_screenshot()
print("Screenshot saved to:", sc)
