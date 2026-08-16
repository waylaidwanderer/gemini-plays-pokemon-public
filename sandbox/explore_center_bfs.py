import mgba
import time

def escape_battle():
    # Clear any battle text
    for _ in range(6):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    # Escape
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    for _ in range(6):
        mgba.press_buttons(["B"])
        time.sleep(0.1)

def run_bfs():
    print("--- RUNNING FULL RECHABLE AREA BFS ---")
    start = mgba.get_coordinates()
    if start is None:
        print("Could not get starting coordinates.")
        return
        
    start_coords = (start['x'], start['y'])
    queue = [start_coords]
    parent_map = {start_coords: None}
    walkable = {start_coords}
    
    # We will do a physical BFS to map all reachable tiles
    directions = ["Up", "Down", "Left", "Right"]
    back_dirs = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
    
    steps_count = 0
    max_steps = 80 # Keep under the 100 button press limit
    
    # Track our physical location (we start at start_coords)
    curr_loc = start_coords
    
    def navigate_physically(target):
        nonlocal curr_loc, steps_count
        if curr_loc == target:
            return True
        # Find path from curr_loc to target using parent_map (or BFS on known walkable)
        # Since we are expanding neighbor-by-neighbor, we can just walk back to parent
        path = []
        node = target
        while node is not None:
            path.append(node)
            node = parent_map.get(node)
        path.reverse()
        
        # Now walk the path step by step
        for next_node in path[1:]:
            # Determine direction from curr_loc to next_node
            dx = next_node[0] - curr_loc[0]
            dy = next_node[1] - curr_loc[1]
            if dx == 1: d = "Right"
            elif dx == -1: d = "Left"
            elif dy == 1: d = "Down"
            else: d = "Up"
            
            mgba.press_buttons([d])
            time.sleep(0.42)
            steps_count += 1
            
            # Check coords
            actual = mgba.get_coordinates()
            if actual is None:
                escape_battle()
                time.sleep(0.5)
                actual = mgba.get_coordinates()
            
            if actual is None or (actual['x'], actual['y']) != next_node:
                print(f"Failed to step to {next_node}. Got {actual}.")
                return False
            curr_loc = next_node
        return True

    # Main BFS loop
    while queue and steps_count < max_steps:
        node = queue.pop(0)
        
        # Walk physically to 'node' to probe its neighbors
        if not navigate_physically(node):
            continue
            
        # Probe neighbors
        for d in directions:
            dx, dy = {"Up": (0, -1), "Down": (0, 1), "Left": (-1, 0), "Right": (1, 0)}[d]
            neighbor = (node[0] + dx, node[1] + dy)
            if neighbor in walkable:
                continue
                
            # Try to move physically in direction d
            mgba.press_buttons([d])
            time.sleep(0.42)
            steps_count += 1
            
            actual = mgba.get_coordinates()
            if actual is None:
                escape_battle()
                time.sleep(0.5)
                actual = mgba.get_coordinates()
                
            if actual is not None:
                ax, ay = actual['x'], actual['y']
                if (ax, ay) != node:
                    # Move succeeded! Neighbor is walkable
                    walkable.add((ax, ay))
                    parent_map[(ax, ay)] = node
                    queue.append((ax, ay))
                    
                    # Step back to node
                    mgba.press_buttons([back_dirs[d]])
                    time.sleep(0.42)
                    steps_count += 1
                    
                    back_curr = mgba.get_coordinates()
                    if back_curr is None:
                        escape_battle()
                        time.sleep(0.5)
                    curr_loc = node
                    
    print("REACHABLE TILES DISCOVERED:")
    print(sorted(list(walkable)))

run_bfs()
