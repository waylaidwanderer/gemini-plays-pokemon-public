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

def navigate():
    # Target path:
    # 1. From current (16, 11) to (18, 11): Right, Right
    # 2. UP Column 18 to Row 7: (18, 10), (18, 9), (18, 8), (18, 7)
    # 3. Left along Row 7 to Column 5: (17, 7) down to (5, 7)
    # 4. Down Column 5 to Row 10: (5, 8), (5, 9), (5, 10)
    
    path = [
        (16, 11),
        (17, 11),
        (18, 11),
        (18, 10),
        (18, 9),
        (18, 8),
        (18, 7),
    ]
    for col in range(17, 4, -1):
        path.append((col, 7))
    path.append((5, 8))
    path.append((5, 9))
    path.append((5, 10))
    
    stuck_count = 0
    while True:
        pos = mgba.get_coordinates()
        cx, cy = pos['x'], pos['y']
        
        # If we reached final destination
        if cx == 5 and cy == 10:
            print("Reached southwest stairs!")
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
                # Double check position after fleeing
                post_flee = mgba.get_coordinates()
                print("Post-flee coordinates:", post_flee)
        else:
            stuck_count = 0

if __name__ == "__main__":
    navigate()
