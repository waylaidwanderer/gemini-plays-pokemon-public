import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def step(direction):
    mgba.press_buttons([direction])
    time.sleep(0.2)
    return get_pos()

# Let's map out the walkable coordinates starting from the current position
# We'll use a simple BFS that only moves to verified safe tiles.
# To prevent spinning out of control, if a step moves us by more than 1 tile,
# we treat it as a spin tile (hazard) and backtrack if possible, or log it.

start_pos = get_pos()
print(f"Starting exploration from {start_pos}")

walkable = set([start_pos])
blocked = set()
spin_tiles = set()
parent = {}

# Directions mapping
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

# Let's do a safe BFS. We keep track of our path to backtrack.
# Since we are physically moving the character, we must backtrack step-by-step.
path_to_current = []

def navigate_to(target_path):
    # Reset to start pos by reverse of path_to_current, then go to target_path
    global path_to_current
    # Backtrack to start
    for d in reversed(path_to_current):
        step(rev_dirs[d])
    path_to_current = []
    # Move to target
    for d in target_path:
        step(d)
        path_to_current.append(d)

queue = [([], start_pos)]
visited_nodes = {start_pos}

while queue:
    curr_path, curr_pos = queue.pop(0)
    navigate_to(curr_path)
    
    # Try all 4 directions from curr_pos
    for d, (dx, dy) in dirs.items():
        neighbor = (curr_pos[0] + dx, curr_pos[1] + dy)
        if neighbor in visited_nodes or neighbor in blocked or neighbor in spin_tiles:
            continue
            
        # Try to step
        new_pos = step(d)
        if new_pos == curr_pos:
            # Blocked
            blocked.add(neighbor)
            print(f"Blocked at {neighbor} going {d}")
        else:
            # Check if we spun (moved more than 1 tile)
            dist = abs(new_pos[0] - curr_pos[0]) + abs(new_pos[1] - curr_pos[1])
            if dist > 1:
                # We spun! This is a spin tile.
                spin_tiles.add(neighbor)
                print(f"SPIN TILE detected at {neighbor}! Spun to {new_pos}")
                # We must recover by navigating back to start, then back to curr_path
                # But wait, we don't know the path back from the spin end-point easily,
                # so let's just use the spin end-point's position.
                # Actually, to be safe, we can reset path_to_current since we are lost.
                # Let's find our current position.
                lost_pos = get_pos()
                print(f"Recovering from spin... current pos is {lost_pos}")
                # Since we spun, let's just reset our navigation state.
                path_to_current = []
                # To be absolutely sure we are at start_pos, let's just run back or let the script end/warn.
                # If we are not at start_pos, we can try to walk back to start_pos if we know a path,
                # but for simplicity, let's just stop exploration on spin to prevent getting stuck.
                print("Stopping exploration to prevent desync after spin.")
                queue = []
                break
            else:
                # Normal walkable tile!
                visited_nodes.add(neighbor)
                walkable.add(neighbor)
                print(f"Walkable: {neighbor}")
                # Step back
                back_pos = step(rev_dirs[d])
                if back_pos != curr_pos:
                    print(f"WARNING: Backtrack desync! Expected {curr_pos}, got {back_pos}")
                    # Reset path
                    path_to_current = []
                    queue = []
                    break
                queue.append((curr_path + [d], neighbor))

# Return to start at the end
navigate_to([])
print("\nExploration Complete!")
print(f"Walkable tiles: {sorted(list(walkable))}")
print(f"Blocked tiles: {sorted(list(blocked))}")
print(f"Spin tiles: {sorted(list(spin_tiles))}")
