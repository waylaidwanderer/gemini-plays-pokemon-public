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
            return False
    return True

print("Exploring left side of 11F...")
# We start at (3, 15)
if walk_to(1, 15):
    # Try to walk Down
    pos = mgba.get_coordinates()
    print(f"Standing at ({pos['x']}, {pos['y']}). Trying to walk Down...")
    mgba.press_buttons(["Down"])
    time.sleep(0.3)
    pos2 = mgba.get_coordinates()
    if pos == pos2:
        print("Down is BLOCKED. Trying to press A...")
        mgba.press_buttons(["A"])
        time.sleep(0.5)
        mgba.press_buttons(["Down"])
        time.sleep(0.3)
        pos3 = mgba.get_coordinates()
        if pos == pos3:
            print("Still BLOCKED Down after A.")
        else:
            print(f"Down SUCCESS to ({pos3['x']}, {pos3['y']}) after A!")
    else:
        print(f"Down SUCCESS to ({pos2['x']}, {pos2['y']})!")

screenshot_file = mgba.take_screenshot()
print(f"Screenshot taken: {screenshot_file}")
