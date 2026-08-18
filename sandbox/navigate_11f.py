import mgba
import time

def walk_to(target_x, target_y):
    while True:
        pos = mgba.get_coordinates()
        curr_x, curr_y = pos['x'], pos['y']
        print(f"Position: ({curr_x}, {curr_y}) -> Target: ({target_x}, {target_y})")
        
        if curr_x == target_x and curr_y == target_y:
            break
            
        dx = target_x - curr_x
        dy = target_y - curr_y
        
        if dx != 0:
            btn = "Left" if dx < 0 else "Right"
        elif dy != 0:
            btn = "Up" if dy < 0 else "Down"
        else:
            break
            
        mgba.press_buttons([btn])
        time.sleep(0.3)
        
        new_pos = mgba.get_coordinates()
        if new_pos['x'] == curr_x and new_pos['y'] == curr_y:
            print(f"Blocked at ({curr_x}, {curr_y}) trying to move {btn}.")
            # Try to press A (it might be a locked gate!)
            print("Pressing A to unlock or talk...")
            mgba.press_buttons(["A"])
            time.sleep(0.5)
            # Check if we can move now
            mgba.press_buttons([btn])
            time.sleep(0.3)
            new_pos = mgba.get_coordinates()
            if new_pos['x'] == curr_x and new_pos['y'] == curr_y:
                print("Still blocked after pressing A. Aborting.")
                return False
            else:
                print(f"Successfully unlocked/bypassed! Now at ({new_pos['x']}, {new_pos['y']})")
    return True

print("Navigating Saffron Silph Co. 11F down Column 3...")
# Let's try to walk down Column 3 to Row 16 (bottom of the map)
walk_to(3, 16)
screenshot_file = mgba.take_screenshot()
print(f"Screenshot taken: {screenshot_file}")
print("Navigation finished!")
