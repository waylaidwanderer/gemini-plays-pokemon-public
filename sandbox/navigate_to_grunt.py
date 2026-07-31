import mgba
import time

def get_stable_coords():
    pos1 = mgba.get_coordinates()
    time.sleep(0.1)
    pos2 = mgba.get_coordinates()
    while pos1 != pos2:
        pos1 = pos2
        time.sleep(0.1)
        pos2 = mgba.get_coordinates()
    return pos1

def walk_to(target_x, target_y):
    pos = get_stable_coords()
    print(f"Walking from {pos} to ({target_x}, {target_y})...")
    
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
            
        pos_before = pos
        mgba.press_buttons([button])
        time.sleep(0.35)
        pos = get_stable_coords()
        
        # Change-detection collision check
        if pos == pos_before:
            print(f"Blipped or blocked. Retrying {button} once...")
            time.sleep(0.4)
            mgba.press_buttons([button])
            time.sleep(0.35)
            pos = get_stable_coords()
            if pos == pos_before:
                print(f"COLLISION DETECTED at {pos_before} going {button}!")
                return False
                
        print(f"  Moved to {pos}")
        
    return True

# We are currently at (15, 8)
# Path:
# 1. Left to (11, 8)
# 2. Up to (11, 5)
# 3. Left to (10, 5)

success = walk_to(11, 8)
if success:
    success = walk_to(11, 5)
if success:
    success = walk_to(10, 5)

if success:
    print("Reached (10, 5) successfully! Facing LEFT towards the Rocket Grunt...")
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
else:
    print("Navigation aborted.")

scr = mgba.take_screenshot()
print(f"Screenshot saved at: {scr}")
