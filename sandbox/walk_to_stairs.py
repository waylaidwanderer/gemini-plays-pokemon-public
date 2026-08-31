import mgba
import time

def flee_battle():
    print("Wild battle! Fleeing...")
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.3)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.3)

def walk_step(action):
    pos = mgba.get_coordinates()
    x, y = pos['x'], pos['y']
    mgba.press_buttons([action])
    time.sleep(0.4)
    new_pos = mgba.get_coordinates()
    if new_pos == {'x': x, 'y': y}:
        flee_battle()
        mgba.press_buttons([action])
        time.sleep(0.4)
        new_pos = mgba.get_coordinates()
    return new_pos

def main():
    # Currently at (5, 6) on 3F West in State A
    # Path to (5, 10) stairs:
    # Down to (5, 10)
    path = [
        ("Down", 5, 7),
        ("Down", 5, 8),
        ("Down", 5, 9),
        ("Down", 5, 10) # Triggers warp to 2F West (5, 11)
    ]
    
    idx = 0
    stuck_count = 0
    last_pos = None
    
    print("Walking down Column 5 on 3F West to 2F West stairs...")
    while idx < len(path):
        action, tx, ty = path[idx]
        pos = mgba.get_coordinates()
        x, y = pos['x'], pos['y']
        
        # Warp check: if coordinates changed to something not in our path segment
        if last_pos is not None and last_pos != (x, y) and (x, y) not in [(p[1], p[2]) for p in path]:
            print(f"Warp detected! Landed at: ({x}, {y})")
            break
            
        if x == tx and y == ty:
            idx += 1
            stuck_count = 0
            continue
            
        if last_pos == (x, y):
            stuck_count += 1
            if stuck_count > 2:
                print("Stuck! Fleeing...")
                flee_battle()
                stuck_count = 0
                continue
        else:
            stuck_count = 0
            last_pos = (x, y)
            
        walk_step(action)
        
    time.sleep(1.5)
    pos = mgba.get_coordinates()
    print("New Position after 2F West transition:", pos)

if __name__ == "__main__":
    main()
