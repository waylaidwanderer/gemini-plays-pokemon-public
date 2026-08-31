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
    # Path from (10, 7) to (7, 10) on 3F West in State B:
    # 1. Right to Column 12: (11, 7), (12, 7)
    # 2. Down Column 12 to Row 11: (12, 8), (12, 9), (12, 10), (12, 11)
    # 3. Left along Row 11 to Column 7: (11, 11), (10, 11), (9, 11), (8, 11), (7, 11)
    # 4. UP to stairs at (7, 10)
    
    path = [
        (10, 7),
        (11, 7),
        (12, 7),
        (12, 8),
        (12, 9),
        (12, 10),
        (12, 11),
    ]
    for col in range(11, 6, -1):
        path.append((col, 11))
    path.append((7, 10))
    
    stuck_count = 0
    while True:
        pos = mgba.get_coordinates()
        cx, cy = pos['x'], pos['y']
        
        # If we reached final target
        if cx == 7 and cy == 10:
            print("Reached staircase at (7, 10) on 3F West!")
            break
            
        # Find closest path node
        min_dist = 999999
        closest_idx = 0
        for i, (tx, ty) in enumerate(path):
            dist = abs(tx - cx) + abs(ty - cy)
            if dist < min_dist:
                min_dist = dist
                closest_idx = i
                
        if cx == path[closest_idx][0] and cy == path[closest_idx][1]:
            target_idx = min(closest_idx + 1, len(path) - 1)
        else:
            target_idx = closest_idx
            
        tx, ty = path[target_idx]
        
        # Get direction
        direction = None
        if tx > cx: direction = "Right"
        elif tx < cx: direction = "Left"
        elif ty > cy: direction = "Down"
        elif ty < cy: direction = "Up"
        
        if direction is None:
            break
            
        print(f"Current: ({cx}, {cy}) | Heading to target {target_idx}: ({tx}, {ty}) via {direction}")
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
                print("Post-flee coordinates:", post_flee)
                if post_flee == {'x': cx, 'y': cy}:
                    print("This is a physical wall! Stopping script.")
                    break
        else:
            stuck_count = 0

if __name__ == "__main__":
    walk_to_stairs()
