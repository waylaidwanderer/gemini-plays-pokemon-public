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

def walk_1f_to_b1f_east():
    # 100% open path on 1F from (12, 12) to B1F East stairs
    path = [
        (12, 12),
        (12, 11), (12, 10), (12, 9), (12, 8), (12, 7), (12, 6), # Up Column 12 to Row 6
        (13, 6), (14, 6), (15, 6), (16, 6), (17, 6), (18, 6), (19, 6), (20, 6), (21, 6), (22, 6), (23, 6), (24, 6), (25, 6), # Right along Row 6
        (25, 7), (25, 8), (25, 9), (25, 10), (25, 11), (25, 12), (25, 13), # Down Column 25 (Gate open in State A)
        (25, 14), # Inside fenced room
        (26, 14) # Stairs to B1F East
    ]
    
    idx = 0
    stuck_count = 0
    last_pos = None
    
    while idx < len(path):
        action_target = path[idx]
        pos = mgba.get_coordinates()
        x, y = pos['x'], pos['y']
        print(f"Current Position: ({x}, {y})")
        
        # Warp check: if we warped down to B1F East, we are no longer on 1F.
        # Let's detect if we reached (26, 14) on 1F.
        if x == 26 and y == 14:
            print("Arrived at B1F East stairs! Stepping onto them...")
            mgba.press_buttons(["Right", "sleep 1000"])
            break
            
        if (x, y) in path:
            curr_idx = path.index((x, y))
            if curr_idx > idx:
                idx = curr_idx
            tx, ty = path[idx + 1]
            print(f"Index: {idx}, Next Target: ({tx}, {ty})")
            
            # Determine button press
            if tx < x:
                action = "Left"
            elif tx > x:
                action = "Right"
            elif ty < y:
                action = "Up"
            else:
                action = "Down"
        else:
            # Fallback if displaced off-path
            print("Displaced off-path! Finding closest path tile...")
            closest_tile = min(path, key=lambda t: abs(t[0] - x) + abs(t[1] - y))
            cx, cy = closest_tile
            print(f"Closest Path Tile: ({cx}, {cy})")
            if cx < x:
                action = "Left"
            elif cx > x:
                action = "Right"
            elif cy < y:
                action = "Up"
            else:
                action = "Down"
                
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
    print("Final Position after path execution:", pos)

walk_1f_to_b1f_east()
