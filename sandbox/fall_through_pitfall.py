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

def walk_to_pitfall():
    # Monotonic path to (26, 4) on 3F East in State A:
    # 1. Walk DOWN Column 14 to Row 6: (14, 4) -> (14, 6)
    # 2. Walk Right along Row 6 to Column 21: (15, 6) -> (21, 6)
    # 3. Walk UP Column 21 to Row 3: (21, 5) -> (21, 3)
    # 4. Walk Right along Row 3 to Column 26: (22, 3) -> (26, 3)
    # 5. Walk DOWN Column 26 to (26, 4) (pitfall)
    
    path = []
    # Currently at (14, 3)
    path.append((14, 4))
    path.append((14, 5))
    path.append((14, 6))
    for col in range(15, 22):
        path.append((col, 6))
    path.append((21, 5))
    path.append((21, 4))
    path.append((21, 3))
    for col in range(22, 27):
        path.append((col, 3))
    path.append((26, 4))
    
    # Find closest path node to initialize current_idx
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
    
    stuck_count = 0
    while current_idx < len(path):
        pos = mgba.get_coordinates()
        cx, cy = pos['x'], pos['y']
        
        # If we reached the pitfall
        if cx == 26 and cy == 4:
            print("Standing on pitfall tile (26, 4)!")
            mgba.press_buttons(["Down"])
            time.sleep(1.5)
            new_pos = mgba.get_coordinates()
            print("Position after stepping down on pitfall:", new_pos)
            break
            
        # Monotonic path progression (check from furthest down to current_idx)
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
    walk_to_pitfall()
