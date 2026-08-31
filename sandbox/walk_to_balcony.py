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

def walk_to_balcony():
    # Target path:
    # 1. Walk Right along Row 11 to Column 12: (4, 11) to (12, 11)
    # 2. Walk UP Column 12 to Row 3: (12, 10) down to (12, 3)
    # 3. Walk Left along Row 3 to Column 10: (11, 3), (10, 3)
    # 4. Walk DOWN Column 10 to Row 16: (10, 4) down to (10, 16)
    # 5. Walk Right along Row 16 to Column 20: (11, 16) to (20, 16)
    # 6. Walk DOWN Column 20 to (20, 17) (open gate to balcony)
    # 7. Walk to (19, 17) -> (19, 18) (balcony drop)
    
    path = []
    for col in range(4, 13):
        path.append((col, 11))
    for row in range(10, 2, -1):
        path.append((12, row))
    path.append((11, 3))
    path.append((10, 3))
    for row in range(4, 17):
        path.append((10, row))
    for col in range(11, 21):
        path.append((col, 16))
    path.append((20, 17))
    path.append((19, 17))
    path.append((19, 18))
    
    stuck_count = 0
    while True:
        pos = mgba.get_coordinates()
        cx, cy = pos['x'], pos['y']
        
        # If we reached the balcony drop
        if cx == 19 and cy == 18:
            print("Arrived at balcony drop!")
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
                # If we are still stuck at the same coordinates after fleeing, it is a physical wall!
                if post_flee == {'x': cx, 'y': cy}:
                    print("This is a physical wall! Stopping script.")
                    break
        else:
            stuck_count = 0

if __name__ == "__main__":
    walk_to_balcony()
