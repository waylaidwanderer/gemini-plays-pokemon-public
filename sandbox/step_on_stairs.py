import mgba
import time

button_count = 0

def press_buttons_safe(buttons):
    global button_count
    if button_count + len(buttons) > 25:
        print(f"Approaching button limit ({button_count} pressed). Safe abort to prevent emulator limit.")
        return False
    mgba.press_buttons(buttons)
    button_count += len(buttons)
    return True

def flee_battle():
    print("Fleeing battle...")
    for _ in range(5):
        if not press_buttons_safe(["B"]): return False
        time.sleep(0.4)
    if not press_buttons_safe(["Down", "Right", "A"]): return False
    time.sleep(2.0)
    for _ in range(3):
        if not press_buttons_safe(["B"]): return False
        time.sleep(0.4)
    return True

def walk_to_target(tx, ty):
    attempts = 0
    while attempts < 15:
        pos = mgba.get_coordinates()
        if pos['x'] == tx and pos['y'] == ty:
            return True
        
        dx = tx - pos['x']
        dy = ty - pos['y']
        if dx > 0: direction = "Right"
        elif dx < 0: direction = "Left"
        elif dy > 0: direction = "Down"
        elif dy < 0: direction = "Up"
        else: break
        
        print(f"Walking {direction} to ({tx}, {ty}) from {pos}...")
        if not press_buttons_safe([direction]):
            return False
        time.sleep(0.6)
        
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            attempts += 1
            print("No movement. Fleeing battle...")
            if not flee_battle():
                return False
        else:
            attempts = 0
            if new_pos['x'] == tx and new_pos['y'] == ty:
                return True
    return False

def main():
    print("--- Stateful Stair Climber (Down to 2F) ---")
    pos = mgba.get_coordinates()
    print("Current position:", pos)
    
    path = []
    if pos['x'] == 22 and pos['y'] == 5:
        pass # Already at (22, 5)
    elif pos['x'] == 23 and pos['y'] == 5:
        path.append((22, 5))
    elif pos['x'] == 23:
        for y in range(pos['y'] + 1, 6):
            path.append((23, y))
        path.append((22, 5))
    else:
        if pos['x'] > 23:
            for x in range(pos['x'] - 1, 22, -1):
                path.append((x, pos['y']))
        elif pos['x'] < 23:
            for x in range(pos['x'] + 1, 24):
                path.append((x, pos['y']))
                
        curr_y = pos['y']
        if curr_y < 5:
            for y in range(curr_y + 1, 6):
                path.append((23, y))
        elif curr_y > 5:
            for y in range(curr_y - 1, 4, -1):
                path.append((23, y))
                
        path.append((22, 5))
        
    print("Planned path to (22, 5):", path)
    
    # Execute path
    for i, target in enumerate(path):
        tx, ty = target
        if not walk_to_target(tx, ty):
            print(f"Failed to reach target ({tx}, {ty}). Ending run.")
            return
            
    pos = mgba.get_coordinates()
    if pos['x'] == 22 and pos['y'] == 5:
        print("At (22, 5). Stepping UP to trigger warp...")
        if press_buttons_safe(["Up"]):
            time.sleep(1.5)
            new_pos = mgba.get_coordinates()
            print("Position after stepping UP:", new_pos)
            mgba.take_screenshot()
            
if __name__ == "__main__":
    main()
