import mgba
import time

def run_from_battle():
    # Run from wild battles
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 100"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 500"])
    for _ in range(4):
        mgba.press_buttons(["B", "sleep 100"])

def try_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction, "sleep 150"])
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        # Check if we turned or if we are in battle
        mgba.press_buttons([direction, "sleep 150"])
        pos_after = mgba.get_coordinates()
        
        attempts = 0
        while pos_before == pos_after and attempts < 5:
            run_from_battle()
            mgba.press_buttons([direction, "sleep 150"])
            pos_after = mgba.get_coordinates()
            attempts += 1
            
    return pos_before != pos_after, pos_after

visited = set()
walkable = set()
to_explore = [(12, 9)]

# BFS/DFS mapper
def map_3f_east():
    start_pos = mgba.get_coordinates()
    visited.add((start_pos['x'], start_pos['y']))
    walkable.add((start_pos['x'], start_pos['y']))
    
    print(f"Starting map from: {start_pos}")
    
    # We will do a simple exploration.
    # From current tile, try moving in 4 directions. If successful, record the tile, and return back.
    # This keeps us localized and doesn't get us lost.
    
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
    
    # DFS recursion with backtracking
    def dfs(x, y):
        for move, (dx, dy) in directions.items():
            tx, ty = x + dx, y + dy
            if (tx, ty) not in visited:
                visited.add((tx, ty))
                success, pos_after = try_step(move)
                if success:
                    # We successfully stepped to tx, ty!
                    nx, ny = pos_after['x'], pos_after['y']
                    walkable.add((nx, ny))
                    print(f"WALKABLE: ({nx}, {ny})")
                    dfs(nx, ny)
                    # Backtrack
                    try_step(opposite[move])
                else:
                    # Blocked
                    pass

    dfs(start_pos['x'], start_pos['y'])
    print("Walkable tiles mapped on 3F East:")
    print(sorted(list(walkable)))

map_3f_east()
