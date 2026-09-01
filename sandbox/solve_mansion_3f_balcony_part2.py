import mgba
import time

def escape_battle():
    print("Dismissing first screen text...")
    mgba.press_buttons(["B"])
    time.sleep(1.0)

    print("Dismissing second screen text...")
    mgba.press_buttons(["B"])
    time.sleep(3.0) # wait for SHELLBY send-out animation

    print("Selecting RUN...")
    mgba.press_buttons(["Down"])
    time.sleep(0.3)
    mgba.press_buttons(["Right"])
    time.sleep(0.3)
    mgba.press_buttons(["A"])
    time.sleep(2.5) # wait for escape text

    print("Dismissing escape text...")
    mgba.press_buttons(["B"])
    time.sleep(1.5)

def step(direction):
    current = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.5)
    next_pos = mgba.get_coordinates()
    if next_pos == current:
        print(f"Blocked at {current}. Attempting battle escape...")
        escape_battle()
        time.sleep(2.0)
        mgba.press_buttons([direction])
        time.sleep(0.5)
        next_pos = mgba.get_coordinates()
    return next_pos

def walk_route(route_coords):
    i = 0
    while i < len(route_coords):
        target = route_coords[i]
        curr = mgba.get_coordinates()
        if curr == target:
            i += 1
            continue
        
        dx = target['x'] - curr['x']
        dy = target['y'] - curr['y']
        
        if abs(dx) + abs(dy) == 1:
            if dx == 1: direction = "Right"
            elif dx == -1: direction = "Left"
            elif dy == 1: direction = "Down"
            elif dy == -1: direction = "Up"
            
            res = step(direction)
            if res == target:
                print(f"Reached {target}")
                i += 1
            else:
                print(f"Failed to reach target {target}. Position: {res}. Retrying...")
        else:
            # We are displaced
            print(f"Displaced! Current: {curr}, Target: {target}. Attempting recovery...")
            found = False
            for idx, coord in enumerate(route_coords):
                if coord == curr:
                    print(f"Found current position {curr} in route at index {idx}. Resuming from there.")
                    i = idx + 1
                    found = True
                    break
            if not found:
                # Find any adjacent route tile
                best_idx = -1
                best_dist = 999999
                for idx, coord in enumerate(route_coords):
                    dist = abs(coord['x'] - curr['x']) + abs(coord['y'] - curr['y'])
                    if dist == 1:
                        idx_diff = abs(idx - i)
                        if idx_diff < best_dist:
                            best_dist = idx_diff
                            best_idx = idx
                
                if best_idx != -1:
                    target_coord = route_coords[best_idx]
                    pdx = target_coord['x'] - curr['x']
                    pdy = target_coord['y'] - curr['y']
                    print(f"Found adjacent route tile {target_coord} (index {best_idx}). Walking to it...")
                    if pdx == 1: pdir = "Right"
                    elif pdx == -1: pdir = "Left"
                    elif pdy == 1: pdir = "Down"
                    elif pdy == -1: pdir = "Up"
                    res = step(pdir)
                    if res == target_coord:
                        i = best_idx + 1
                        continue
                
                print("Could not find adjacent route tile for recovery.")
                return False
    return True

# 1. Walk from current position (21, 4) to (12, 6) via Row 6
route_to_col12 = [
    {'x': 20, 'y': 4},
    {'x': 20, 'y': 5},
    {'x': 20, 'y': 6},
    # Left along Row 6
    {'x': 19, 'y': 6},
    {'x': 18, 'y': 6},
    {'x': 17, 'y': 6},
    {'x': 16, 'y': 6},
    {'x': 15, 'y': 6},
    {'x': 14, 'y': 6},
    {'x': 13, 'y': 6},
    {'x': 12, 'y': 6}
]

print("1. Walking to Column 12 Row 6...")
if not walk_route(route_to_col12):
    print("Failed to reach Column 12 Row 6.")
    mgba.take_screenshot()
    exit(1)

