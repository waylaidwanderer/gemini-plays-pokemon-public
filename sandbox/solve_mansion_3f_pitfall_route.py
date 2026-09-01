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

# Absolute open route in State B starting from current position (17, 7)
route_to_pitfall = [
    # 1. Walk RIGHT to Column 18
    {'x': 18, 'y': 7},
    # 2. Walk UP Column 18 to Row 4
    {'x': 18, 'y': 6},
    {'x': 18, 'y': 5},
    {'x': 18, 'y': 4},
    # 3. Walk RIGHT along Row 4 to Column 21
    {'x': 19, 'y': 4},
    {'x': 20, 'y': 4},
    {'x': 21, 'y': 4},
    # 4. Walk UP Column 21 to Row 3
    {'x': 21, 'y': 3},
    # 5. Walk RIGHT along Row 3 to Column 26
    {'x': 22, 'y': 3},
    {'x': 23, 'y': 3},
    {'x': 24, 'y': 3},
    {'x': 25, 'y': 3},
    {'x': 26, 'y': 3} # pitfall tile!
]

print("Walking perfect State B route to 3F East pitfall starting from (17, 7)...")
print("Current position:", mgba.get_coordinates())

if walk_route(route_to_pitfall):
    print("Reached (26, 3)! Attempting to step into the pitfall...")
    # Step down to fall into the pitfall
    mgba.press_buttons(["Down"])
    time.sleep(3.0) # wait generously for falling transition and 1F East fade-in
    print("Coordinates after falling:", mgba.get_coordinates())
    mgba.take_screenshot()
else:
    print("Failed to reach pitfall tile.")
    mgba.take_screenshot()
