import mgba
import time

# Robust coordinate reader that filters out transient states
def get_stable_coords():
    pos1 = mgba.get_coordinates()
    time.sleep(0.15)
    pos2 = mgba.get_coordinates()
    while pos1 != pos2:
        pos1 = pos2
        time.sleep(0.15)
        pos2 = mgba.get_coordinates()
    return pos1

start_pos = get_stable_coords()
print(f"Starting exploration from: {start_pos}")

# We treat (3, 7) as the exit warp, so we do not walk back onto it.
exit_tile = (3, 7)

# BFS queue and structures
# Each item in queue is (x, y)
queue = [(start_pos['x'], start_pos['y'])]
visited = set()
visited.add((start_pos['x'], start_pos['y']))

# Parent map to reconstruct paths
parent = {}

def get_path_to(target):
    path = []
    curr = target
    while curr in parent:
        path.append(curr)
        curr = parent[curr]
    path.reverse()
    return path

# To navigate from current position to a target tile
def navigate_to(target):
    curr = get_stable_coords()
    curr_tup = (curr['x'], curr['y'])
    if curr_tup == target:
        return True
        
    path = get_path_to(target)
    if not path:
        return False
        
    for node in path:
        pos = get_stable_coords()
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
            time.sleep(0.55) # robust delay
            new_pos = get_stable_coords()
            if (new_pos['x'], new_pos['y']) != node:
                # Blocked or deviated
                return False
    return True

walkable = set()
walkable.add((start_pos['x'], start_pos['y']))

# Let's perform a simple coordinate check in 4 directions around current position
# Instead of a full recursive DFS which can get lost, we will use a BFS
# that returns to a known walkable node to explore its neighbors.

print("Starting BFS...")
limit = 150 # safety step limit
steps = 0

while queue and steps < limit:
    curr_node = queue.pop(0)
    
    # Walk to curr_node to explore its neighbors
    if not navigate_to(curr_node):
        print(f"Failed to navigate to {curr_node}, skipping.")
        continue
        
    # Test all 4 directions
    for direction, (dx, dy, btn, rev_btn) in {
        "Up": (0, -1, "Up", "Down"),
        "Down": (0, 1, "Down", "Up"),
        "Left": (-1, 0, "Left", "Right"),
        "Right": (1, 0, "Right", "Left")
    }.items():
        nx, ny = curr_node[0] + dx, curr_node[1] + dy
        
        if (nx, ny) == exit_tile:
            continue # do not step on exit tile!
            
        if (nx, ny) in visited:
            continue
            
        # Try to step onto neighbor
        steps += 1
        pos_before = get_stable_coords()
        mgba.press_buttons([btn])
        time.sleep(0.55) # robust delay
        pos_after = get_stable_coords()
        
        if (pos_after['x'], pos_after['y']) == (nx, ny):
            # Success! Walkable
            walkable.add((nx, ny))
            visited.add((nx, ny))
            parent[(nx, ny)] = curr_node
            queue.append((nx, ny))
            
            # Step back
            mgba.press_buttons([rev_btn])
            time.sleep(0.55)
            get_stable_coords()
        elif (pos_after['x'], pos_after['y']) == (pos_before['x'], pos_before['y']):
            # Blocked (wall/obstacle)
            visited.add((nx, ny))
        else:
            # Warped!
            print(f"WARP DETECTED when going {direction} from {curr_node} to {pos_after}")
            # Step back
            mgba.press_buttons([rev_btn])
            time.sleep(1.2) # wait for warp transition
            get_stable_coords()
            visited.add((nx, ny))

print("=== EXPLORATION COMPLETED ===")
print("Walkable tiles:")
print(sorted(list(walkable)))

# Take final screenshot
scr = mgba.take_screenshot()
print(f"Screenshot saved at: {scr}")
