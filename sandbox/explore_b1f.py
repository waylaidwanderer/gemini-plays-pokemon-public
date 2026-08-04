import mgba, time

def handle_battle_or_dismiss():
    # If battle text or text box appears, run away or dismiss
    # Try pressing B, Right, Down, A to run from wild battle
    mgba.press_buttons(["B", "Right", "Down", "A"])
    time.sleep(0.1)

def explore_bfs():
    start = mgba.get_coordinates()
    print(f"Starting BFS exploration from {start}...")
    
    # We want to find a path from current position to Y <= 16 (Row 16 Highway)
    # Let's keep track of visited coordinates
    visited = set()
    visited.add((start['x'], start['y']))
    
    # We can perform a local grid search
    queue = [start]
    
    # Directions: Up, Down, Left, Right
    moves = [("Up", 0, -1), ("Down", 0, 1), ("Left", -1, 0), ("Right", 1, 0)]
    
    # Since we physically move the player, let's trace paths from start
    # To keep script within button limits, let's explore up to 60 moves
    
    for iteration in range(60):
        cur = mgba.get_coordinates()
        print(f"Iter {iteration}: Current pos {cur}")
        
        if cur['y'] <= 16:
            print(f"SUCCESS! Reached Row 16 Highway at {cur}!")
            return True
            
        # Try moving Up first if possible
        moved = False
        for dir_name, dx, dy in [("Up", 0, -1), ("Right", 1, 0), ("Left", -1, 0), ("Down", 0, 1)]:
            target = (cur['x'] + dx, cur['y'] + dy)
            if target not in visited:
                print(f"  Attempting move {dir_name} to {target}...")
                mgba.press_buttons([dir_name])
                time.sleep(0.05)
                new_pos = mgba.get_coordinates()
                if new_pos != cur:
                    print(f"  Moved to {new_pos}")
                    visited.add((new_pos['x'], new_pos['y']))
                    moved = True
                    break
                else:
                    print(f"  Blocked at {target}")
                    visited.add(target) # Mark wall/blocked
                    
        if not moved:
            # Backtrack or try another direction
            print("  No unvisited step available directly, trying random move...")
            mgba.press_buttons(["Right", "Up", "Left", "Down"][iteration % 4])
            time.sleep(0.05)

explore_bfs()
