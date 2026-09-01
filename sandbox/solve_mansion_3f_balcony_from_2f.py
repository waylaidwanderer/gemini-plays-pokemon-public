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

# 1. Walk from (3, 11) on 3F West to stairs at (5, 10) to warp DOWN to 2F West
route_to_warp = [
    {'x': 4, 'y': 11},
    {'x': 5, 'y': 11},
    {'x': 5, 'y': 10} # stairs
]

print("1. Walking to stairs (5, 10) on 3F West...")
if not walk_route(route_to_warp):
    print("Failed to reach stairs.")
    mgba.take_screenshot()
    exit(1)

print("Warping DOWN to 2F West...")
time.sleep(3.0) # wait generously for floor transition fade
print("Coordinates after warp DOWN:", mgba.get_coordinates())

# 2. Walk UP Column 5 (open in State A) to Row 2, and across Row 2 to 2F East stairs at (22, 1)
route_to_stairs = [
    # Walk UP Column 5 to Row 2
    {'x': 5, 'y': 9},
    {'x': 5, 'y': 8},
    {'x': 5, 'y': 7},
    {'x': 5, 'y': 6},
    {'x': 5, 'y': 5},
    {'x': 5, 'y': 4},
    {'x': 5, 'y': 3},
    {'x': 5, 'y': 2},
    # Walk RIGHT along Row 2 to Column 22
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
    {'x': 19, 'y': 2},
    {'x': 20, 'y': 2},
    {'x': 21, 'y': 2},
    {'x': 22, 'y': 2},
    # Step UP onto northeast stairs at (22, 1) to warp to 3F East
    {'x': 22, 'y': 1}
]

print("2. Walking 2F West-to-East in State A to northeast stairs...")
if not walk_route(route_to_stairs):
    print("Failed to reach northeast stairs.")
    mgba.take_screenshot()
    exit(1)

print("Warping UP to 3F East...")
time.sleep(3.0) # wait generously for floor transition fade

# 3. Walk down Column 21 to balcony on 3F East and drop!
route_to_balcony = [
    {'x': 21, 'y': 1},
    {'x': 21, 'y': 2},
    {'x': 21, 'y': 3},
    {'x': 21, 'y': 4},
    {'x': 21, 'y': 5},
    {'x': 21, 'y': 6},
    {'x': 21, 'y': 7},
    {'x': 21, 'y': 8},
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
    # Left along Row 18 to Column 19
    {'x': 20, 'y': 18},
    {'x': 19, 'y': 18} # drop tile
]

print("3. Navigating 3F East to balcony drop tile (19, 18)...")
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
