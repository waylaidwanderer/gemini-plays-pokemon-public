import mgba
import time

def escape_battle():
    print("Encountered a battle! Attempting to escape...")
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    # Highlight RUN (Down, Right) and select
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    print("Escape sequence complete.")

def get_path_bfs(start, target, blocked_edges):
    queue = [[start]]
    visited = {start}
    
    while queue:
        path = queue.pop(0)
        curr = path[-1]
        if curr == target:
            return path
            
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            neighbor = (curr[0] + dx, curr[1] + dy)
            if 0 <= neighbor[0] <= 40 and 0 <= neighbor[1] <= 40:
                if neighbor not in visited:
                    edge = (curr, neighbor)
                    if edge not in blocked_edges:
                        visited.add(neighbor)
                        queue.append(path + [neighbor])
    return None

def navigate_to_waypoint(target_x, target_y, blocked_edges):
    print(f"Navigating to waypoint ({target_x}, {target_y})...")
    stuck_count = 0
    last_coords = None
    
    while True:
        curr = mgba.get_coordinates()
        if curr is None:
            print("Coordinates are None. Escape battle or wait...")
            escape_battle()
            time.sleep(0.5)
            curr = mgba.get_coordinates()
            if curr is None:
                continue
                
        cx, cy = curr['x'], curr['y']
        if cx == target_x and cy == target_y:
            print(f"Reached waypoint ({target_x}, {target_y})")
            return True
            
        # Get path using BFS
        path = get_path_bfs((cx, cy), (target_x, target_y), blocked_edges)
        if not path or len(path) < 2:
            print(f"No path found to ({target_x}, {target_y}) with current knowledge!")
            return False
            
        next_step = path[1]
        dx = next_step[0] - cx
        dy = next_step[1] - cy
        
        if dx == 1: btn = "Right"
        elif dx == -1: btn = "Left"
        elif dy == 1: btn = "Down"
        else: btn = "Up"
        
        print(f"At ({cx}, {cy}). Stepping {btn} to {next_step}...")
        mgba.press_buttons([btn])
        time.sleep(0.42)
        
        # Verify movement
        post = mgba.get_coordinates()
        if post is None:
            escape_battle()
            time.sleep(0.5)
            post = mgba.get_coordinates()
            if post is None:
                continue
                
        px, py = post['x'], post['y']
        if (px, py) == (cx, cy):
            # Bumped! Add to blocked edges
            print(f"BUMPED! Edge {((cx, cy), next_step)} is blocked.")
            blocked_edges.add(((cx, cy), next_step))
            # Also add reverse direction just in case
            blocked_edges.add((next_step, (cx, cy)))
        else:
            # Successfully moved
            if (px, py) != next_step:
                print(f"Unexpected movement: expected {next_step}, got ({px}, {py})")
                # If we changed map, return True to let caller handle map transition
                if abs(px - cx) > 5 or abs(py - cy) > 5:
                    print("Map transition detected during navigation!")
                    return True

# Let's run the sequence!
blocked_edges = set()

# Current position is in Area 1 (East) at (28, 2)
# Waypoint 1: Go to (0, 5) to transition to Area 2 (North)
print("--- NAVIGATING TO AREA 2 TRANSITION ---")
success = navigate_to_waypoint(0, 5, blocked_edges)
if success:
    print("Arrived at transition point (0, 5). Stepping Left to transition...")
    for _ in range(4):
        mgba.press_buttons(["Left"])
        time.sleep(0.5)
    time.sleep(1.5)

# Wait to confirm new map coordinates
curr = mgba.get_coordinates()
print("Current position after Area 2 transition:", curr)

