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
        time.sleep(0.35) # robust 350ms delay
        
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            # Try once more
            print(f"Position did not change. Retrying {button}...")
            time.sleep(0.5)
            mgba.press_buttons([button])
            time.sleep(0.35)
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                print(f"Blocked at {pos}")
                return False
        pos = new_pos
    return True

# 1. Walk to (3, 7) (near the entrance)
walk_to(3, 7)

# 2. Walk to (7, 7) (across the partition)
walk_to(7, 7)

# 3. Explore Right along Row 7 to find the right wall
pos = mgba.get_coordinates()
print(f"At {pos}, exploring Right...")
for x in range(8, 25):
    mgba.press_buttons(["Right"])
    time.sleep(0.35)
    new_pos = mgba.get_coordinates()
    if new_pos == pos:
        print(f"Blocked going Right at {pos}")
        break
    pos = new_pos
    print(f"Reached {pos}")

# 4. Explore Up along the right wall to find the Rocket Grunt
pos = mgba.get_coordinates()
print(f"At {pos}, exploring Upward...")
for y in range(pos['y'] - 1, 0, -1):
    mgba.press_buttons(["Up"])
    time.sleep(0.35)
    new_pos = mgba.get_coordinates()
    if new_pos == pos:
        print(f"Blocked going Up at {pos}")
        break
    pos = new_pos
    print(f"Reached {pos}")

screenshot_path = mgba.take_screenshot()
print(f"Screenshot taken: {screenshot_path}")
