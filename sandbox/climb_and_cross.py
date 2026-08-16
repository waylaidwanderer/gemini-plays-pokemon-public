import mgba
import time

def escape_battle():
    print("Encountered a battle! Attempting to escape...")
    for _ in range(6):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    for _ in range(6):
        mgba.press_buttons(["B"])
        time.sleep(0.1)

def step(direction):
    curr = mgba.get_coordinates()
    cx, cy = curr['x'], curr['y']
    mgba.press_buttons([direction])
    time.sleep(0.45)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == cx and new_pos['y'] == cy:
        # We only treat as battle if we are walking on verified open tiles
        escape_battle()
        time.sleep(0.5)
        after = mgba.get_coordinates()
        if after['x'] == cx and after['y'] == cy:
            return False, (cx, cy)
        return True, (after['x'], after['y'])
    return True, (new_pos['x'], new_pos['y'])

def walk_to(target_x, target_y):
    print(f"Walking to ({target_x}, {target_y})...")
    while True:
        curr = mgba.get_coordinates()
        cx, cy = curr['x'], curr['y']
        if cx == target_x and cy == target_y:
            print(f"Reached ({target_x}, {target_y})")
            return True
            
        if cx < target_x: btn = "Right"
        elif cx > target_x: btn = "Left"
        elif cy < target_y: btn = "Down"
        else: btn = "Up"
        
        success, pos = step(btn)
        if not success:
            print(f"Failed to reach ({target_x}, {target_y}) - blocked at {pos}")
            return False

# Starting at (28, 6)
print("Executing climb_and_cross.py...")

# 1. Walk LEFT along Row 6 to Column 20
walk_to(20, 6)

# 2. Walk DOWN Column 20 to Row 14
walk_to(20, 14)

# 3. Walk LEFT 1 step to (19, 14)
walk_to(19, 14)

# 4. Walk DOWN 1 step to (19, 15)
walk_to(19, 15)

# 5. Walk RIGHT 1 step to climb West Stairs onto the plateau at (20, 15)
walk_to(20, 15)

print("Final position:", mgba.get_coordinates())
mgba.take_screenshot()
