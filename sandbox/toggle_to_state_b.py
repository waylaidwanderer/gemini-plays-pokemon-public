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

# Starting at (4, 10) on 3F West in State A
print("1. Walking to (4, 13)...")
walk_to(4, 13)
print("2. Walking LEFT along Row 13 to Column 1...")
walk_to(1, 13)
print("3. Walking UP Column 1 to Row 11...")
walk_to(1, 11)

# Toggle switch to State B
print("4. Toggling switch to State B...")
mgba.press_buttons(["Right", "sleep 250", "A", "sleep 500", "A", "sleep 500", "B", "sleep 250"])
print("State B activated! Position:", get_pos())

sc = mgba.take_screenshot()
print("Screenshot:", sc)
