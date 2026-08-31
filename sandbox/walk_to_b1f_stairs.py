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
    # Start at current position, go to (8, 6)
    path = [(8, 6)]
    # Walk to (25, 6)
    for col in range(9, 26):
        path.append((col, 6))
    # Walk to (25, 13)
    for row in range(7, 14):
        path.append((25, row))
    # Walk inside fenced room to (25, 14)
    path.append((25, 14))
    
    walk_path_robust(path)
    
    # Once inside the fenced room, let's print our final position!
    pos = mgba.get_coordinates()
    print("Reached inside fenced room at:", pos)

if __name__ == "__main__":
    main()
