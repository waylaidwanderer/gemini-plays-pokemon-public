import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def press_and_wait(btn):
    mgba.press_buttons([btn])
    time.sleep(0.35) # 350ms to be 100% sure the emulator advances and settles
    return get_pos()

# Let's perform a complete overworld DFS to discover every walkable tile in this map
# starting from our current position.
start = get_pos()
print(f"Starting complete DFS mapping from {start}...")

walkable = set()
walkable.add(start)

directions = {
    "Left": (-1, 0),
    "Right": (1, 0),
    "Up": (0, -1),
    "Down": (0, 1)
}

opposites = {
    "Left": "Right",
    "Right": "Left",
    "Up": "Down",
    "Down": "Up"
}

# We will keep a stack of (current_node, direction_index) to do DFS without recursion limits
stack = [(start, 0, [])] # (pos, dir_idx, path_to_here)

# To be safe, we will just find all neighbors first, then move, explore, and backtrack.
# Since the map is small, DFS is very quick.

visited_states = set()
visited_states.add(start)

def run_dfs(curr):
    for d, (dx, dy) in directions.items():
        nxt = (curr[0] + dx, curr[1] + dy)
        if nxt in visited_states:
            continue
        
        pos = press_and_wait(d)
        if pos != curr:
            # We successfully moved to a new tile!
            visited_states.add(pos)
            print(f"Discovered: {pos}")
            
            # Check if this tile triggers a map warp!
            # If our coordinate changed drastically or to another map,
            # we will notice and we shouldn't backtrack blindly.
            if abs(pos[0] - curr[0]) > 1 or abs(pos[1] - curr[1]) > 1:
                print(f"WARPED! Current position: {pos}")
                # We warped out of the map! Exit script immediately.
                return True
            
            # Recursively explore from the new tile
            warped = run_dfs(pos)
            if warped:
                return True
            
            # Backtrack to curr
            press_and_wait(opposites[d])
        else:
            # Blocked, so it's a wall or solid object
            pass
    return False

run_dfs(start)
print("DFS complete. Walkable tiles found:")
print(sorted(list(visited_states)))
