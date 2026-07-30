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

# Walk back to the southern plaza
walk_to(16, 10)
walk_to(16, 22)
walk_to(31, 22)
walk_to(31, 28)

screenshot_path = mgba.take_screenshot()
print(f"Reached southern plaza! Screenshot taken: {screenshot_path}")
