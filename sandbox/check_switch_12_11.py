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

# Route from (27, 5) on 3F East to Column 12 Row 11 in State B
route_to_12_11 = [
    # Go UP to Row 3
    {'x': 27, 'y': 4},
    {'x': 27, 'y': 3},
    # Left along Row 3 to Column 20
    {'x': 26, 'y': 3},
    {'x': 25, 'y': 3},
    {'x': 24, 'y': 3},
    {'x': 23, 'y': 3},
    {'x': 22, 'y': 3},
    {'x': 21, 'y': 3},
    {'x': 20, 'y': 3},
    # Down through Column 20/19 to Row 6 (bypassing gate at (19, 3))
    {'x': 20, 'y': 4},
    {'x': 19, 'y': 4},
    {'x': 19, 'y': 5},
    {'x': 19, 'y': 6},
    # Left along Row 6 to Column 10
    {'x': 18, 'y': 6},
    {'x': 17, 'y': 6},
    {'x': 16, 'y': 6},
    {'x': 15, 'y': 6},
    {'x': 14, 'y': 6},
    {'x': 13, 'y': 6},
    {'x': 12, 'y': 6},
    {'x': 11, 'y': 6},
    {'x': 10, 'y': 6},
    # Down Column 10 to Row 11
    {'x': 10, 'y': 7},
    {'x': 10, 'y': 8},
    {'x': 10, 'y': 9},
    {'x': 10, 'y': 10},
    {'x': 10, 'y': 11},
    # Walk left along Row 11 to Column 12
    {'x': 9, 'y': 11},
    {'x': 8, 'y': 11},
    {'x': 7, 'y': 11},
    {'x': 6, 'y': 11},
    {'x': 5, 'y': 11},
    {'x': 4, 'y': 11},
    {'x': 3, 'y': 11},
    {'x': 4, 'y': 11},
    {'x': 5, 'y': 11},
    {'x': 6, 'y': 11},
    {'x': 7, 'y': 11},
    {'x': 8, 'y': 11},
    {'x': 9, 'y': 11},
    {'x': 10, 'y': 11},
    {'x': 11, 'y': 11},
    {'x': 12, 'y': 11}
]

print("Walking to (12, 11) to inspect potential switch...")
if walk_route(route_to_12_11):
    print("Successfully reached (12, 11). Checking for switch...")
    # Face UP
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    # Interact
    print("Interacting with (12, 10)...")
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    # Check if there is any dialogue textbox
    mgba.take_screenshot()
else:
    print("Failed to reach (12, 11).")
    mgba.take_screenshot()