# 2. Try walking Column 12 to Row 16
col12_to_row16 = [
    {'x': 12, 'y': 7},
    {'x': 12, 'y': 8},
    {'x': 12, 'y': 9},
    {'x': 12, 'y': 10},
    {'x': 12, 'y': 11},
    {'x': 12, 'y': 12},
    {'x': 12, 'y': 13},
    {'x': 12, 'y': 14},
    {'x': 12, 'y': 15},
    {'x': 12, 'y': 16}
]

print("2. Attempting Column 12 path to Row 16...")
col12_success = walk_route(col12_to_row16)

if col12_success:
    print("Column 12 path succeeded! Walking to balcony...")
    route_to_balcony = [
        {'x': 13, 'y': 16},
        {'x': 14, 'y': 16},
        {'x': 15, 'y': 16},
        {'x': 16, 'y': 16},
        {'x': 17, 'y': 16},
        {'x': 18, 'y': 16},
        {'x': 19, 'y': 16},
        {'x': 20, 'y': 16},
        {'x': 21, 'y': 16},
        # Down past open gate to Row 18
        {'x': 21, 'y': 17},
        {'x': 21, 'y': 18},
        # Left along Row 18 to Column 19
        {'x': 20, 'y': 18},
        {'x': 19, 'y': 18}
    ]
else:
    print("Column 12 path blocked. Walking back UP to Row 6 to try Column 17 path...")
    # Walk back up to Row 6 (recovery from whichever point on Column 12 we reached)
    # The simplest is to use coordinates based on current position
    curr = mgba.get_coordinates()
    y_pos = curr['y']
    recovery_up = []
    for y in range(y_pos - 1, 5, -1):
        recovery_up.append({'x': 12, 'y': y})
    walk_route(recovery_up)
    
    # Walk to Column 17 Row 6
    print("Walking to Column 17 Row 6...")
    route_to_col17 = [
        {'x': 13, 'y': 6},
        {'x': 14, 'y': 6},
        {'x': 15, 'y': 6},
        {'x': 16, 'y': 6},
        {'x': 17, 'y': 6}
    ]
    walk_route(route_to_col17)
    
    # Try Column 17 path
    print("Attempting Column 17 path to Row 16...")
    col17_to_row16 = [
        {'x': 17, 'y': 7},
        {'x': 17, 'y': 8},
        {'x': 17, 'y': 9},
        {'x': 17, 'y': 10},
        {'x': 17, 'y': 11},
        {'x': 17, 'y': 12},
        {'x': 17, 'y': 13},
        {'x': 17, 'y': 14},
        {'x': 17, 'y': 15},
        {'x': 17, 'y': 16}
    ]
    if walk_route(col17_to_row16):
        print("Column 17 path succeeded! Walking to balcony...")
        route_to_balcony = [
            {'x': 18, 'y': 16},
            {'x': 19, 'y': 16},
            {'x': 20, 'y': 16},
            {'x': 21, 'y': 16},
            # Down past open gate to Row 18
            {'x': 21, 'y': 17},
            {'x': 21, 'y': 18},
            # Left along Row 18 to Column 19
            {'x': 20, 'y': 18},
            {'x': 19, 'y': 18}
        ]
    else:
        print("Fatal: Column 17 path also blocked!")
        mgba.take_screenshot()
        exit(1)

# Walk from Row 16 to balcony
if walk_route(route_to_balcony):
    print("Successfully reached the balcony drop tile (19, 18)!")
    print("Performing balcony drop step...")
    # Step down to drop
    mgba.press_buttons(["Down"])
    time.sleep(3.0) # wait generously for drop transition and fade-in
    print("Final coordinates after drop:", mgba.get_coordinates())
    mgba.take_screenshot()
else:
    print("Failed to navigate to balcony.")
    mgba.take_screenshot()
