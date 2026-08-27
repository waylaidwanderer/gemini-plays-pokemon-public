import mgba
import time
from PIL import Image

def handle_any_menu_or_battle():
    time.sleep(0.1)
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file)
    img_std = img.resize((160, 144), Image.Resampling.NEAREST)
    
    black_or_white = 0
    total_pixels = 0
    for y in range(115, 140):
        for x in range(10, 150):
            r, g, b = img_std.getpixel((x, y))[:3]
            total_pixels += 1
            is_bw = (r < 50 and g < 50 and b < 50) or (r > 200 and g > 200 and b > 200)
            if is_bw:
                black_or_white += 1
                
    percentage = black_or_white / total_pixels
    if percentage > 0.90:
        print(f"Menu/Dialogue detected! (B/W: {percentage*100:.2f}%)")
        mgba.press_buttons(["B"])
        time.sleep(0.4)
        
        # Check if still in battle
        scr_file2 = mgba.take_screenshot()
        img2 = Image.open(scr_file2)
        img_std2 = img2.resize((160, 144), Image.Resampling.NEAREST)
        black_or_white2 = 0
        for y in range(115, 140):
            for x in range(10, 150):
                r, g, b = img_std2.getpixel((x, y))[:3]
                is_bw = (r < 50 and g < 50 and b < 50) or (r > 200 and g > 200 and b > 200)
                if is_bw:
                    black_or_white2 += 1
        percentage2 = black_or_white2 / total_pixels
        
        if percentage2 > 0.90:
            print("Still in battle. Running...")
            mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A"])
            time.sleep(1.5)
            # Dismiss run text
            for _ in range(5):
                mgba.press_buttons(["B"])
                time.sleep(0.3)
        return True
    return False

# Ensure battle screen is dismissed
for _ in range(3):
    mgba.press_buttons(["B"])
    time.sleep(0.2)

start = mgba.get_coordinates()
start_tuple = (start["x"], start["y"])
print("BFS Robust Start position:", start_tuple)

# Bidirectional graph
# maps coord_tuple -> set of neighbor_tuples
graph = {}
blocked_tiles = set()
visited = { start_tuple }

dirs = {
    "Up": (0, -1),
    "Down": (0, 1),
    "Left": (-1, 0),
    "Right": (1, 0)
}

def add_edge(u, v):
    if u not in graph:
        graph[u] = set()
    if v not in graph:
        graph[v] = set()
    graph[u].add(v)
    graph[v].add(u)

def find_shortest_path(src, dst):
    if src == dst:
        return []
    queue = [src]
    paths = {src: []}
    visited_nodes = {src}
    
    while queue:
        curr = queue.pop(0)
        if curr == dst:
            return paths[curr]
        for neighbor in graph.get(curr, []):
            if neighbor not in visited_nodes and neighbor not in blocked_tiles:
                visited_nodes.add(neighbor)
                # find direction
                dx = neighbor[0] - curr[0]
                dy = neighbor[1] - curr[1]
                direction = None
                for d, (v_dx, v_dy) in dirs.items():
                    if v_dx == dx and v_dy == dy:
                        direction = d
                        break
                paths[neighbor] = paths[curr] + [direction]
                queue.append(neighbor)
    return None

def navigate_to(target):
    # Dynamically find current position and walk to target
    pos = mgba.get_coordinates()
    curr = (pos["x"], pos["y"])
    if curr == target:
        return True
        
    path = find_shortest_path(curr, target)
    if path is None:
        print(f"No path in graph from {curr} to {target}!")
        return False
        
    print(f"Navigating from {curr} to {target} via path: {path}")
    for d in path:
        mgba.press_buttons([d])
        time.sleep(0.4)
        handle_any_menu_or_battle()
        
    # Verify arrival
    pos = mgba.get_coordinates()
    curr = (pos["x"], pos["y"])
    if curr == target:
        return True
    print(f"Arrived at {curr} instead of {target}!")
    return False

# Target exit
exit_tile = (5, 27)

# We will maintain a frontier of unexplored but discovered walkable nodes
frontier = [start_tuple]

steps = 0
max_steps = 300

while frontier and steps < max_steps:
    # Find the closest frontier node from our actual current position
    pos = mgba.get_coordinates()
    curr_tuple = (pos["x"], pos["y"])
    
    if curr_tuple == exit_tile:
        print("REACHED THE EXIT TILE!")
        break
        
    # Find closest frontier
    best_f = None
    best_path = None
    for f in frontier:
        path = find_shortest_path(curr_tuple, f)
        if path is not None:
            if best_path is None or len(path) < len(best_path):
                best_f = f
                best_path = path
                
    if best_f is None:
        # No reachable frontier, let's explore neighbors of current tile
        best_f = curr_tuple
        if best_f not in frontier:
            frontier.append(best_f)
            
    # Navigate to best_f
    if curr_tuple != best_f:
        if not navigate_to(best_f):
            # Failed to navigate, let's handle desync
            pos = mgba.get_coordinates()
            curr_tuple = (pos["x"], pos["y"])
            print(f"Navigation failed. Resynced to current position: {curr_tuple}")
            # If we ended up somewhere, let's add it to visited
            visited.add(curr_tuple)
            if curr_tuple not in graph:
                graph[curr_tuple] = set()
            continue
            
    # We are now at best_f
    curr_tuple = best_f
    if best_f in frontier:
        frontier.remove(best_f)
        
    print(f"Exploring from {curr_tuple}...")
    
    # Try all 4 directions
    for d, (dx, dy) in dirs.items():
        neighbor = (curr_tuple[0] + dx, curr_tuple[1] + dy)
        if neighbor in visited or neighbor in blocked_tiles:
            continue
            
        print(f"  Testing {d} to {neighbor}...")
        mgba.press_buttons([d])
        time.sleep(0.4)
        
        handle_any_menu_or_battle()
        pos_after = mgba.get_coordinates()
        pos_after_tuple = (pos_after["x"], pos_after["y"])
        
        if pos_after_tuple == neighbor:
            # Walkable!
            print(f"  Walkable discovered: {neighbor}")
            visited.add(neighbor)
            add_edge(curr_tuple, neighbor)
            frontier.append(neighbor)
            
            # Step back
            rev_d = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}[d]
            mgba.press_buttons([rev_d])
            time.sleep(0.4)
            handle_any_menu_or_battle()
        else:
            # Blocked!
            print(f"  Blocked/solid: {neighbor}")
            blocked_tiles.add(neighbor)
            
    steps += 1

print(f"Finished BFS. Visited {len(visited)} tiles. Exit found? {exit_tile in visited}")
if exit_tile in visited:
    print("Navigating to exit at (5, 27)...")
    if navigate_to(exit_tile):
        print("At exit! Stepping DOWN to exit the mansion...")
        mgba.press_buttons(["Down"])
        time.sleep(2.5)
        print("Final position after exit:", mgba.get_coordinates())
    else:
        print("Failed to navigate to exit tile!")
else:
    print("Exit tile (5, 27) not found reachable!")
