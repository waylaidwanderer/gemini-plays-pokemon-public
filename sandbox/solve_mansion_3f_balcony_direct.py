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

# 1. Walk from (25, 5) on 2F East to 2F West switch (2, 6)
route_to_switch = [
    # Walk UP to Row 3
    {'x': 25, 'y': 4},
    {'x': 25, 'y': 3},
    # Walk LEFT along Row 3 to Column 12
    {'x': 24, 'y': 3},
    {'x': 23, 'y': 3},
    {'x': 22, 'y': 3},
    {'x': 21, 'y': 3},
    {'x': 20, 'y': 3},
    {'x': 19, 'y': 3},
    {'x': 18, 'y': 3},
    {'x': 17, 'y': 3},
    {'x': 16, 'y': 3},
    {'x': 15, 'y': 3},
    {'x': 14, 'y': 3},
    {'x': 13, 'y': 3},
    {'x': 12, 'y': 3},
    # Walk DOWN Column 12 to Row 11
    {'x': 12, 'y': 4},
    {'x': 12, 'y': 5},
    {'x': 12, 'y': 6},
    {'x': 12, 'y': 7},
    {'x': 12, 'y': 8},
    {'x': 12, 'y': 9},
    {'x': 12, 'y': 10},
    {'x': 12, 'y': 11},
    # Walk LEFT along Row 11 to 2F West
    {'x': 11, 'y': 11},
    {'x': 10, 'y': 11},
    {'x': 9, 'y': 11},
    {'x': 8, 'y': 11},
    {'x': 7, 'y': 11},
    {'x': 6, 'y': 11},
    {'x': 5, 'y': 11},
    {'x': 4, 'y': 11},
    {'x': 3, 'y': 11},
    {'x': 2, 'y': 11},
    # Walk UP Column 2 to Row 6 (stand at 2, 6 facing UP to switch at 2, 5)
    {'x': 2, 'y': 10},
    {'x': 2, 'y': 8}, # wait, Row 9 has wall panel on Cols 1-7 in both states!
    # Ah! Let's bypass Column 2 Row 9 by walking Column 8/10
]

# Let's fix route_to_switch to bypass Column 2 Row 9 wall panel!
# Row 9 is blocked on Cols 1-7. So on 2F West, Row 9 Column 2 is blocked.
# To bypass, we walk LEFT along Row 11 to Column 8, walk UP Column 8 to Row 8, and walk LEFT to Column 2!
route_to_switch_v2 = [
    # Walk UP to Row 3
    {'x': 25, 'y': 4},
    {'x': 25, 'y': 3},
    # Walk LEFT along Row 3 to Column 12
    {'x': 24, 'y': 3},
    {'x': 23, 'y': 3},
    {'x': 22, 'y': 3},
    {'x': 21, 'y': 3},
    {'x': 20, 'y': 3},
    {'x': 19, 'y': 3},
    {'x': 18, 'y': 3},
    {'x': 17, 'y': 3},
    {'x': 16, 'y': 3},
    {'x': 15, 'y': 3},
    {'x': 14, 'y': 3},
    {'x': 13, 'y': 3},
    {'x': 12, 'y': 3},
    # Walk DOWN Column 12 to Row 11
    {'x': 12, 'y': 4},
    {'x': 12, 'y': 5},
    {'x': 12, 'y': 6},
    {'x': 12, 'y': 7},
    {'x': 12, 'y': 8},
    {'x': 12, 'y': 9},
    {'x': 12, 'y': 10},
    {'x': 12, 'y': 11},
    # Walk LEFT along Row 11 to Column 8
    {'x': 11, 'y': 11},
    {'x': 10, 'y': 11},
    {'x': 9, 'y': 11},
    {'x': 8, 'y': 11},
    # Walk UP Column 8 to Row 8
    {'x': 8, 'y': 10},
    {'x': 8, 'y': 9}, # wait! Row 9 Columns 8-11 are NOT blocked? Yes, Row 9 has wall panel on Cols 1-7. So Col 8 Row 9 is OPEN!
    {'x': 8, 'y': 8},
    # Walk LEFT along Row 8 to Column 2
    {'x': 7, 'y': 8},
    {'x': 6, 'y': 8},
    {'x': 5, 'y': 8},
    {'x': 4, 'y': 8},
    {'x': 3, 'y': 8},
    {'x': 2, 'y': 8},
    # Walk UP Column 2 to Row 6 (facing UP to switch at 2, 5)
    {'x': 2, 'y': 7},
    {'x': 2, 'y': 6}
]

