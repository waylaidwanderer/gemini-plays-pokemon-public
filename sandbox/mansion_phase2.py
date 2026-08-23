import mgba
import time

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("In battle! Running...")
    for _ in range(12):
        mgba.press_buttons(["B", "sleep 120"])
    mgba.press_buttons(["Down", "sleep 120", "Right", "sleep 120", "A", "sleep 1500"])
    for _ in range(4):
        mgba.press_buttons(["B", "sleep 120"])
    time.sleep(1.5)

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

# Starting at (10, 7) on 1F West
print("Walking to (10, 11)...")
walk_to(10, 11)
print("Walking to (6, 11)...")
walk_to(6, 11)
print("Walking to (6, 10)...")
walk_to(6, 10)
print("Warping LEFT to 2F West...")
walk_step("Left")
time.sleep(1.5)
print("Arrived on 2F West. Position:", get_pos())

# On 2F West: (5, 11) -> (7, 11) -> (7, 10) warp UP
print("Walking to (7, 11) on 2F West...")
walk_to(7, 11)
print("Warping UP to 3F West...")
walk_step("Up")
time.sleep(1.5)

print("Arrived on 3F West! Final Position:", get_pos())
sc = mgba.take_screenshot()
print("Screenshot:", sc)
