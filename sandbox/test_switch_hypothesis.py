import mgba
import time

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("In battle! Running...")
    for _ in range(18):
        mgba.press_buttons(["B", "sleep 150"])
    mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 2000"])
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 150"])
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

# Start at (9, 9)
print("Walking to (2, 13)...")
walk_to(2, 9)
walk_to(2, 13)

# Test walking right along Row 13
print("Testing walking right from (2, 13) to (11, 13)...")
for col in range(3, 12):
    try:
        walk_to(col, 13)
        print(f"Reached ({col}, 13)")
    except Exception as e:
        print(f"FAILED to reach ({col}, 13): {e}")
        break

print("Final position:", get_pos())
sc = mgba.take_screenshot()
print("Final Screenshot:", sc)
