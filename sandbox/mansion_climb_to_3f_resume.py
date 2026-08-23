import mgba
import time

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("In battle! Running...")
    # Longer sleep to fully clear intro and make sure fight menu is open
    for _ in range(18):
        mgba.press_buttons(["B", "sleep 150"])
    # Down, Right, A to select RUN
    mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 2000"])
    # Clear got away safely
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 150"])
    # Let the overworld transition load completely
    time.sleep(2.0)

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction, "sleep 150"])
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        run_from_battle()
        mgba.press_buttons([direction, "sleep 150"])
        pos_after = mgba.get_coordinates()
        
        if pos_before == pos_after:
            raise Exception(f"Blocked at {pos_before} trying to go {direction}")
    return pos_after

def walk_to(target_x, target_y):
    print(f"Walking to: ({target_x}, {target_y})")
    max_steps = 40
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

# Starting at (5, 25) inside 1F West
print("1. Walking UP Column 5 inside 1F West...")
walk_to(5, 11)
walk_to(6, 11)
walk_to(6, 10)
print("Warping LEFT to 2F West...")
walk_step("Left")
time.sleep(1.5)
print("Arrived on 2F West. Position:", get_pos())

# On 2F West: walk to (7, 11) and warp UP to 3F West
print("2. Walking to 2F West stairs at (7, 11)...")
walk_to(7, 11)
print("Warping UP to 3F West...")
walk_step("Up")
time.sleep(1.5)

print("SUCCESS! Arrived on 3F West! Final Position:", get_pos())
sc = mgba.take_screenshot()
print("Final Screenshot:", sc)
