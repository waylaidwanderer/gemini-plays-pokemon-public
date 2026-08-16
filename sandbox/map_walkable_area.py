import mgba
import time

def escape_battle():
    print("Encountered a battle! Attempting to escape...")
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    mgba.press_buttons(["Down"])
    time.sleep(0.3)
    mgba.press_buttons(["Right"])
    time.sleep(0.3)
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.1)

def map_reachable():
    print("--- MAPPING REACHABLE AREA FROM (27, 21) ---")
    start = mgba.get_coordinates()
    if start is None:
        print("Could not get start coordinates.")
        return
        
    start_coords = (start['x'], start['y'])
    queue = [start_coords]
    parent_map = {start_coords: None}
    walkable = {start_coords}
    
    directions = ["Up", "Down", "Left", "Right"]
    back_dirs = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
    
    steps_count = 0
    max_steps = 90
    curr_loc = start_coords
    
    def navigate_physically(target):
        nonlocal curr_loc, steps_count
        if curr_loc == target:
            return True
        path = []
        node = target
        while node is not None:
            path.append(node)
            node = parent_map.get(node)
        path.reverse()
        
        for next_node in path[1:]:
            dx = next_node[0] - curr_loc[0]
            dy = next_node[1] - curr_loc[1]
            if dx == 1: d = "Right"
            elif dx == -1: d = "Left"
            elif dy == 1: d = "Down"
            else: d = "Up"
            
            mgba.press_buttons([d])
            time.sleep(0.42)
            steps_count += 1
            
            actual = mgba.get_coordinates()
            if actual is None:
                escape_battle()
                time.sleep(0.5)
                actual = mgba.get_coordinates()
                
            if actual is None or (actual['x'], actual['y']) != next_node:
                return False
            curr_loc = next_node
        return True

    while queue and steps_count < max_steps:
        node = queue.pop(0)
        if not navigate_physically(node):
            continue
            
        for d in directions:
            dx, dy = {"Up": (0, -1), "Down": (0, 1), "Left": (-1, 0), "Right": (1, 0)}[d]
            neighbor = (node[0] + dx, node[1] + dy)
            if neighbor in walkable:
                continue
                
            mgba.press_buttons([d])
            time.sleep(0.42)
            steps_count += 1
            
            actual = mgba.get_coordinates()
            if actual is None:
                escape_battle()
                time.sleep(0.5)
                actual = mgba.get_coordinates()
                
            if actual is not None:
                ax, ay = actual['x'], actual['y']
                if (ax, ay) != node:
                    # Successfully moved!
                    walkable.add((ax, ay))
                    parent_map[(ax, ay)] = node
                    queue.append((ax, ay))
                    
                    # Step back
                    mgba.press_buttons([back_dirs[d]])
                    time.sleep(0.42)
                    steps_count += 1
                    curr_loc = node
                    
    print("REACHABLE COORDS:")
    print(sorted(list(walkable)))

map_reachable()

