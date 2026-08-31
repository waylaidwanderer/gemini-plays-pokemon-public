import mgba
import time

def flee_battle():
    print("Wild battle! Fleeing...")
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.3)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.3)

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

def run_route(path, target_map_description):
    idx = 0
    stuck_count = 0
    last_pos = None
    
    print(f"Starting route to: {target_map_description}")
    while idx < len(path):
        action, tx, ty = path[idx]
        pos = mgba.get_coordinates()
        x, y = pos['x'], pos['y']
        
        # Warp check: if coordinates changed to something not in our path segment
        if last_pos is not None and last_pos != (x, y) and (x, y) not in [(p[1], p[2]) for p in path]:
            print(f"Warp detected! Landed at: ({x}, {y})")
            return (x, y)
            
        if x == tx and y == ty:
            idx += 1
            stuck_count = 0
            continue
            
        if last_pos == (x, y):
            stuck_count += 1
            if stuck_count > 2:
                print("Stuck! Fleeing...")
                flee_battle()
                stuck_count = 0
                continue
        else:
            stuck_count = 0
            last_pos = (x, y)
            
        walk_step(action)
        
    time.sleep(1.0)
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def main():
    # --- STEP 1: 3F West to 2F West ---
    # Currently at (2, 6) on 3F West.
    # Path to (5, 10):
    # Left (to 4,5), Left (to 3,5), Down (to 3,6), Left (to 2,6)? No!
    # Let's use the verified bypassing route:
    # 1. Right to (3, 6)
    # 2. Up to (3, 5)
    # 3. Right to (4, 5)
    # 4. Right to (5, 5)
    # 5. Down to (5, 10)
    path_3f = [
        ("Right", 3, 6),
        ("Up", 3, 5),
        ("Right", 4, 5),
        ("Right", 5, 5),
        ("Down", 5, 6),
        ("Down", 5, 7),
        ("Down", 5, 8),
        ("Down", 5, 9),
        ("Down", 5, 10) # Triggers warp to 2F West (5, 11)
    ]
    land_pos = run_route(path_3f, "2F West")
    print("Landed on 2F West at:", land_pos)
    
    # --- STEP 2: 2F West to 1F West ---
    # Currently at (5, 11) on 2F West.
    # Path to (7, 10):
    # Right to (7, 11), Up to (7, 10)
    path_2f = [
        ("Right", 6, 11),
        ("Right", 7, 11),
        ("Up", 7, 10) # Triggers warp to 1F West (7, 11)
    ]
    land_pos = run_route(path_2f, "1F West")
    print("Landed on 1F West at:", land_pos)
    
    # --- STEP 3: 1F West to 1F East Fenced Room ---
    # Currently at (7, 11) on 1F West.
    # Path: Up to (7, 6) on Row 6.
    # Right to (25, 6) on 1F East.
    # Down to (25, 13) into the fenced room.
    path_1f = [
        ("Up", 7, 10),
        ("Up", 7, 9),
        ("Up", 7, 8),
        ("Up", 7, 7),
        ("Up", 7, 6),
    ]
    # Walk Right along Row 6 to Column 25
    for col in range(8, 26):
        path_1f.append(("Right", col, 6))
    # Walk Down Column 25 to (25, 13)
    for row in range(7, 14):
        path_1f.append(("Down", 25, row))
        
    land_pos = run_route(path_1f, "1F East Fenced Room")
    print("Entered Fenced Room on 1F East at:", land_pos)
    
    # --- STEP 4: Walk around the fenced room and search for B1F stairs ---
    # Let's do a simple spiral or block search in the fenced room:
    # Walkable tiles are in Columns 25-28, Rows 11-14.
    # Let's try to step on various tiles to trigger the B1F warp!
    fenced_path = [
        ("Right", 26, 13),
        ("Right", 27, 13),
        ("Down", 27, 14),
        ("Right", 28, 14),
        ("Up", 28, 13),
        ("Up", 28, 12),
        ("Left", 27, 12),
        ("Left", 26, 12),
        ("Left", 25, 12),
        ("Down", 25, 13),
        ("Down", 25, 14),
        ("Right", 26, 14),
        ("Right", 27, 14),
        ("Up", 27, 13),
        ("Up", 27, 12),
        ("Up", 27, 11), # Let's try (27, 11) just in case!
    ]
    
    # Run the fenced path search
    run_route(fenced_path, "B1F East Warp Search")

if __name__ == "__main__":
    main()
