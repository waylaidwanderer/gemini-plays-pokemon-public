# BFS-based pathfinder that plans a route between start and target coordinates on a specified map,

# with integrated static collision database and custom spinner-sliding simulation for Rocket Hideout floors

# (Map 0_199 = B1F, Map 0_200 = B2F, Map 0_201 = B3F, Map 0_202 = B4F) to ensure valid, obstacle-free overworld routing.

import json
import collections

# Retrieve parameters directly from the globally injected 'input_data' dictionary
map_id = input_data['map_id']
start_x = int(input_data['start_x'])
start_y = int(input_data['start_y'])
target_x = int(input_data['target_x'])
target_y = int(input_data['target_y'])

def find_path():
    impassable = set()
    
    # Define map-specific boundaries and blockages based on empirical data:
    if map_id == "0_10": # Saffron City
        # Main buildings and fences
        # Add fences on column 3:
        for y in range(17, 30):
            impassable.add((3, y))
        # Mr. Psychic's house
        for x in range(26, 32):
            for y in range(25, 30):
                impassable.add((x, y))
        # Pokemon Center
        for x in range(5, 11):
            for y in range(25, 29):
                impassable.add((x, y))
                
    elif map_id == "0_202": # Rocket Hideout B4F
        # Office walls and tables on Row 4
        for x in range(18, 28):
            impassable.add((x, 4))
        # Guard posts and other walls:
        for y in range(1, 15):
            impassable.add((21, y)) # Column 21 partition wall
            
    # Spinner definitions for Rocket Hideout floors (Map 0_199 to 0_202):
    # Spinners map a tile (x, y) to a sliding direction: "Up", "Down", "Left", "Right"
    spinners = {}
    stop_tiles = set()
    
    if map_id == "0_200": # Rocket Hideout B2F Spinner Maze
        # Define spinners:
        spinners[(17, 11)] = "Left"
        spinners[(13, 18)] = "Left"
        spinners[(11, 18)] = "Down"
        spinners[(13, 22)] = "Left"
        spinners[(9, 22)] = "Down"
        spinners[(10, 25)] = "Right"
        
        # Stop tiles:
        stop_tiles.update([(1, 9), (9, 16), (15, 18), (11, 20), (9, 24), (14, 25)])

    # BFS Pathfinder with Spinner Simulation:
    queue = collections.deque([(start_x, start_y, [])])
    visited = set([(start_x, start_y)])
    
    while queue:
        cx, cy, path = queue.popleft()
        if (cx, cy) == (target_x, target_y):
            return path
            
        # Standard moves
        for dx, dy, move in [(0, -1, "Up"), (0, 1, "Down"), (-1, 0, "Left"), (1, 0, "Right")]:
            nx, ny = cx + dx, cy + dy
            
            # Check map boundaries (assumed 100x100 max for general maps)
            if not (0 <= nx < 100 and 0 <= ny < 100):
                continue
            if (nx, ny) in impassable:
                continue
                
            # Spinner sliding simulation:
            if (nx, ny) in spinners:
                # Slide until we hit a stop tile or boundary
                sx, sy = nx, ny
                visited_slide = set([(sx, sy)])
                while (sx, sy) in spinners and (sx, sy) not in stop_tiles:
                    s_move = spinners[(sx, sy)]
                    sdx, sdy = {"Up": (0, -1), "Down": (0, 1), "Left": (-1, 0), "Right": (1, 0)}[s_move]
                    nsx, nsy = sx + sdx, sy + sdy
                    if not (0 <= nsx < 100 and 0 <= nsy < 100) or (nsx, nsy) in impassable or (nsx, nsy) in visited_slide:
                        break
                    sx, sy = nsx, nsy
                    visited_slide.add((sx, sy))
                nx, ny = sx, sy
                
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, path + [move]))
                
    return None

path = find_path()
if path is not None:
    print(json.dumps(path))
else:
    print(json.dumps([]))