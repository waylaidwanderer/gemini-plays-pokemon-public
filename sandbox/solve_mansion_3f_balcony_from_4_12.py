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

# 1. Route to switch at (2, 12) starting from (4, 12)
route_to_switch = [
    {'x': 3, 'y': 12},
    {'x': 2, 'y': 12}
]

print("Walking to switch from (4, 12)...")
if walk_route(route_to_switch):
    print("Reached (2, 12). Toggling Mewtwo switch...")
    # Stand at (2, 12) facing UP to interact with switch at (2, 11)
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    # Perform switch dialogue: 4 A presses with 1.5s delays
    for i in range(4):
        print(f"Pressing A ({i+1}/4)...")
        mgba.press_buttons(["A"])
        time.sleep(1.5)
    
    print("Switch toggled. Walking State A route to balcony...")
    # State A route to balcony starting from (2, 12)
    route_state_a = [
        {'x': 3, 'y': 12},
        {'x': 3, 'y': 11},
        # Right along Row 11 to Column 12
        {'x': 4, 'y': 11},
        {'x': 5, 'y': 11},
        {'x': 6, 'y': 11},
        {'x': 7, 'y': 11},
        {'x': 8, 'y': 11},
        {'x': 9, 'y': 11},
        {'x': 10, 'y': 11},
        {'x': 11, 'y': 11},
        {'x': 12, 'y': 11},
        # Down Column 12 to Row 16
        {'x': 12, 'y': 12},
        {'x': 12, 'y': 13},
        {'x': 12, 'y': 14},
        {'x': 12, 'y': 15},
        {'x': 12, 'y': 16},
        # Right along Row 16 to Column 21
        {'x': 13, 'y': 16},
        {'x': 14, 'y': 16},
        {'x': 15, 'y': 16},
        {'x': 16, 'y': 16},
        {'x': 17, 'y': 16},
        {'x': 18, 'y': 16},
        {'x': 19, 'y': 16},
        {'x': 20, 'y': 16},
        {'x': 21, 'y': 16}, # open balcony gate in State A!
        # Down past open gate to Row 18
        {'x': 21, 'y': 17},
        {'x': 21, 'y': 18},
        # Left along Row 18 to Column 19
        {'x': 20, 'y': 18},
        {'x': 19, 'y': 18} # drop tile
    ]
    
    if walk_route(route_state_a):
        print("Successfully reached balcony drop tile (19, 18)!")
        print("Performing drop step...")
        mgba.press_buttons(["Down"])
        time.sleep(3.0) # wait generously for drop transition and B1F West fade-in
        print("Final coordinates after drop:", mgba.get_coordinates())
        mgba.take_screenshot()
    else:
        print("Failed to navigate to balcony in State A.")
        mgba.take_screenshot()
else:
    print("Failed to reach switch on 3F West.")
    mgba.take_screenshot()
