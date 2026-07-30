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
        time.sleep(0.35) # robust delay
        
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            # Try once more
            time.sleep(0.5)
            mgba.press_buttons([button])
            time.sleep(0.35)
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                print(f"Blocked at {pos}")
                return False
        pos = new_pos
    return True

# 1. Walk down and across partition to (7, 7)
walk_to(2, 7)
walk_to(7, 7)

# 2. Walk to (7, 6), right in front of the pacing Grunt
walk_to(7, 6)

# 3. Talk to the Grunt
print("Talking to the Grunt...")
mgba.press_buttons(["Up"])
time.sleep(1.0)

screenshot_path = mgba.take_screenshot()
print(f"Screenshot taken: {screenshot_path}")
