import mgba
import time

def run_from_battle():
    print("In battle! Running...")
    # Press B multiple times to clear any text
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 150"])
    # Select RUN (Right, Down, A)
    mgba.press_buttons(["Right", "sleep 150", "Down", "sleep 150", "A", "sleep 600"])
    # Clear safe escape text
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

# Starting at (5, 27) in State A
print("Starting ascent to 3F West in State A...")
print("Initial position:", mgba.get_coordinates())

# 1. Walk from (5, 27) to (5, 10) and warp UP to 2F West
print("1. Warp UP to 2F West...")
walk_to(5, 11)
walk_to(8, 11)
walk_to(8, 10)
walk_to(5, 10)
mgba.press_buttons(["Left", "sleep 400"]) # Step LEFT onto (5, 10) to warp
time.sleep(1.5)
print("Position on 2F West:", mgba.get_coordinates())

# 2. Warp UP to 3F West
print("2. Warp UP to 3F West...")
walk_to(7, 11)
mgba.press_buttons(["Up", "sleep 400"]) # Step UP onto stairs at (7, 10) to warp
time.sleep(1.5)
print("Arrived on 3F West! Position:", mgba.get_coordinates())

# Save screenshot to confirm landing
sc = mgba.take_screenshot()
print("Screenshot saved to:", sc)
