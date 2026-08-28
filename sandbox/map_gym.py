import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

# We want to map the gym. 
# We'll represent the gym as a directed graph.
# For each walkable tile (x, y), we'll try walking in 4 directions: Up, Down, Left, Right.
# If we succeed in walking normally (i.e. coordinate matches expected), we add a bi-directional edge (if walkable back) or directed edge.
# If we spin, we record it as a one-way spin transition.
# To avoid getting stuck, we can use BFS on our known bidirectional graph to navigate back to a safe spot.

walkable_adj = {} # (x, y) -> list of (nx, ny)
spin_transitions = {} # (x, y, dir) -> (nx, ny)
blocked = set() # (x, y, dir)

# We start at current pos
start_pos = get_pos()
print("Starting map_gym.py from:", start_pos)

# Let's define a safe path-finding function using the currently known undirected/bidirectional graph
def find_path(start, target):
    if start == target:
        return []
    queue = [[start]]
    visited = {start}
    while queue:
        path = queue.pop(0)
        node = path[-1]
        for neighbor in walkable_adj.get(node, []):
            if neighbor not in visited:
                if neighbor == target:
                    return path[1:] + [neighbor]
                visited.add(neighbor)
                queue.append(path + [neighbor])
    return None

def walk_path(path):
    for node in path:
        pos = get_pos()
        # determine direction to node
        dx = node[0] - pos[0]
        dy = node[1] - pos[1]
        if dx == 1 and dy == 0:
            d = "Right"
        elif dx == -1 and dy == 0:
            d = "Left"
        elif dx == 0 and dy == 1:
            d = "Down"
        elif dx == 0 and dy == -1:
            d = "Up"
        else:
            print(f"Error: path step from {pos} to {node} is invalid!")
            return False
        
        mgba.press_buttons([d])
        time.sleep(0.55)
        new_pos = get_pos()
        if new_pos != node:
            print(f"Error: failed to follow path. Expected {node}, got {new_pos}")
            return False
    return True

# Initialize walkable_adj for start_pos
walkable_adj[start_pos] = []

to_explore = [start_pos]
visited_nodes = {start_pos}

limit = 50 # max steps/probes to avoid infinite loop
steps = 0

dirs = {
    "Up": (0, -1),
    "Down": (0, 1),
    "Left": (-1, 0),
    "Right": (1, 0)
}

try:
    while to_explore and steps < limit:
        # Sort to_explore to prefer nodes closer to current position
        curr_pos = get_pos()
        to_explore.sort(key=lambda p: abs(p[0] - curr_pos[0]) + abs(p[1] - curr_pos[1]))
        target = to_explore.pop(0)
        
        # Navigate to target using known safe path
        if get_pos() != target:
            path = find_path(get_pos(), target)
            if path is None:
                print(f"Cannot find safe path from {get_pos()} to {target}, skipping.")
                continue
            if not walk_path(path):
                print(f"Failed navigating to {target}, aborting.")
                break
        
        # Target reached. Explore 4 directions
        curr_pos = get_pos()
        print(f"\nExploring from {curr_pos}...")
        
        for d, (dx, dy) in dirs.items():
            expected = (curr_pos[0] + dx, curr_pos[1] + dy)
            
            # Skip if we already know this direction is blocked or visited
            if (curr_pos, d) in blocked:
                continue
            
            # Press button B to clear potential text, then direction
            mgba.press_buttons(["B"])
            time.sleep(0.1)
            mgba.press_buttons([d])
            time.sleep(0.55)
            
            new_pos = get_pos()
            steps += 1
            
            if new_pos == curr_pos:
                # Blocked
                print(f"  Direction {d} is BLOCKED.")
                blocked.add((curr_pos, d))
            elif new_pos == expected:
                # Normal walk
                print(f"  Direction {d} leads to {new_pos} (Normal).")
                # Add bidirectional edge
                if curr_pos not in walkable_adj:
                    walkable_adj[curr_pos] = []
                if new_pos not in walkable_adj:
                    walkable_adj[new_pos] = []
                if new_pos not in walkable_adj[curr_pos]:
                    walkable_adj[curr_pos].append(new_pos)
                if curr_pos not in walkable_adj[new_pos]:
                    walkable_adj[new_pos].append(curr_pos)
                
                if new_pos not in visited_nodes:
                    visited_nodes.add(new_pos)
                    to_explore.append(new_pos)
                
                # Step back to curr_pos
                # Opp direction
                opp_d = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}[d]
                mgba.press_buttons([opp_d])
                time.sleep(0.55)
                if get_pos() != curr_pos:
                    print(f"  WARNING: failed to step back from {new_pos} to {curr_pos}!")
                    # We might have stepped on a one-way or spinner going back!
                    # Let's break to re-evaluate
                    break
            else:
                # Spinner or one-way warp
                print(f"  SPIN/WARP DETECTED! {curr_pos} + {d} -> {new_pos}")
                spin_transitions[(curr_pos, d)] = new_pos
                
                # Since we spun, we are now at new_pos. We need to get back to curr_pos
                # Let's check if new_pos is already visited or has a known path back
                if new_pos not in visited_nodes:
                    visited_nodes.add(new_pos)
                    to_explore.append(new_pos)
                
                # Try to navigate back to curr_pos
                path_back = find_path(new_pos, curr_pos)
                if path_back:
                    print(f"  Navigating back to {curr_pos} via known path...")
                    if not walk_path(path_back):
                        print("  Failed to walk back!")
                        break
                else:
                    print(f"  No known safe path back from spin destination {new_pos} to {curr_pos}. Remaining at {new_pos}.")
                    # Since we are at new_pos now, we make it our new active target
                    break

except Exception as e:
    print("Exception occurred:", e)

print("\n--- Exploration Summary ---")
print("Walkable Adj Graph:", walkable_adj)
print("Spin Transitions:", spin_transitions)
print("Blocked:", list(blocked))
print("Current Position:", get_pos())

# Let's save the results to a local file so we don't lose them
with open("gym_map_data.txt", "w") as f:
    f.write(f"walkable_adj = {walkable_adj}\n")
    f.write(f"spin_transitions = {spin_transitions}\n")
    f.write(f"blocked = {list(blocked)}\n")
