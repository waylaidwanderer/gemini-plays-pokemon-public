import mgba
import time

def flood_fill():
    print("Running programmatic flood fill to map the entire room...")
    # Initialize start position
    start = mgba.get_coordinates()
    visited = { (start['x'], start['y']) }
    queue = [ start ]
    
    # Directions
    dirs = {
        "Up": (0, -1),
        "Down": (0, 1),
        "Left": (-1, 0),
        "Right": (1, 0)
    }
    
    # To restore position, we will keep track of movements
    # But wait, flood fill on emulator:
    # Since we can only move the character, we can explore step-by-step
    # Let's do a simple DFS with backtracking.
    walkable = set()
    walkable.add((start['x'], start['y']))
    
    def dfs(cx, cy):
        for d, (dx, dy) in dirs.items():
            nx, ny = cx + dx, cy + dy
            if (nx, ny) not in walkable:
                # Try to move
                mgba.press_buttons([d])
                time.sleep(0.3) # wait for movement
                pos = mgba.get_coordinates()
                if pos['x'] == nx and pos['y'] == ny:
                    # Successfully moved!
                    walkable.add((nx, ny))
                    dfs(nx, ny)
                    # Backtrack
                    opp = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}[d]
                    mgba.press_buttons([opp])
                    time.sleep(0.3)
                else:
                    # Blocked (or ran into a battle, which we should escape)
                    # If position changed but not to (nx, ny), we might be in a battle
                    # Let's check if we are in a battle by seeing if position is different or same
                    # If it's same, it's just a wall.
                    pass
                    
    dfs(start['x'], start['y'])
    print("FINISHED DFS!")
    print("All walkable tiles in this room:")
    for x, y in sorted(list(walkable)):
        print(f"({x}, {y})")
        
    mgba.take_screenshot()

if __name__ == "__main__":
    flood_fill()
