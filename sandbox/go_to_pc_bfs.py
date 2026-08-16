import bridge
import time

def solve_path(start, target, blocked_edges, blocked_tiles):
    # BFS to find the shortest path from start to target
    # transitions are only 4-directional
    queue = [[start]]
    visited = {start}
    
    while queue:
        path = queue.pop(0)
        curr = path[-1]
        
        if curr == target:
            return path
            
        x, y = curr
        neighbors = [
            ((x, y-1), "Up"),
            ((x, y+1), "Down"),
            ((x-1, y), "Left"),
            ((x+1, y), "Right")
        ]
        
        for neighbor, direction in neighbors:
            nx, ny = neighbor
            # Check map boundary in Fuchsia City (0-39, 0-35)
            if nx < 0 or nx > 39 or ny < 0 or ny > 35:
                continue
            if neighbor in blocked_tiles:
                continue
            edge = (curr, neighbor)
            if edge in blocked_edges:
                continue
                
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
                
    return None

def navigate_to(target_x, target_y):
    target = (target_x, target_y)
    blocked_edges = set()
    blocked_tiles = set()
    
    # Pre-populate known solid blocks in Fuchsia City to save steps
    # Rooftops at Rows 22-23, Columns 12-23
    for x in range(12, 24):
        for y in range(22, 24):
            blocked_tiles.add((x, y))
            
    # Regular house at (22, 13)
    blocked_tiles.add((22, 13))
    
    # Pokémon Center at Columns 18-21, Rows 22-27 (except we enter at (19, 27) from south)
    for x in range(18, 22):
        for y in range(22, 27):
            blocked_tiles.add((x, y))
            
    # Warden's House at Columns 26-29, Rows 25-27
    for x in range(26, 30):
        for y in range(25, 28):
            blocked_tiles.add((x, y))
            
    stuck_count = 0
    last_pos = None
    
    while True:
        curr = bridge.get_coordinates()
        if curr is None:
            time.sleep(0.5)
            continue
            
        curr_tuple = (curr[0], curr[1])
        if curr_tuple == target:
            print(f"Successfully arrived at target: {curr_tuple}")
            return True
            
        path = solve_path(curr_tuple, target, blocked_edges, blocked_tiles)
        if path is None or len(path) < 2:
            print("No path found to target! We might be completely blocked.")
            return False
            
        next_tile = path[1]
        
        # Determine movement button
        cx, cy = curr_tuple
        nx, ny = next_tile
        if nx > cx:
            btn = "Right"
        elif nx < cx:
            btn = "Left"
        elif ny > cy:
            btn = "Down"
        elif ny < cy:
            btn = "Up"
            
        print(f"At {curr_tuple}, moving {btn} to {next_tile}...")
        bridge.press_buttons([btn])
        time.sleep(0.44)
        
        # Check if we moved
        after = bridge.get_coordinates()
        if after is None:
            continue
            
        after_tuple = (after[0], after[1])
        if after_tuple == curr_tuple:
            # We bumped! Mark this edge as blocked
            print(f"BUMPED! Transition from {curr_tuple} to {next_tile} is blocked.")
            blocked_edges.add((curr_tuple, next_tile))
            # Also block the reverse to be clean
            blocked_edges.add((next_tile, curr_tuple))
            stuck_count += 1
            if stuck_count > 5:
                print("Stuck too many times, mashing B/A to clear possible text...")
                bridge.press_buttons(["B", "A", "B"])
                time.sleep(0.5)
                stuck_count = 0
        else:
            stuck_count = 0

# Start navigating from current position to (19, 28)
navigate_to(19, 28)
