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
    # Currently at (2, 6) on 1F West in State B.
    # 1. Walk to 1F East northeast stairs at (27, 11)
    # Path:
    # Walk Right along Row 6 to Column 27: (3, 6) to (27, 6)
    # Walk Down Column 27 to Row 11: (27, 7) to (27, 11) (triggers warp up to 2F East)
    path = []
    for col in range(3, 28):
        path.append(("Right", col, 6))
    for row in range(7, 12):
        path.append(("Down", 27, row))
        
    idx = 0
    stuck_count = 0
    last_pos = None
    
    print("Walking from 1F West to 1F East northeast stairs...")
    while idx < len(path):
        action, tx, ty = path[idx]
        pos = mgba.get_coordinates()
        x, y = pos['x'], pos['y']
        
        # Warp check: we should land on 2F East (coordinates usually around (27, 11) or close to it)
        if last_pos is not None and last_pos != (x, y) and (x, y) not in [(p[1], p[2]) for p in path]:
            print(f"Warp detected! Landed on 2F East at: ({x}, {y})")
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
    print("Current Position on 2F East:", pos)

if __name__ == "__main__":
    main()
