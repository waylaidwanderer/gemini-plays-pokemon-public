# -*- coding: utf-8 -*-
import mgba
import time

def flee_battle():
    print("Wild battle! Fleeing...")
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.3)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.0)
    for _ in range(4):
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

def walk_to_b1f_stairs_and_warp():
    # We are currently at (26, 11).
    # Path to (22, 7) stairs:
    path = [
        ("Left", 25, 11),
        ("Up", 25, 10),
        ("Left", 24, 10),
        ("Left", 23, 10),
        ("Up", 23, 9),
        ("Up", 23, 8),
        ("Up", 23, 7),
        ("Left", 22, 7) # Step Left onto the stairs at (22, 7) to warp DOWN!
    ]
    
    idx = 0
    stuck_count = 0
    last_pos = None
    
    while idx < len(path):
        action, tx, ty = path[idx]
        pos = mgba.get_coordinates()
        x, y = pos['x'], pos['y']
        print(f"Current Position: ({x}, {y})")
        
        # Warp check: if we warped, our position will change drastically (we'll land on B1F East)
        if last_pos is not None and last_pos != (x, y) and (x, y) not in [(p[1], p[2]) for p in path]:
            print(f"WARPED! New Position: ({x}, {y})")
            break
            
        if x == tx and y == ty:
            idx += 1
            stuck_count = 0
            continue
            
        if last_pos == (x, y):
            stuck_count += 1
            if stuck_count > 2:
                print("Stuck! Running flee_battle...")
                flee_battle()
                stuck_count = 0
                continue
        else:
            stuck_count = 0
            last_pos = (x, y)
            
        mgba.press_buttons([action])
        time.sleep(0.4)
        
    time.sleep(1.5)
    pos = mgba.get_coordinates()
    print("Final Position:", pos)

walk_to_b1f_stairs_and_warp()
