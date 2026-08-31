import mgba
import time

def flee_battle():
    print("Wild battle! Fleeing...")
    # First, press B multiple times to advance/clear intro text
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.3)
    # At battle menu: select RUN (Down, Right, A) or if cursor is at ITEM (Right, A)
    # To be extremely safe, we press B, then select RUN
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.0)
    # Clear got away text
    for _ in range(4):
        mgba.press_buttons(["B"])
        time.sleep(0.3)

def walk_east():
    # Target path from (15, 3):
    # 1. Step Right to (16, 3)
    # 2. Step Up to (16, 2)
    # 3. Step Up to (16, 1)
    # 4. Step Right to (22, 1)
    
    path = [
        ("Right", 16, 3),
        ("Up", 16, 2),
        ("Up", 16, 1),
        ("Right", 17, 1),
        ("Right", 18, 1),
        ("Right", 19, 1),
        ("Right", 20, 1),
        ("Right", 21, 1),
        ("Right", 22, 1)
    ]
    
    idx = 0
    stuck_count = 0
    last_pos = None
    
    while idx < len(path):
        action, tx, ty = path[idx]
        pos = mgba.get_coordinates()
        x, y = pos['x'], pos['y']
        print(f"Index: {idx}, Action: {action}, Target: ({tx}, {ty}), Current: ({x}, {y})")
        
        # If we successfully reached the final target or warped to 3F (landing at 22, 1 on 3F)
        # Note: on 3F East, the coordinates are also (22, 1).
        # We can detect if map transition happened by the fact that we can't step left anymore or if we successfully finished.
        if x == 22 and y == 1:
            print("Arrived at 22, 1! Making sure we warp...")
            mgba.press_buttons(["Up"])
            time.sleep(1.5)
            break
            
        # If we are already at the target tile for this step, advance
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

print("Walking to 2F East stairs...")
walk_east()
