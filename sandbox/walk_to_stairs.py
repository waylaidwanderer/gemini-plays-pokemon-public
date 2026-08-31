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
    # Path to (5, 10) stairs via Column 10:
    path = [
        ("Right", 6, 6),
        ("Right", 7, 6),
        ("Right", 8, 6),
        ("Right", 9, 6),
        ("Right", 10, 6),
        ("Down", 10, 7),
        ("Down", 10, 8),
        ("Down", 10, 9),
        ("Down", 10, 10),
        ("Left", 9, 10),
        ("Left", 8, 10),
        ("Left", 7, 10),
        ("Left", 6, 10),
        ("Left", 5, 10) # Triggers warp to 2F West
    ]
    
    idx = 0
    stuck_count = 0
    last_pos = None
    
    print("Walking on 3F West to stairs at (5, 10) via Column 10...")
    while idx < len(path):
        action, tx, ty = path[idx]
        pos = mgba.get_coordinates()
        x, y = pos['x'], pos['y']
        
        # Warp check: if coordinates changed to 2F West (usually (5, 11) or close to it)
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
