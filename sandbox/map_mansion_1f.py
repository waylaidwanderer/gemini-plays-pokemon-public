import mgba
import time
from PIL import Image

def handle_any_menu_or_battle():
    time.sleep(0.15)
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
            for _ in range(4):
                mgba.press_buttons(["B"])
                time.sleep(0.3)
        return True
    return False

# Global state for walkable tiles on 1F West
walkable_graph = {} # node -> list of (neighbor_node, direction)
visited = set()

start = mgba.get_coordinates()
start_tuple = (start["x"], start["y"])
print("Starting exploration from:", start_tuple)

frontier = [start_tuple]
visited.add(start_tuple)

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

# Construct parent/ancestor path using current walkable graph
def find_path(src, dst):
    # Standard BFS on walkable_graph
    if src == dst:
        return []
    queue = [src]
    paths = {src: []}
    visited_nodes = {src}
    
    while queue:
        curr = queue.pop(0)
        if curr == dst:
            return paths[curr]
        for neighbor, d in walkable_graph.get(curr, []):
            if neighbor not in visited_nodes:
                visited_nodes.add(neighbor)
                paths[neighbor] = paths[curr] + [d]
                queue.append(neighbor)
    return None

def walk_path_strictly(path):
    for d in path:
        mgba.press_buttons([d])
        time.sleep(0.4)
        handle_any_menu_or_battle()

# Let's do a safe explore loop
# Instead of strict BFS traversal over mGBA, we do:
# For each frontier node, we navigate there using the known walkable graph,
# then we try to step into unvisited neighbors. If they are walkable, we add them to the graph and the frontier.

# Initialize starting node in graph
walkable_graph[start_tuple] = []

step_count = 0
max_steps = 150 # Safety limit

while frontier and step_count < max_steps:
    # Get current position
    pos = mgba.get_coordinates()
    curr_tuple = (pos["x"], pos["y"])
    
    # Choose a target frontier node
    # Let's find the closest unvisited/unexplored frontier node
    target = None
    target_path = None
    for f_node in frontier:
        path = find_path(curr_tuple, f_node)
        if path is not None:
            if target_path is None or len(path) < len(target_path):
                target = f_node
                target_path = path
                
    if target is None:
        print("No reachable frontier nodes left in graph!")
        break
        
    # Navigate to target
    if len(target_path) > 0:
        print(f"Navigating from {curr_tuple} to frontier {target} via path: {target_path}")
        walk_path_strictly(target_path)
        pos = mgba.get_coordinates()
        curr_tuple = (pos["x"], pos["y"])
        if curr_tuple != target:
            print(f"Failed to navigate to target! Ended up at {curr_tuple}")
            # Reset target pathing
            continue
            
    # Remove from frontier as we are exploring it now
    frontier.remove(target)
    
    # Try all 4 directions from target
    for d, (dx, dy) in dirs.items():
        neighbor = (curr_tuple[0] + dx, curr_tuple[1] + dy)
        if neighbor in visited:
            continue
            
        print(f"Testing step {d} to {neighbor}...")
        mgba.press_buttons([d])
        time.sleep(0.45)
        
        # Check if we successfully moved
        handle_any_menu_or_battle()
        new_pos = mgba.get_coordinates()
        new_tuple = (new_pos["x"], new_pos["y"])
        
        if new_tuple == neighbor:
            # Walkable!
            print(f"Found new walkable tile: {neighbor}")
            visited.add(neighbor)
            frontier.append(neighbor)
            
            # Update bidirectional graph
            if curr_tuple not in walkable_graph:
                walkable_graph[curr_tuple] = []
            if neighbor not in walkable_graph:
                walkable_graph[neighbor] = []
            walkable_graph[curr_tuple].append((neighbor, d))
            walkable_graph[neighbor].append((curr_tuple, rev_dirs[d]))
            
            # Walk back to target
            mgba.press_buttons([rev_dirs[d]])
            time.sleep(0.45)
            handle_any_menu_or_battle()
        else:
            # Solid
            # print(f"Tile {neighbor} is solid.")
            pass
            
    step_count += 1

print(f"Exploration complete! Visited {len(visited)} tiles.")
print("Walkable graph nodes:")
for k, v in walkable_graph.items():
    print(f"  {k} -> {[x[0] for x in v]}")
