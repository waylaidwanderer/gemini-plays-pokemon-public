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
    # 1. Walk to (12, 11)
    # 2. Walk UP to (12, 2)
    # 3. Walk Right to (26, 2)
    # 4. Walk DOWN to (26, 4) (pitfall)
    
    path = []
    # Currently at (5, 11)
    for col in range(6, 13):
        path.append((col, 11))
    for row in range(10, 1, -1):
        path.append((12, row))
    for col in range(13, 27):
        path.append((col, 2))
    path.append((26, 3))
    path.append((26, 4))
    
    current_idx = 0
    stuck_count = 0
    
    while current_idx < len(path):
        pos = mgba.get_coordinates()
        cx, cy = pos['x'], pos['y']
        
        # If we warped/fell, we will detect map/coordinate change
        if cy == 4 and cx == 26:
            # We are on the pitfall tile. Stepping onto it or moving should trigger fall.
            print("Standing on pitfall tile (26, 4)!")
            mgba.press_buttons(["Down"])
            time.sleep(1.5)
            new_pos = mgba.get_coordinates()
            print("Position after stepping down on pitfall:", new_pos)
            break
            
        # Monotonic path progression
        best_idx = current_idx
        # Check from furthest lookahead down to current_idx
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
