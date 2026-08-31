import mgba
import time
import json

def flee_battle():
    print("Wild battle! Fleeing...")
    # Advance the screen/text
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.3)
    # Select RUN
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    # Clear any "Got away safely!" text
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.3)

def walk_step(direction):
    pos = mgba.get_coordinates()
    x, y = pos['x'], pos['y']
    
    # Try to move
    mgba.press_buttons([direction])
    time.sleep(0.4)
    
    new_pos = mgba.get_coordinates()
    if new_pos == {'x': x, 'y': y}:
        # Check if we are in a battle
        # A simple test: press B several times and try again
        flee_battle()
        mgba.press_buttons([direction])
        time.sleep(0.4)
        new_pos = mgba.get_coordinates()
        
    return new_pos

def explore():
    # We start at our current position
    start_pos = mgba.get_coordinates()
    print("Start position:", start_pos)
    
    # Let's map out the walkable area around here.
    # Since we don't want to warp out by accident, we should be careful.
    # But if we do warp, we will print it and stop.
    
    visited = set()
    walkable = set()
    blocked = set()
    
    # Queue of coordinates to visit
    # Format: (x, y, path_to_get_there)
    queue = [(start_pos['x'], start_pos['y'], [])]
    walkable.add((start_pos['x'], start_pos['y']))
    
    max_steps = 100
    steps = 0
    
    # Let's do a simple DFS or grid exploration.
    # To keep it safe and avoid getting lost, we can use a backtrack-based path.
    # Or, we can just do a simple coordinate expansion by trying to step in directions and returning.
    # Let's try a simpler approach: walk in a local area and record coordinates.
    # Let's probe the grid from x in [15, 30], y in [0, 15].
    
    # Let's do a systematic backtracking exploration.
    current_path = []
    
    def go_to(target_path):
        # Reset to start if we are not at start?
        # Actually, if we just keep track of our current position and take relative steps:
        pass

    # Let's do a simpler exploration:
    # From current position, try to go Left as much as possible, then Up, Down, Right, and record the coordinates.
    # Let's write a simple randomized or deterministic local explorer.
    
    pos = mgba.get_coordinates()
    walkable.add((pos['x'], pos['y']))
    
    # Let's try to explore in 4 directions relative to current position.
    # Let's do a depth-limited search (depth 5) to see the local shape of B1F East.
    # This avoids going too far or getting warped.
    
    opponents = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
    
    def dls(depth, max_depth):
        if depth > max_depth:
            return
            
        pos = mgba.get_coordinates()
        cx, cy = pos['x'], pos['y']
        walkable.add((cx, cy))
        
        # Check if we warped
        # In B1F East, if we warp to 1F, the coordinates will be around (27, 11) or so.
        # Let's define the B1F East coordinate boundary: x should be >= 18 or so, and y should be small.
        # If we warp, coordinates will change. Let's check:
        # B1F East coordinates are like (26, 3).
        # If we are suddenly on another map, we stop.
        
        for dir_name in ["Left", "Right", "Up", "Down"]:
            # Predict next coordinate
            nx, ny = cx, cy
            if dir_name == "Left": nx -= 1
            elif dir_name == "Right": nx += 1
            elif dir_name == "Up": ny -= 1
            elif dir_name == "Down": ny += 1
            
            if (nx, ny) in blocked:
                continue
            if (nx, ny) in walkable and depth > 0:
                # We already know it's walkable, but let's not waste moves unless necessary
                # Actually, DLS needs to traverse to expand
                pass
                
            # Try to step
            new_pos = walk_step(dir_name)
            rx, ry = new_pos['x'], new_pos['y']
            
            if rx == cx and ry == cy:
                # Blocked!
                blocked.add((nx, ny))
                print(f"Blocked at: ({nx}, {ny})")
            else:
                # Moved successfully!
                if (rx, ry) != (nx, ny):
                    # Warped!
                    print(f"WARPED from ({cx}, {cy}) via {dir_name} to ({rx}, {ry})!")
                    # Go back if possible?
                    # Since we warped, we probably can't easily go back from inside the script.
                    # Let's just exit the script.
                    return True
                else:
                    walkable.add((rx, ry))
                    # Recurse
                    warped = dls(depth + 1, max_depth)
                    if warped:
                        return True
                    # Backtrack
                    walk_step(opponents[dir_name])
                    
        return False

    dls(0, 4)
    
    print("Walkable tiles mapped:")
    print(sorted(list(walkable)))
    print("Blocked tiles mapped:")
    print(sorted(list(blocked)))

explore()
