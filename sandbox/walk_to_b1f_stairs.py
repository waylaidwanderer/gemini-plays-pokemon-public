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

def walk_to_fenced_room():
    # Path from (22, 7) to inside fenced room at (25, 14):
    path = [
        (22, 7),
        (22, 6),
        (23, 6),
        (24, 6),
        (25, 6),
        (25, 7),
        (25, 8),
        (25, 9),
        (25, 10),
        (25, 11),
        (25, 12),
        (25, 13), # Gate (open in State A)
        (25, 14)  # Inside
    ]
    
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
        
        # If we warped, coordinates will change drastically
        if abs(cx - 25) + abs(cy - 14) > 10:
            print("Warped! New position:", pos)
            return True
            
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
        
        new_pos = mgba.get_coordinates()
        if new_pos == {'x': cx, 'y': cy}:
            stuck_count += 1
            if stuck_count > 1:
                print("Stuck! Running flee/clear routine...")
                flee_battle()
                stuck_count = 0
                post_flee = mgba.get_coordinates()
                if post_flee == {'x': cx, 'y': cy}:
                    print("Physical wall/obstacle at", pos, "heading to", (tx, ty))
                    break
        else:
            stuck_count = 0
            
    # Now let's explore inside the fenced room
    print("Testing tiles inside fenced room...")
    test_tiles = [
        (25, 14),
        (26, 14),
        (27, 14),
        (28, 14)
    ]
    for target in test_tiles:
        pos = mgba.get_coordinates()
        cx, cy = pos['x'], pos['y']
        
        direction = None
        if target[0] > cx: direction = "Right"
        elif target[0] < cx: direction = "Left"
        elif target[1] > cy: direction = "Down"
        elif target[1] < cy: direction = "Up"
        
        if direction is not None:
            print(f"Testing step from ({cx}, {cy}) to {target} via {direction}")
            mgba.press_buttons([direction])
            time.sleep(1.0)
            new_pos = mgba.get_coordinates()
            if abs(new_pos['x'] - cx) + abs(new_pos['y'] - cy) > 2:
                print("WARPED! New position after warp:", new_pos)
                return True
                
    print("Search inside fenced room completed. No warp.")
    return False

if __name__ == "__main__":
    walk_to_fenced_room()
