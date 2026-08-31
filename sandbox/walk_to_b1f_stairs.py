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
    idx = 0
    stuck_count = 0
    
    while idx < len(target_path):
        tx, ty = target_path[idx]
        pos = mgba.get_coordinates()
        cx, cy = pos['x'], pos['y']
        
        # If we reached the target tile, go to next
        if cx == tx and cy == ty:
            idx += 1
            stuck_count = 0
            continue
            
        # Determine direction
        direction = get_dir(cx, cy, tx, ty)
        if direction is None:
            idx += 1
            continue
            
        print(f"Current: ({cx}, {cy}) | Heading to target {idx}: ({tx}, {ty}) via {direction}")
        
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
