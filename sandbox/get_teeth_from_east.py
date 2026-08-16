import bridge
import time
import json
import os

def escape_battle():
    print("Encountered a battle or stuck! Attempting to escape...")
    for _ in range(5):
        bridge.press_buttons(["B"])
        time.sleep(0.1)
    bridge.press_buttons(["Down", "Right", "A"])
    time.sleep(1.2)
    for _ in range(5):
        bridge.press_buttons(["B"])
        time.sleep(0.1)
    print("Escape sequence complete.")

def solve_path(start, target, blocked_edges, blocked_tiles, max_x, max_y):
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
            if nx < 0 or nx > max_x or ny < 0 or ny > max_y:
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

def navigate_map_bfs(target_x, target_y, state_file, max_x=39, max_y=35):
    target = (target_x, target_y)
    blocked_edges = set()
    blocked_tiles = set()
    
    # Load existing state if file exists
    if os.path.exists(state_file):
        try:
            with open(state_file, "r") as f:
                data = json.load(f)
                blocked_edges = set(tuple(tuple(x) for x in edge) for edge in data.get("blocked_edges", []))
                blocked_tiles = set(tuple(x) for x in data.get("blocked_tiles", []))
                print(f"Loaded {len(blocked_edges)} blocked edges from {state_file}")
        except Exception as e:
            print("Error loading state:", e)
            
    stuck_count = 0
    last_coords = None
    
    while True:
        curr = bridge.get_coordinates()
        if curr is None:
            time.sleep(0.5)
            continue
            
        curr_tuple = (curr[0], curr[1])
        if curr_tuple == target:
            print(f"Reached target {target}!")
            return True
            
        # Detect if map transition occurred (coordinates shifted drastically away from current path region)
        # We can handle this by checking if we are far away from target, but simple target check is safer.
        
        path = solve_path(curr_tuple, target, blocked_edges, blocked_tiles, max_x, max_y)
        if path is None or len(path) < 2:
            print("No path found to target! We might be completely blocked. Backtracking...")
            # If completely blocked, clear some recent edges to allow retry
            blocked_edges.clear()
            continue
            
        next_tile = path[1]
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
        
        after = bridge.get_coordinates()
        if after is None:
            continue
            
        after_tuple = (after[0], after[1])
        if after_tuple == curr_tuple:
            print(f"BUMPED! Transition from {curr_tuple} to {next_tile} is blocked.")
            blocked_edges.add((curr_tuple, next_tile))
            blocked_edges.add((next_tile, curr_tuple))
            
            # Save state
            try:
                data = {
                    "blocked_edges": [list(list(x) for x in edge) for edge in blocked_edges],
                    "blocked_tiles": [list(x) for x in blocked_tiles]
                }
                with open(state_file, "w") as f:
                    json.dump(data, f, indent=2)
            except Exception as e:
                print("Error saving state:", e)
                
            stuck_count += 1
            if stuck_count > 4:
                print("Stuck too many times. Running escape battle...")
                escape_battle()
                stuck_count = 0
                time.sleep(0.5)
                # Recover menu if open
                bridge.press_buttons(["B", "B"])
                time.sleep(0.5)
        else:
            stuck_count = 0

# ----------------------------------------------------
# MAIN EXECUTION FLOW
# ----------------------------------------------------
# Get current coordinate to see which map we are on
curr = bridge.get_coordinates()
print("Current position:", curr)

if curr is not None:
    # 1. If we are in Area 2 (North)
    # Check if we are in the coordinates typical of Area 2
    # Area 2 has y up to 35, and we are navigating to (8, 35)
    if curr[1] <= 35 and curr[0] <= 39:
        # We might be in Area 2 or Area 3, but let's check if we are in Area 2 by verifying x >= 26 is not our target yet
        # Let's run BFS to (8, 35) for Area 2
        print("Starting Area 2 (North) Navigation...")
        if navigate_map_bfs(8, 35, "safari_area2_state.json", max_x=39, max_y=35):
            # Step Down onto (8, 36) to warp to Area 3
            print("Warping to Area 3 (West)...")
            bridge.press_buttons(["Down"])
            time.sleep(1.0)
            
    # Refresh coordinates
    curr = bridge.get_coordinates()
    print("Coordinates after potential transition:", curr)
    
    # 2. If we are in Area 3 (West)
    if curr is not None:
        print("Starting Area 3 (West) Navigation...")
        if navigate_map_bfs(19, 24, "safari_area3_state.json", max_x=29, max_y=25):
            print("Reached directly above Gold Teeth at (19, 24)!")
            print("Facing DOWN...")
            bridge.press_buttons(["Down"])
            time.sleep(0.5)
            
            print("Pressing A to retrieve Gold Teeth...")
            bridge.press_buttons(["A"])
            time.sleep(1.0)
            
            print("Clearing dialogue...")
            bridge.press_buttons(["A"])
            time.sleep(0.5)
            bridge.press_buttons(["A"])
            time.sleep(0.5)
            
            print("Successfully retrieved Gold Teeth! Current position:", bridge.get_coordinates())
