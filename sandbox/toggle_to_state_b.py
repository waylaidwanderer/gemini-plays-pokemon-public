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

# Starting at (1, 11) on 3F West in State B
print("1. Walking UP to (1, 9)...")
walk_to(1, 9)
print("2. Walking RIGHT along Row 9 to (12, 9)...")
walk_to(12, 9)
print("3. Walking UP Column 12 to (12, 6)...")
walk_to(12, 6)
print("4. Walking straight RIGHT along Row 6 to pitfall at (26, 6)...")
walk_to(26, 6)

# Step DOWN to drop
print("5. Dropping through pitfall...")
walk_step("Down")
time.sleep(2.0)

print("Arrived on 1F East inside fenced room! Final Position:", get_pos())
sc = mgba.take_screenshot()
print("Final Screenshot:", sc)
