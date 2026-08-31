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

def fall():
    # Monotonic path from (22, 7) to (26, 6) on 3F East in State A:
    # 1. Walk to (19, 7)
    # 2. Walk UP Column 19 to Row 4: (19, 4)
    # 3. Walk Right to (21, 4)
    # 4. Walk UP Column 21 to Row 3: (21, 3)
    # 5. Walk Right along Row 3 to Column 26: (26, 3)
    # 6. Walk DOWN Column 26 to (26, 6) to trigger fall!
    
    path = [
        (22, 7),
        (21, 7),
        (20, 7),
        (19, 7),
        (19, 6),
        (19, 5),
        (19, 4),
        (20, 4),
        (21, 4),
        (21, 3),
        (22, 3),
        (23, 3),
        (24, 3),
        (25, 3),
        (26, 3),
        (26, 4),
        (26, 5),
        (26, 6)
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
        
        # If we fell, we will warp to a different map (coordinates change drastically)
        if abs(cx - 26) + abs(cy - 6) > 10:
            print("WARPED! Successfully fell through pitfall to 1F East fenced room! New position:", pos)
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
    fall()
