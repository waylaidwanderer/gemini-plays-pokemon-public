import mgba
import time

# Let's perform a BFS to find all walkable tiles in the current map
# Starting from the current position

start_pos = mgba.get_coordinates()
print(f"Starting exploration from: {start_pos}")

walkable = set()
walkable.add((start_pos['x'], start_pos['y']))

queue = [(start_pos['x'], start_pos['y'])]
parent = {}

def get_path(target):
    path = []
    curr = target
    while curr in parent:
        path.append(curr)
        curr = parent[curr]
    path.reverse()
    return path

# To move to a tile, we find the path from current position
# and press the buttons to walk there.
def walk_path(path):
    curr = mgba.get_coordinates()
    curr_tup = (curr['x'], curr['y'])
    
    # We find where we are in the path
    if curr_tup not in path and curr_tup != start_pos:
        # If we are lost, walk back to start_pos
        # (This is a simplified assumption; pathing from scratch is safer)
        return False
        
    for node in path:
        pos = mgba.get_coordinates()
        dx = node[0] - pos['x']
        dy = node[1] - pos['y']
        
        button = None
        if dy > 0:
            button = "Down"
        elif dy < 0:
            button = "Up"
        elif dx > 0:
            button = "Right"
        elif dx < 0:
            button = "Left"
            
        if button:
            mgba.press_buttons([button])
            time.sleep(0.35)
            
            new_pos = mgba.get_coordinates()
            if (new_pos['x'], new_pos['y']) != node:
                # Failed to move
                return False
    return True

# Let's just do a simple coordinate scanning by trying to move.
# To avoid getting stuck, we can just try to move 1 step in each direction from our current position,
# and if it succeeds, we record it, then step back. This is very safe and doesn't require complex BFS.

# Let's write a recursive-backtracking or simple depth-first search that maps walkable tiles.
visited = set()
walkable = set()

def explore_dfs(x, y):
    walkable.add((x, y))
    visited.add((x, y))
    
    for direction, (dx, dy, btn, rev_btn) in {
        "Up": (0, -1, "Up", "Down"),
        "Down": (0, 1, "Down", "Up"),
        "Left": (-1, 0, "Left", "Right"),
        "Right": (1, 0, "Right", "Left")
    }.items():
        nx, ny = x + dx, y + dy
        if (nx, ny) in visited:
            continue
            
        # Try to step in direction
        pos_before = mgba.get_coordinates()
        mgba.press_buttons([btn])
        time.sleep(0.35)
        pos_after = mgba.get_coordinates()
        
        if (pos_after['x'], pos_after['y']) == (nx, ny):
            # Success! Walkable.
            explore_dfs(nx, ny)
            # Step back
            mgba.press_buttons([rev_btn])
            time.sleep(0.35)
        elif (pos_after['x'], pos_after['y']) == (pos_before['x'], pos_before['y']):
            # Blocked, so not walkable
            visited.add((nx, ny))
        else:
            # Warped!
            print(f"WARP DETECTED when going {direction} from ({x}, {y}) to {pos_after}")
            # Step back to return
            mgba.press_buttons([rev_btn])
            time.sleep(1.0) # wait for warp back
            visited.add((nx, ny))

curr = mgba.get_coordinates()
explore_dfs(curr['x'], curr['y'])

print("--- WALKABLE TILES FOUND ---")
print(sorted(list(walkable)))
