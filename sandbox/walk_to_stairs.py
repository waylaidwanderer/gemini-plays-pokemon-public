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

def get_dir(cx, cy, tx, ty):
    if tx > cx: return "Right"
    if tx < cx: return "Left"
    if ty > cy: return "Down"
    if ty < cy: return "Up"
    return None

def walk_path_robust(target_path):
    stuck_count = 0
    
    while True:
        pos = mgba.get_coordinates()
        cx, cy = pos['x'], pos['y']
        
        # If we reached the final target, we are done!
        final_tx, final_ty = target_path[-1]
        if cx == final_tx and cy == final_ty:
            print("Reached final destination!")
            break
            
        # Find the closest point in target_path to our current position
        min_dist = 999999
        closest_idx = 0
        for i, (tx, ty) in enumerate(target_path):
            dist = abs(tx - cx) + abs(ty - cy)
            if dist < min_dist:
                min_dist = dist
                closest_idx = i
                
        # We want to head towards the next tile in the path
        if cx == target_path[closest_idx][0] and cy == target_path[closest_idx][1]:
            target_idx = min(closest_idx + 1, len(target_path) - 1)
        else:
            target_idx = closest_idx
            
        tx, ty = target_path[target_idx]
        direction = get_dir(cx, cy, tx, ty)
        if direction is None:
            break
            
        print(f"Current: ({cx}, {cy}) | Heading to target {target_idx}: ({tx}, {ty}) via {direction}")
        
        # Take step
        mgba.press_buttons([direction])
        time.sleep(0.4)
        
        # Check if we moved
        new_pos = mgba.get_coordinates()
        if new_pos == {'x': cx, 'y': cy}:
            stuck_count += 1
            if stuck_count > 1:
                print("Stuck! Attempting to flee battle / clear obstacle...")
                flee_battle()
                stuck_count = 0
        else:
            stuck_count = 0

def main():
    # Currently at (22, 7) on 2F East in State A
    # Path to (5, 10) southwest stairs on 2F West via Column 21:
    # 1. Left to Column 21: (21, 7)
    # 2. Down Column 21 to Row 11: (21, 8) to (21, 11)
    # 3. Left along Row 11 to Column 5: (20, 11) to (5, 11)
    # 4. UP to stairs at (5, 10) (triggers warp up to 3F West)
    path = [
        (21, 7),
        (20, 7),
        (19, 7),
        (19, 8),
        (19, 9),
        (19, 10),
        (19, 11),
    ]
    for col in range(18, 4, -1):
        path.append((col, 11))
    path.append((5, 10))
    
    walk_path_robust(path)
    
    # Wait for transition to 3F West
    time.sleep(1.5)
    pos = mgba.get_coordinates()
    print("New Position after 3F West transition:", pos)

if __name__ == "__main__":
    main()