print("Walking State B route to 2F West switch from (25, 5)...")
print("Current position:", mgba.get_coordinates())

if walk_route(route_to_switch_v2):
    print("Reached (2, 6). Toggling Mewtwo switch...")
    # Stand at (2, 6) facing UP and interact with switch at (2, 5)
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    for i in range(4):
        print(f"Pressing A ({i+1}/4)...")
        mgba.press_buttons(["A"])
        time.sleep(1.5)
    
    print("Switch toggled. Walking State A route to stairs (5, 10)...")
    # State A route to the stairs at (5, 10) starting from (2, 6)
    route_to_stairs = [
        {'x': 2, 'y': 7},
        {'x': 2, 'y': 8},
        {'x': 3, 'y': 8},
        {'x': 4, 'y': 8},
        {'x': 5, 'y': 8},
        {'x': 5, 'y': 9},
        {'x': 5, 'y': 10} # stairs warp tile UP to 3F West
    ]
    
    if walk_route(route_to_stairs):
        print("Successfully reached stairs warp (5, 10)!")
        print("Taking stairs...")
        # Step DOWN onto stairs warp
        mgba.press_buttons(["Down"])
        time.sleep(3.0) # wait for warp transition to 3F West
        print("Coordinates on 3F West:", mgba.get_coordinates())
        
        # State A route on 3F West to the balcony on 3F East
        route_on_3f = [
            # Walk UP Column 5 to Row 2
            {'x': 5, 'y': 10},
            {'x': 5, 'y': 9},
            {'x': 5, 'y': 8},
            {'x': 5, 'y': 7},
            {'x': 5, 'y': 6},
            {'x': 5, 'y': 5},
            {'x': 5, 'y': 4},
            {'x': 5, 'y': 3},
            {'x': 5, 'y': 2},
            # Walk RIGHT along Row 2 past Column 22 to Column 21
            {'x': 6, 'y': 2},
            {'x': 7, 'y': 2},
            {'x': 8, 'y': 2},
            {'x': 9, 'y': 2},
            {'x': 10, 'y': 2},
            {'x': 11, 'y': 2},
            {'x': 12, 'y': 2},
            {'x': 13, 'y': 2},
            {'x': 14, 'y': 2},
            {'x': 15, 'y': 2},
            {'x': 16, 'y': 2},
            {'x': 17, 'y': 2},
            {'x': 18, 'y': 2},
            {'x': 19, 'y': 2}, # open gate in State A!
            {'x': 20, 'y': 2},
            {'x': 21, 'y': 2}, # open gate in State A!
            # Walk DOWN Column 21 past all open gates to Row 18
            {'x': 21, 'y': 3},
            {'x': 21, 'y': 4},
            {'x': 21, 'y': 5}, # open gate in State A!
            {'x': 21, 'y': 6},
            {'x': 21, 'y': 7},
            {'x': 21, 'y': 8}, # open gate in State A!
            {'x': 21, 'y': 9},
            {'x': 21, 'y': 10},
            {'x': 21, 'y': 11},
            {'x': 21, 'y': 12},
            {'x': 21, 'y': 13},
            {'x': 21, 'y': 14},
            {'x': 21, 'y': 15},
            {'x': 21, 'y': 16}, # open balcony gate in State A!
            {'x': 21, 'y': 17},
            {'x': 21, 'y': 18},
            # Walk LEFT Row 18 to Column 19
            {'x': 20, 'y': 18},
            {'x': 19, 'y': 18} # drop tile
        ]
        
        if walk_route(route_on_3f):
            print("Successfully reached balcony drop tile (19, 18)!")
            print("Performing drop step...")
            mgba.press_buttons(["Down"])
            time.sleep(3.0)
            print("Final coordinates after drop:", mgba.get_coordinates())
            mgba.take_screenshot()
        else:
            print("Failed to navigate on 3F.")
            mgba.take_screenshot()
    else:
        print("Failed to reach stairs on 2F West.")
        mgba.take_screenshot()
else:
    print("Failed to reach switch on 2F West.")
    mgba.take_screenshot()
