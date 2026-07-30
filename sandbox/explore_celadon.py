import mgba
import time

# 1. Close the CUT textbox
print("Closing textbox...")
mgba.press_buttons(["A"])
time.sleep(0.5)

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
        time.sleep(0.35) # increased from 0.1 to 0.35s to allow tile animation to finish!
        
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            # Try once more with a longer pause
            print(f"Position did not change. Retrying step {button}...")
            time.sleep(0.5)
            mgba.press_buttons([button])
            time.sleep(0.35)
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                print(f"Blocked at {pos}")
                return False
        pos = new_pos
    return True

# 2. Walk UP through the cut bush gap to Row 31 pavement
walk_to(35, 31)

# 3. Walk Left along Row 31 to column 28
walk_to(28, 31)

# 4. Explore UP column 28 to find the Game Corner entrance
pos = mgba.get_coordinates()
print(f"At {pos}, exploring Upward...")
for y in range(30, 15, -1):
    mgba.press_buttons(["Up"])
    time.sleep(0.35) # increased from 0.1 to 0.35s!
    new_pos = mgba.get_coordinates()
    if new_pos == pos:
        print(f"Blocked going Up at {pos}")
        break
    pos = new_pos
    print(f"Reached {pos}")

# 5. Let's see if we can find the door around here
screenshot_path = mgba.take_screenshot()
print(f"Screenshot taken: {screenshot_path}")
