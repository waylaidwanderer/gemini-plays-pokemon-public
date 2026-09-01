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

# Route from current position (19, 5) directly to pitfall trap at (26, 3) in State B via southern route
route_to_pitfall = [
    # Walk DOWN Column 19 to Row 16
    {'x': 19, 'y': 6},
    {'x': 19, 'y': 7},
    {'x': 19, 'y': 8},
    {'x': 19, 'y': 9},
    {'x': 19, 'y': 10},
    {'x': 19, 'y': 11},
    {'x': 19, 'y': 12},
    {'x': 19, 'y': 13}, # open in State B
    {'x': 19, 'y': 14},
    {'x': 19, 'y': 15},
    {'x': 19, 'y': 16},
    # Walk RIGHT along Row 16 to Column 24
    {'x': 20, 'y': 16},
    {'x': 21, 'y': 16},
    {'x': 22, 'y': 16},
    {'x': 23, 'y': 16},
    {'x': 24, 'y': 16},
    # Walk UP Column 24 to Row 12
    {'x': 24, 'y': 15},
    {'x': 24, 'y': 14},
    {'x': 24, 'y': 13},
    {'x': 24, 'y': 12},
    # Walk RIGHT along Row 12 to Column 26
    {'x': 25, 'y': 12},
    {'x': 26, 'y': 12},
    # Walk UP Column 26 to Row 3
    {'x': 26, 'y': 11},
    {'x': 26, 'y': 10},
    {'x': 26, 'y': 9},
    {'x': 26, 'y': 8},
    {'x': 26, 'y': 7},
    {'x': 26, 'y': 6},
    {'x': 26, 'y': 5},
    {'x': 26, 'y': 4},
    {'x': 26, 'y': 3} # pitfall tile!
]

print("Walking from (19, 5) to pitfall trap (26, 3) on 3F East in State B via Row 16/Column 24...")
print("Current position:", mgba.get_coordinates())

if walk_route(route_to_pitfall):
    print("Successfully reached pitfall tile (26, 3)!")
    print("Performing fall step...")
    # Step down onto pitfall
    mgba.press_buttons(["Down"])
    time.sleep(3.0) # wait generously for fall transition and fade-in to 1F East
    print("Coordinates after fall onto 1F East fenced room:", mgba.get_coordinates())
    mgba.take_screenshot()
else:
    print("Failed to reach pitfall.")
    mgba.take_screenshot()
