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
            # Select RUN: in Gen 1, RUN is at bottom-right (Down, Right, A)
            mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A"])
            time.sleep(1.5)
            # Dismiss "Got away safely!" or similar text
            for _ in range(5):
                mgba.press_buttons(["B"])
                time.sleep(0.3)
        return True
    return False

# Starting position
start = mgba.get_coordinates()
start_tuple = (start["x"], start["y"])
print("BFS Start position:", start_tuple)

# Walkable graph: bidirectional connections
# maps coord_tuple -> list of (neighbor_tuple, direction_from_coord)
walkable_graph = { start_tuple: [] }
visited = { start_tuple }
queue = [start_tuple]

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

# Find path using BFS on our discovered walkable_graph
def find_path(src, dst):
    if src == dst:
        return []
    bfs_queue = [src]
    paths = {src: []}
    visited_nodes = {src}
    
    while bfs_queue:
        curr = bfs_queue.pop(0)
        if curr == dst:
            return paths[curr]
        for neighbor, d in walkable_graph.get(curr, []):
            if neighbor not in visited_nodes:
                visited_nodes.add(neighbor)
                paths[neighbor] = paths[curr] + [d]
                bfs_queue.append(neighbor)
    return None

def navigate_to(target_tuple):
    # Walk to target from wherever we are
    for attempt in range(3):
        pos = mgba.get_coordinates()
        curr_tuple = (pos["x"], pos["y"])
        if curr_tuple == target_tuple:
            return True
        path = find_path(curr_tuple, target_tuple)
        if path is None:
            print(f"No path found from {curr_tuple} to {target_tuple} in graph!")
            return False
        print(f"Navigating from {curr_tuple} to {target_tuple} via path: {path}")
        for d in path:
            mgba.press_buttons([d])
            time.sleep(0.45)
            handle_any_menu_or_battle()
        
        # Verify arrival
        pos = mgba.get_coordinates()
        curr_tuple = (pos["x"], pos["y"])
        if curr_tuple == target_tuple:
            return True
        print(f"Navigate attempt {attempt+1} failed, ended up at {curr_tuple}. Retrying pathing...")
    return False

step_limit = 200
steps = 0

# We want to find the exit at (5, 27)
exit_tile = (5, 27)
target_found = False

while queue and steps < step_limit:
    # Pop next tile to explore from
    curr_tuple = queue.pop(0)
    
    if curr_tuple == exit_tile:
        print("We found the exit tile in our queue!")
        target_found = True
        break
        
    # Navigate to the tile we are exploring from
    if not navigate_to(curr_tuple):
        print(f"Could not navigate to exploration node {curr_tuple}")
        continue
        
    print(f"Exploring from {curr_tuple}...")
    
    # Check all 4 directions
    for d, (dx, dy) in dirs.items():
        neighbor = (curr_tuple[0] + dx, curr_tuple[1] + dy)
        if neighbor in visited:
            # We already know this tile, but make sure the connection is in the graph
            # check if neighbor is already a connection
            already_connected = False
            for n, dir_n in walkable_graph.get(curr_tuple, []):
                if n == neighbor:
                    already_connected = True
                    break
            if not already_connected and neighbor in walkable_graph:
                # We can't assume it's connected unless we verify, but if it's already visited,
                # we can test stepping to it to verify the bidirectional link.
                pass
            continue
            
        # Try stepping into neighbor
        print(f"  Stepping {d} to test {neighbor}...")
        mgba.press_buttons([d])
        time.sleep(0.45)
        
        handle_any_menu_or_battle()
        pos_after = mgba.get_coordinates()
        pos_after_tuple = (pos_after["x"], pos_after["y"])
        
        if pos_after_tuple == neighbor:
            # WALKABLE!
            print(f"  Found walkable tile: {neighbor}")
            visited.add(neighbor)
            queue.append(neighbor)
            
            # Add to bidirectional graph
            if curr_tuple not in walkable_graph:
                walkable_graph[curr_tuple] = []
            if neighbor not in walkable_graph:
                walkable_graph[neighbor] = []
                
            walkable_graph[curr_tuple].append((neighbor, d))
            walkable_graph[neighbor].append((curr_tuple, rev_dirs[d]))
            
            # Step back
            mgba.press_buttons([rev_dirs[d]])
            time.sleep(0.45)
            handle_any_menu_or_battle()
        else:
            # BLOCKED
            # print(f"  Blocked at {neighbor}")
            pass
            
    steps += 1

print(f"Exploration finished. Visited {len(visited)} tiles.")
print("Walkable graph:")
for k, v in walkable_graph.items():
    print(f"  {k} -> {[x[0] for x in v]}")

if exit_tile in visited:
    print("EXIT IS REACHABLE!")
    print("Navigating to exit at (5, 27)...")
    if navigate_to(exit_tile):
        print("At exit! Stepping DOWN to exit...")
        mgba.press_buttons(["Down"])
        time.sleep(2.5)
        print("Final position after exit:", mgba.get_coordinates())
    else:
        print("Failed to navigate to exit tile!")
else:
    print("Exit at (5, 27) was NOT found reachable from starting position!")
    # Return to start for safety
    navigate_to(start_tuple)
