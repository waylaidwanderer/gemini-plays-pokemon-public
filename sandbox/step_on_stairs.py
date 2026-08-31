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
    # Currently at (3, 6) on 1F West in State A
    # Path to (7, 11) testing the (7, 9) gate:
    # 1. Down to (3, 7)
    # 2. Right to (4, 7) (open gate)
    # 3. Right to (7, 7)
    # 4. Down to (7, 11) (passing through (7, 8), (7, 9) gate, (7, 10))
    path = [
        ("Down", 3, 7),
        ("Right", 4, 7),
        ("Right", 5, 7),
        ("Right", 6, 7),
        ("Right", 7, 7),
        ("Down", 7, 8),
        ("Down", 7, 9),
        ("Down", 7, 10),
        ("Down", 7, 11)
    ]
    
    idx = 0
    stuck_count = 0
    last_pos = None
    
    print("Walking and testing (7, 9) vertical gate in State A...")
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
        
    final_pos = mgba.get_coordinates()
    print("Final Position after walk test:", final_pos)

if __name__ == "__main__":
    main()
