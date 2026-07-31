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
            
        # Try to move 1 step
        pos_before = pos
        mgba.press_buttons([button])
        time.sleep(0.35)
        pos = get_stable_coords()
        
        # Change-detection collision check
        if pos == pos_before:
            # We hit an obstacle! Try once more with a longer delay in case of lag
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

# 1. Start at (19, 19)
# 2. Walk Left to (16, 19)
# 3. Walk Up to (16, 10)
# 4. Walk Right to (28, 10)
# 5. Walk Down to (28, 19)

success = walk_to(16, 19)
if success:
    success = walk_to(16, 10)
if success:
    success = walk_to(28, 10)
if success:
    success = walk_to(28, 19)

if success:
    print("Reached (28, 19) successfully! Trying UP to enter the Game Corner...")
    mgba.press_buttons(["Up"])
    time.sleep(1.2)
    print(f"Final coordinates: {get_stable_coords()}")
else:
    print("Navigation aborted due to collision/error.")

scr = mgba.take_screenshot()
print(f"Screenshot saved at: {scr}")
