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

# 1. Walk from (10, 28) to (10, 34)
walk_to(10, 34)

# 2. Walk to (22, 34)
walk_to(22, 34)

# 3. Walk to (22, 22)
walk_to(22, 22)

# 4. Explore Right from (22, 22)
pos = mgba.get_coordinates()
print(f"At {pos}, exploring Right...")
for x in range(23, 50):
    mgba.press_buttons(["Right"])
    time.sleep(0.1)
    new_pos = mgba.get_coordinates()
    if new_pos == pos:
        print(f"Blocked going Right at {pos}")
        break
    pos = new_pos
    print(f"Reached {pos}")

# 5. Let's see what is Up or Down from here
pos = mgba.get_coordinates()
print(f"At {pos}, trying to go Down...")
for y in range(pos['y'] + 1, 35):
    mgba.press_buttons(["Down"])
    time.sleep(0.1)
    new_pos = mgba.get_coordinates()
    if new_pos == pos:
        print(f"Blocked going Down at {pos}")
        break
    pos = new_pos
    print(f"Reached {pos}")

screenshot_path = mgba.take_screenshot()
print(f"Screenshot taken: {screenshot_path}")
