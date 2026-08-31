import mgba
import time

def flee_battle():
    print("Wild battle! Fleeing...")
    # Clean up screen text
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.3)
    # Select RUN
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    # Clear "Got away safely!"
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.3)

def walk_to_stairs():
    # Robust, monotonic path from (28, 7) to B1F East Stairs at (22, 7) on 1F East:
    path = [
        (28, 7),
        (28, 6),
        (28, 5),
        (28, 4),
        (27, 4),
        (26, 4),
        (25, 4),
        (25, 3),
        (24, 3),
        (23, 3),
        (22, 3),
        (21, 3),
        (21, 4),
        (20, 4),
        (19, 4),
        (19, 5),
        (19, 6),
        (19, 7),
        (20, 7),
        (21, 7),
        (22, 7)
    ]
    
    # Initialize current_idx to the closest point in the entire path
    pos = mgba.get_coordinates()
    cx, cy = pos['x'], pos['y']
    min_dist = 999999
    closest_idx = 0
    for i, (tx, ty) in enumerate(path):
        dist = abs(tx - cx) + abs(ty - cy)
        if dist < min_dist:
            min_dist = dist
            closest_idx = i
    current_idx = closest_idx
    print(f"Initialized path index to {current_idx}/{len(path)-1} at current position ({cx}, {cy})")
    
    stuck_count = 0
    while current_idx < len(path):
        pos = mgba.get_coordinates()
        cx, cy = pos['x'], pos['y']
        
        # If we reached the stairs and warped, we will detect map/coordinate change
        if cx == 22 and cy == 7:
            print("Standing on B1F East Stairs (22, 7)!")
            # Take step to trigger warp if not warped automatically
            mgba.press_buttons(["A"])
            time.sleep(1.5)
            new_pos = mgba.get_coordinates()
            print("Position after warp attempt:", new_pos)
            break
            
        # Monotonic path progression (check from furthest lookahead down to current_idx)
        best_idx = current_idx
        for i in range(min(current_idx + 4, len(path) - 1), current_idx - 1, -1):
            dist = abs(path[i][0] - cx) + abs(path[i][1] - cy)
            if dist <= 1:
                best_idx = i
                break
                
        current_idx = max(current_idx, best_idx)
        
        if cx == path[current_idx][0] and cy == path[current_idx][1]:
            target_idx = min(current_idx + 1, len(path) - 1)
        else:
            target_idx = current_idx
            
        tx, ty = path[target_idx]
        
        # Get direction
        direction = None
        if tx > cx: direction = "Right"
        elif tx < cx: direction = "Left"
        elif ty > cy: direction = "Down"
        elif ty < cy: direction = "Up"
        
        if direction is None:
            current_idx += 1
            continue
            
        print(f"Current: ({cx}, {cy}) | Path Index: {current_idx}/{len(path)-1} | Heading to: ({tx}, {ty}) via {direction}")
        mgba.press_buttons([direction])
        time.sleep(0.4)
        
        # Check movement
        new_pos = mgba.get_coordinates()
        if new_pos == {'x': cx, 'y': cy}:
            stuck_count += 1
            if stuck_count > 1:
                print("Stuck! Running flee/clear routine...")
                flee_battle()
                stuck_count = 0
                post_flee = mgba.get_coordinates()
                if post_flee == {'x': cx, 'y': cy}:
                    print("This is a physical wall! Stopping script.")
                    break
        else:
            stuck_count = 0

if __name__ == "__main__":
    walk_to_stairs()
