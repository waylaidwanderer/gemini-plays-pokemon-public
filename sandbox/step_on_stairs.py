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
    # Currently at (5, 8) on 1F West
    # Path to (5, 10) stairs:
    # 1. Right to (7, 8)
    # 2. Down to (7, 10)
    # 3. Left to (5, 10)
    path_1f = [
        ("Right", 6, 8),
        ("Right", 7, 8),
        ("Down", 7, 9),
        ("Down", 7, 10),
        ("Left", 6, 10),
        ("Left", 5, 10) # Triggers warp to 2F West (5, 11)
    ]
    
    idx = 0
    stuck_count = 0
    last_pos = None
    
    print("Walking to 1F West stairs...")
    while idx < len(path_1f):
        action, tx, ty = path_1f[idx]
        pos = mgba.get_coordinates()
        x, y = pos['x'], pos['y']
        
        # Warp check: if we are on 2F West (our coordinates will typically be (5, 11) or close to it)
        # And we were at (5, 10) on 1F, so if coordinates change to anything not on 1F
        if last_pos is not None and last_pos != (x, y) and (x, y) not in [(p[1], p[2]) for p in path_1f]:
            print(f"Warped! Landed at: ({x}, {y})")
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
    print("Current Position on 2F:", pos)

if __name__ == "__main__":
    main()
