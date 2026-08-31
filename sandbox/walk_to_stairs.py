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

def walk_robust_path():
    # Complete 100% open path from (7, 8) to the stairs at (5, 10) on 3F
    path = [
        (7, 8),
        (6, 8), (5, 8), # Walk to Column 5
        (5, 7), (5, 6), (5, 5), (5, 4), (5, 3), (5, 2), # Up to Row 2
        (6, 2), (7, 2), (8, 2), (9, 2), (10, 2), (11, 2), (12, 2), # Right to Column 12 (cross Column 9)
        (12, 3), (12, 4), (12, 5), (12, 6), (12, 7), (12, 8), (12, 9), (12, 10), (12, 11), # Down to Row 11
        (11, 11), (10, 11), (9, 11), (8, 11), (7, 11), (6, 11), (5, 11), # Left to Column 5 on Row 11 (bypassing closed gates)
        (5, 10) # Up onto the stairs warp!
    ]
    
    stuck_count = 0
    last_pos = None
    
    while True:
        pos = mgba.get_coordinates()
        x, y = pos['x'], pos['y']
        print(f"Current Position: ({x}, {y})")
        
        # Warp check: if we are on 2F West (landing at 5, 11), warp succeeded!
        # Note: B1F East or 2F West landing position. On 2F West, coordinate is (5, 11)
        # To be absolutely sure, let's also check if the map name/properties changed, but coordinates are sufficient.
        if x == 5 and y == 11 and last_pos is not None and last_pos != (5, 11):
            # Wait, we might land on 2F West (5, 11) when coming down the stairs from (5, 10).
            # Yes! This means warp succeeded!
            print("Successfully warped down to 2F West!")
            break
            
        # Find where we are in the path
        if (x, y) in path:
            curr_idx = path.index((x, y))
            if curr_idx == len(path) - 1:
                print("Arrived at stairs (5, 10)! Waiting for warp...")
                mgba.press_buttons(["Up"])
                time.sleep(1.5)
                continue
            
            # Next target tile
            tx, ty = path[curr_idx + 1]
            print(f"Next Target: ({tx}, {ty})")
            
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
            # Fallback if displaced off-path: walk to the closest path tile
            print("Displaced off-path! Finding closest path tile...")
            # Simple Manhattan distance
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

print("Starting robust walk to stairs...")
walk_robust_path()
