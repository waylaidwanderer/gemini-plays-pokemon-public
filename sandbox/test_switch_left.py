import mgba
import time

def step_strict(direction, target_x, target_y):
    for attempt in range(2):
        pos_before = mgba.get_coordinates()
        mgba.press_buttons([direction])
        time.sleep(0.4)
        pos_after = mgba.get_coordinates()
        if pos_after['x'] == target_x and pos_after['y'] == target_y:
            return "SUCCESS"
        time.sleep(0.1)
    return "BLOCKED"

def walk_to(target_x, target_y):
    pos = mgba.get_coordinates()
    while pos['x'] != target_x or pos['y'] != target_y:
        dx = target_x - pos['x']
        dy = target_y - pos['y']
        if dx > 0: step = "Right"
        elif dx < 0: step = "Left"
        elif dy > 0: step = "Down"
        elif dy < 0: step = "Up"
        else: break
        
        mgba.press_buttons([step])
        time.sleep(0.4)
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            print(f"Blocked trying to walk to ({target_x}, {target_y})")
            return False
        pos = new_pos
    return True

print("Walking to (2, 11)...")
walk_to(2, 11)

print("Facing Left and pressing A (4-press sequence)...")
mgba.press_buttons(["Left"])
time.sleep(0.4)

# 4 A-press sequence with delays
for i in range(1, 5):
    print(f"A-press {i}...")
    mgba.press_buttons(["A"])
    time.sleep(1.5)

print("Walking to (3, 11)...")
walk_to(3, 11)

print("Testing if gate at (4, 11) is open...")
res = step_strict("Right", 4, 11)
print(f"Gate test result: {res}. Current position: {mgba.get_coordinates()}")

