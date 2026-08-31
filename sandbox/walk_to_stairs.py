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

def step_on_stairs(action, tx, ty):
    # This function steps on the stair tile and waits for map load
    print(f"Stepping onto stairs at ({tx}, {ty}) via {action}...")
    walk_step(action)
    time.sleep(1.5)
    new_pos = mgba.get_coordinates()
    print("New Position after stairs:", new_pos)
    return new_pos

def walk_step(action):
    pos = mgba.get_coordinates()
    x, y = pos['x'], pos['y']
    mgba.press_buttons([action])
    time.sleep(0.4)
    new_pos = mgba.get_coordinates()
    if new_pos == {'x': x, 'y': y}:
        flee_battle()
        mgba.press_buttons([action])
        time.sleep(0.4)
        new_pos = mgba.get_coordinates()
    return new_pos

def main():
    # Currently at (8, 6) on 1F West
    # 1. Walk to stairs at (7, 8) on 1F West
    path_to_1f_stairs = [(8, 7), (8, 8), (7, 8)]
    walk_path_robust(path_to_1f_stairs)
    
    # Take stairs to 2F West (step on (7, 8) again to trigger warp if not triggered)
    pos = mgba.get_coordinates()
    if pos['x'] == 7 and pos['y'] == 8:
        # Step UP or Down? The stairs is at (7, 8), we step on it.
        # It should trigger warp immediately.
        pass
        
    time.sleep(1.0)
    pos = mgba.get_coordinates()
    print("Current Position on 2F West:", pos)
    
    # 2. On 2F West: walk to 2F East northeast stairs at (22, 1)
    # Landing on 2F West is typically around (7, 8).
    # Path to 2F East stairs:
    # Walk Down to Row 11: (7, 11)
    # Walk Right to 2F East Row 11: (22, 11)?
    # Wait, let's check if Row 11 is open across the whole floor on 2F in State A!
    # Yes, "On 2F, since State A gates on Row 11 are OPEN, walk freely to 2F East."
    # Let's write the 2F path:
    path_2f = []
    # From current 2F position, walk to (7, 11)
    path_2f.extend([(7, 9), (7, 10), (7, 11)])
    # Walk Right to Column 22 on Row 11
    for col in range(8, 23):
        path_2f.append((col, 11))
    # Walk Up Column 22 to the northeast stairs at (22, 1)
    for row in range(10, 0, -1):
        path_2f.append((22, row))
        
    walk_path_robust(path_2f)
    
    # Take stairs UP to 3F East (landing at 22, 1)
    print("Stepping UP to 3F East...")
    pos = mgba.get_coordinates()
    print("Completed transition. Position should be on 3F East. Current:", pos)

if __name__ == "__main__":
    main()
