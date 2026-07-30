import mgba
import time

def walk_to(target_x, target_y):
    pos = mgba.get_coordinates()
    print(f"Walking to ({target_x}, {target_y}) from {pos}")
    
    while pos['x'] != target_x or pos['y'] != target_y:
        dx = target_x - pos['x']
        dy = target_y - pos['y']
        
        button = None
        if dy > 0:
            button = "Down"
        elif dy < 0:
            button = "Up"
        elif dx > 0:
            button = "Right"
        elif dx < 0:
            button = "Left"
            
        if not button:
            break
            
        mgba.press_buttons([button])
        time.sleep(0.1)
        
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            # Try once more
            time.sleep(0.3)
            mgba.press_buttons([button])
            time.sleep(0.1)
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                print(f"Blocked at {pos}")
                return False
        pos = new_pos
    return True

# 1. Walk from Gym to (10, 22)
walk_to(12, 29)
walk_to(10, 29)
walk_to(10, 22)

# 2. Walk to (22, 22)
walk_to(22, 22)

# Now, let's explore UP from (22, 22) to see what is there
pos = mgba.get_coordinates()
print(f"At {pos}, starting upward exploration...")
for y in range(21, 10, -1):
    mgba.press_buttons(["Up"])
    time.sleep(0.1)
    new_pos = mgba.get_coordinates()
    if new_pos == pos:
        print(f"Blocked going Up at {pos}")
        break
    pos = new_pos
    print(f"Reached {pos}")

# Let's see what is to the Right of our current position
pos = mgba.get_coordinates()
print(f"At {pos}, exploring Right...")
for x in range(pos['x'] + 1, 40):
    mgba.press_buttons(["Right"])
    time.sleep(0.1)
    new_pos = mgba.get_coordinates()
    if new_pos == pos:
        print(f"Blocked going Right at {pos}")
        break
    pos = new_pos
    print(f"Reached {pos}")

screenshot_path = mgba.take_screenshot()
print(f"Screenshot taken: {screenshot_path}")
