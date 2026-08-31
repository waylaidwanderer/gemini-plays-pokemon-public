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

def walk_and_warp_down():
    # Complete path from (11, 9) to (7, 10) to warp DOWN
    path = [
        ("Down", 11, 10),
        ("Down", 11, 11),
        ("Left", 10, 11),
        ("Left", 9, 11),
        ("Left", 8, 11),
        ("Left", 7, 11),
        ("Up", 7, 10)
    ]
    
    idx = 0
    stuck_count = 0
    last_pos = None
    
    while idx < len(path):
        action, tx, ty = path[idx]
        pos = mgba.get_coordinates()
        x, y = pos['x'], pos['y']
        print(f"Index: {idx}, Action: {action}, Target: ({tx}, {ty}), Current: ({x}, {y})")
        
        # Warp check: if we executed Up to (7, 10) (idx == 6) and are now at (7, 11), we warped!
        if idx == 6 and x == 7 and y == 11:
            print("Successfully warped down to 1F West!")
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

walk_and_warp_down()
