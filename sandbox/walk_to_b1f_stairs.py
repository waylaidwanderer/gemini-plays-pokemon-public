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

def walk_down_column_26():
    # Safe path down Column 26 on 1F East
    # We step Right to (26, 3) first, then walk Down Column 26.
    path = [
        (25, 3),
        (26, 3), # Step Right to Column 26
        (26, 4), (26, 5), (26, 6), (26, 7), (26, 8), (26, 9), (26, 10), (26, 11), (26, 12), (26, 13), (26, 14) # Down Column 26
    ]
    
    idx = 0
    stuck_count = 0
    last_pos = None
    
    while idx < len(path):
        action_target = path[idx]
        pos = mgba.get_coordinates()
        x, y = pos['x'], pos['y']
        print(f"Current Position: ({x}, {y})")
        
        # Warp check: if we are no longer on 1F East (our coordinate changes to B1F East, or we can't find ourselves on 1F), we warped!
        # If our position changes to something else, we print it and break.
        if last_pos is not None and last_pos != (x, y) and (x, y) not in path:
            print(f"Warp detected! New Position: ({x}, {y})")
            break
            
        if (x, y) in path:
            curr_idx = path.index((x, y))
            if curr_idx > idx:
                idx = curr_idx
                
            if idx == len(path) - 1:
                # We reached (26, 14). Let's see if we warped or if the stairs are here.
                # In Pokemon Red/Blue, the stairs to B1F are usually on Row 12 or Row 14.
                # Let's check if the coordinate changes
                print("Arrived at the end of Column 26! Testing for warp...")
                # Press Right or Down to activate warp if we are standing on it
                mgba.press_buttons(["Right"])
                time.sleep(1.5)
                break
                
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
    print("Final Position after loop:", pos)

walk_down_column_26()
