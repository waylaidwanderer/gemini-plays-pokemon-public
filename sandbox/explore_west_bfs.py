import mgba
import time

def run():
    print("--- AUTOMATIC PATHFINDER TO WEST FUCHSIA ---")
    
    start_pos = mgba.get_coordinates()
    print("Start position:", start_pos)
    
    # We want to find a path from start_pos to any position with x <= 13.
    # We will use DFS with backtracking.
    # path is a list of button presses from start_pos.
    # visited is a set of (x, y) coordinates.
    visited = { (start_pos['x'], start_pos['y']) }
    
    directions = [
        ("Left", "Right", -1, 0),
        ("Up", "Down", 0, -1),
        ("Down", "Up", 0, 1),
        ("Right", "Left", 1, 0)
    ]
    
    solution_path = []
    
    def dfs(x, y, path_so_far):
        if x <= 13:
            print(f"FOUND PATH TO x={x}, y={y}!")
            print("Path length:", len(path_so_far))
            print("Path:", path_so_far)
            solution_path.extend(path_so_far)
            return True
            
        for move, reverse_move, dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (nx, ny) in visited:
                continue
                
            # Try to make the move
            mgba.press_buttons([move])
            time.sleep(0.25)
            curr = mgba.get_coordinates()
            
            if curr['x'] == nx and curr['y'] == ny:
                # Successfully moved!
                visited.add((nx, ny))
                if dfs(nx, ny, path_so_far + [move]):
                    return True
                # Backtrack
                mgba.press_buttons([reverse_move])
                time.sleep(0.25)
            else:
                # Blocked, so mark as visited to avoid trying again
                visited.add((nx, ny))
                
        return False

    # Run DFS
    dfs(start_pos['x'], start_pos['y'], [])
    
    # If a path was found, solution_path will contain the sequence.
    # Since we backtracked all the way to start_pos, let's now execute the solution_path!
    if solution_path:
        print("Executing solution path...")
        # Since the DFS already returned us to the start, we can just execute the moves!
        # But wait! Did the DFS backtrack to the start?
        # Yes, because if dfs returns True, it propagates up, but wait:
        # If dfs returns True, it does NOT execute the backtracks on the recursion stack!
        # So the player is currently standing at the destination!
        print("Player should already be at the destination. Verified position:", mgba.get_coordinates())
        mgba.take_screenshot()
    else:
        print("No path found.")

if __name__ == "__main__":
    run()
