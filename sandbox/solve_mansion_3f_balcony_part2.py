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

# Route from current position (13, 12) (in battle) to (17, 16) and then balcony
route_to_balcony = [
    # Walk UP Column 13 to Row 6
    {'x': 13, 'y': 11},
    {'x': 13, 'y': 10},
    {'x': 13, 'y': 9},
    {'x': 13, 'y': 8},
    {'x': 13, 'y': 7},
    {'x': 13, 'y': 6},
    # Walk RIGHT along Row 6 to Column 17
    {'x': 14, 'y': 6},
    {'x': 15, 'y': 6},
    {'x': 16, 'y': 6},
    {'x': 17, 'y': 6},
    # Walk DOWN Column 17 to Row 16
    {'x': 17, 'y': 7},
    {'x': 17, 'y': 8},
    {'x': 17, 'y': 9},
    {'x': 17, 'y': 10},
    {'x': 17, 'y': 11},
    {'x': 17, 'y': 12},
    {'x': 17, 'y': 13},
    {'x': 17, 'y': 14},
    {'x': 17, 'y': 15},
    {'x': 17, 'y': 16},
    # Walk RIGHT Row 16 to Column 21
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

print("Escaping battle at (13, 12) and completing balcony navigation via Column 17...")
escape_battle()
print("Position after escape:", mgba.get_coordinates())

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
