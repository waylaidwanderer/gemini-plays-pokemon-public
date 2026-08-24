import mgba
import time

def get_pos():
    return mgba.get_coordinates()

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction, "sleep 150"])
    pos_after = mgba.get_coordinates()
    if pos_before == pos_after:
        raise Exception(f"Collision or battle detected at {pos_before} trying to go {direction}! Terminating script.")
    return pos_after

def walk_to(target_x, target_y):
    print(f"Walking to: ({target_x}, {target_y})")
    max_steps = 30
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

# Starting at (2, 12) on 3F West inside Mansion in State B
print("Starting on 3F West:", get_pos())

# 1. Walk to (1, 9)
walk_to(1, 9)
print("Position 1:", get_pos())

# 2. Try walking Right to (12, 9)
print("Crossing to 3F East at (12, 9)...")
walk_to(12, 9)
print("Arrived at 3F East (12, 9):", get_pos())

# 3. Walk to pitfall at (26, 6) from (12, 9)
walk_to(12, 6)
print("Arrived at (12, 6):", get_pos())

walk_to(26, 6)
print("Should have dropped! Waiting 2 seconds...")
time.sleep(2.0)

print("Position after drop:", get_pos())
sc = mgba.take_screenshot()
print("Final Screenshot:", sc)
