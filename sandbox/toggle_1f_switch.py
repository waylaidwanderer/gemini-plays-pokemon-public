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
    # Currently at (5, 6) on 1F West
    # Path to (2, 6):
    # 1. Down to (5, 7)
    # 2. Left to (4, 7) (open gate in State A)
    # 3. Left to (3, 7)
    # 4. Left to (2, 7)
    # 5. Up to (2, 6)
    path = [
        ("Down", 5, 7),
        ("Left", 4, 7),
        ("Left", 3, 7),
        ("Left", 2, 7),
        ("Up", 2, 6)
    ]
    
    idx = 0
    stuck_count = 0
    last_pos = None
    
    print("Walking to 1F West Mewtwo switch...")
    while idx < len(path):
        action, tx, ty = path[idx]
        pos = mgba.get_coordinates()
        x, y = pos['x'], pos['y']
        
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
        
    print("Arrived below the Mewtwo switch at (2, 6). Facing UP...")
    # Face UP
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    # Toggle switch to State B (4 A-presses)
    print("Toggling switch to State B...")
    for press in range(1, 5):
        print(f"A-press {press}")
        mgba.press_buttons(["A"])
        time.sleep(2.0)
        
    final_pos = mgba.get_coordinates()
    print("Final Position:", final_pos)

if __name__ == "__main__":
    main()
