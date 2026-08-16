import bridge
import time
import json
import os

STATE_FILE = "bfs_navigation_state.json"

def load_navigation_state():
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r") as f:
                data = json.load(f)
                # Convert list of lists back to sets of tuples
                blocked_edges = set(tuple(tuple(x) for x in edge) for edge in data.get("blocked_edges", []))
                blocked_tiles = set(tuple(x) for x in data.get("blocked_tiles", []))
                print(f"Loaded state: {len(blocked_edges)} blocked edges, {len(blocked_tiles)} blocked tiles.")
                return blocked_edges, blocked_tiles
        except Exception as e:
            print("Error loading state:", e)
    return set(), set()

def save_navigation_state(blocked_edges, blocked_tiles):
    try:
        # Convert sets of tuples to lists for JSON serialization
        data = {
            "blocked_edges": [list(list(x) for x in edge) for edge in blocked_edges],
            "blocked_tiles": [list(x) for x in blocked_tiles]
        }
        with open(STATE_FILE, "w") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print("Error saving state:", e)

def solve_path(start, target, blocked_edges, blocked_tiles):
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
    blocked_edges, blocked_tiles = load_navigation_state()
    
    # Pre-populate known solid blocks in Fuchsia City to save steps
    # Rooftops at Rows 22-23, Columns 12-23
    for x in range(12, 24):
        for y in range(22, 24):
            blocked_tiles.add((x, y))
            
    # Regular house at (22, 13)
    blocked_tiles.add((22, 13))
    
    # Pokémon Center at Columns 18-21, Rows 22-27
    for x in range(18, 22):
        for y in range(22, 27):
            blocked_tiles.add((x, y))
            
    # Warden's House at Columns 26-29, Rows 25-27
    for x in range(26, 30):
        for y in range(25, 28):
            blocked_tiles.add((x, y))
            
    # Poké Mart at Columns 4-7, Rows 10-13
    for x in range(4, 8):
        for y in range(10, 14):
            blocked_tiles.add((x, y))
            
    stuck_count = 0
    
    while True:
        curr = bridge.get_coordinates()
        if curr is None:
            time.sleep(0.5)
            continue
            
        # Detect if we have entered the Gatehouse map
        # Gatehouse coordinates are typically x <= 7, y <= 8, but distinct from Fuchsia (e.g. start at (3,5) or (4,5) on red mat)
        # Let's check if current map is different by looking at Fuchsia boundaries or Gatehouse characteristics
        # Fuchsia City has y up to 35, Gatehouse has y up to 8.
        # If we are in the Gatehouse, we are warped, so our coordinates will jump from near (18, 3) to (3,5) or (4,5).
        # Let's check if the coordinates are in the Gatehouse range.
        if curr[0] == 4 and curr[1] == 5:
            print("Successfully entered the Safari Zone Gatehouse!")
            return True
            
        curr_tuple = (curr[0], curr[1])
        if curr_tuple == target:
            print(f"Reached Fuchsia gatehouse entrance at {curr_tuple}! Walking UP to enter...")
            bridge.press_buttons(["Up"])
            time.sleep(1.0)
            continue
            
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
            blocked_edges.add((next_tile, curr_tuple))
            save_navigation_state(blocked_edges, blocked_tiles)
            stuck_count += 1
            if stuck_count > 5:
                print("Stuck too many times, mashing B/A to clear possible text...")
                bridge.press_buttons(["B", "A", "B"])
                time.sleep(0.5)
                stuck_count = 0
        else:
            stuck_count = 0

# Target the Safari Gatehouse entrance door at (18, 3) in Fuchsia City
navigate_to(18, 3)
