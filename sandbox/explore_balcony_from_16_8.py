import mgba
import time

def run_from_battle():
    print("In battle! Attempting to run...")
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 100"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 500"])
    for _ in range(4):
        mgba.press_buttons(["B", "sleep 100"])

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction, "sleep 150"])
    pos_after = mgba.get_coordinates()
    if pos_before == pos_after:
        mgba.press_buttons([direction, "sleep 150"])
        pos_after = mgba.get_coordinates()
        attempts = 0
        while pos_before == pos_after and attempts < 5:
            run_from_battle()
            mgba.press_buttons([direction, "sleep 150"])
            pos_after = mgba.get_coordinates()
            attempts += 1
    return pos_after

# We are at (16, 8). Let's do a BFS to find any path to Row 18!
# Since we want to find a path, we can keep track of paths from the start.
start_pos = (16, 8)
queue = [[start_pos]]
visited = {start_pos}

directions = {
    "Up": (0, -1),
    "Down": (0, 1),
    "Left": (-1, 0),
    "Right": (1, 0)
}
opposite = {
    "Up": "Down",
    "Down": "Up",
    "Left": "Right",
    "Right": "Left"
}

print("Starting BFS to find a path to the Balcony (Row 18)...")
found_path = None

# To do BFS on the emulator, we can't warp instantly, we must physically walk.
# A safe way is to walk the current path, test 4 directions, and backtrack.
# Since DFS with backtracking is easier to implement for physical traversal on foot, let's use DFS!

walkable_paths = []
def dfs(path):
    global found_path
    curr = path[-1]
    if curr[1] >= 18:
        print(f"FOUND BALCONY PATH: {path}")
        found_path = path
        return True
        
    for move, (dx, dy) in directions.items():
        nxt = (curr[0] + dx, curr[1] + dy)
        if nxt not in visited:
            visited.add(nxt)
            # Try to step
            pos_before = mgba.get_coordinates()
            pos_after = walk_step(move)
            if pos_before != pos_after:
                actual_nxt = (pos_after['x'], pos_after['y'])
                visited.add(actual_nxt)
                new_path = path + [actual_nxt]
                if dfs(new_path):
                    return True
                # Backtrack
                walk_step(opposite[move])
    return False

dfs([start_pos])

if found_path is not None:
    print("SUCCESS: Found path to balcony!")
else:
    print("Failed to find any path to Row 18 using DFS.")
    print("Visited tiles:", sorted(list(visited)))
