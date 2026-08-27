import mgba
import time

# BFS to map all reachable tiles on 1F West from our current position (5, 16)
# We will use a parent map to find paths, and systematically visit all reachable tiles.

start = mgba.get_coordinates()
print("BFS Start position:", start)

queue = [start]
visited = { (start["x"], start["y"]) }
parent = {} # maps child_coord (tuple) -> (direction_to_child, parent_coord_tuple)

# Direction vectors
dirs = {
    "Up": (0, -1),
    "Down": (0, 1),
    "Left": (-1, 0),
    "Right": (1, 0)
}
rev_dirs = {
    "Up": "Down",
    "Down": "Up",
    "Left": "Right",
    "Right": "Left"
}

def get_path_to(target_tuple):
    path = []
    curr = target_tuple
    while curr in parent:
        d, p = parent[curr]
        path.append(d)
        curr = p
    path.reverse()
    return path

def navigate_to(target_tuple, current_tuple):
    # First, find path from current to target
    # But since we are back-tracking, we can just walk back to start, then walk to target.
    # Or, find path from current to start, then start to target.
    # Actually, a simpler way is to walk from current back to start by reversing our path,
    # then walk from start to target.
    
    # Path from start to current:
    path_start_to_curr = get_path_to(current_tuple)
    # Walk back to start:
    for d in reversed(path_start_to_curr):
        rev_d = rev_dirs[d]
        mgba.press_buttons([rev_d])
        time.sleep(0.4)
        
    # Walk from start to target:
    path_start_to_target = get_path_to(target_tuple)
    for d in path_start_to_target:
        mgba.press_buttons([d])
        time.sleep(0.4)

current_pos = (start["x"], start["y"])

try:
    while queue:
        curr_coord = queue.pop(0)
        curr_tuple = (curr_coord["x"], curr_coord["y"])
        
        # Move player to curr_tuple
        if curr_tuple != current_pos:
            navigate_to(curr_tuple, current_pos)
            current_pos = curr_tuple
            
        # Verify position
        actual = mgba.get_coordinates()
        actual_tuple = (actual["x"], actual["y"])
        if actual_tuple != curr_tuple:
            print(f"Desync! Expected {curr_tuple}, got {actual_tuple}")
            break
            
        # Try all 4 directions
        for d, (dx, dy) in dirs.items():
            neighbor_tuple = (curr_tuple[0] + dx, curr_tuple[1] + dy)
            if neighbor_tuple in visited:
                continue
                
            # Try moving
            mgba.press_buttons([d])
            time.sleep(0.4)
            pos_after = mgba.get_coordinates()
            pos_after_tuple = (pos_after["x"], pos_after["y"])
            
            if pos_after_tuple == neighbor_tuple:
                # Walkable!
                print(f"Discovered walkable: {pos_after_tuple}")
                visited.add(neighbor_tuple)
                parent[neighbor_tuple] = (d, curr_tuple)
                queue.append(pos_after)
                
                # Walk back
                rev_d = rev_dirs[d]
                mgba.press_buttons([rev_d])
                time.sleep(0.4)
            else:
                # Blocked/solid
                # print(f"Solid/blocked: {neighbor_tuple}")
                pass
finally:
    # Always try to return to start
    actual = mgba.get_coordinates()
    actual_tuple = (actual["x"], actual["y"])
    print(f"Ending scan. Visited {len(visited)} tiles: {sorted(list(visited))}")
    if actual_tuple != (start["x"], start["y"]):
        print("Returning to start...")
        navigate_to((start["x"], start["y"]), actual_tuple)
        print("Returned to start:", mgba.get_coordinates())
