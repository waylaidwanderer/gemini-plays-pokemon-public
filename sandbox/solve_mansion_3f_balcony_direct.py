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

print("Escaping active battle at (13, 12)...")
escape_battle()
print("Position after escape:", mgba.get_coordinates())

# 1. Walk from (13, 12) to (3, 6) to check the state of gate (4, 6)
route_to_check = [
    {'x': 13, 'y': 11},
    # Left along Row 11 to Column 3
    {'x': 12, 'y': 11},
    {'x': 11, 'y': 11},
    {'x': 10, 'y': 11},
    {'x': 9, 'y': 11},
    {'x': 8, 'y': 11},
    {'x': 7, 'y': 11},
    {'x': 6, 'y': 11},
    {'x': 5, 'y': 11},
    {'x': 4, 'y': 11},
    {'x': 3, 'y': 11},
    # Up Column 3 to (3, 6)
    {'x': 3, 'y': 10},
    {'x': 3, 'y': 9},
    {'x': 3, 'y': 8},
    {'x': 3, 'y': 7},
    {'x': 3, 'y': 6}
]

print("1. Walking to verification tile (3, 6)...")
if not walk_route(route_to_check):
    print("Failed to reach verification tile.")
    mgba.take_screenshot()
    exit(1)

# Test gate at (4, 6)
print("Testing gate (4, 6) state...")
curr = mgba.get_coordinates()
mgba.press_buttons(["Right"])
time.sleep(0.5)
pos = mgba.get_coordinates()

need_toggle = False
if pos == {'x': 4, 'y': 6}:
    print("Gate (4, 6) is OPEN -> Mansion is in STATE B.")
    need_toggle = True
    # Step back Left to (3, 6)
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
else:
    print("Gate (4, 6) is CLOSED -> Mansion is in STATE A.")

if need_toggle:
    # Walk down Column 3 to switch standing position (3, 11)
    route_to_switch = [
        {'x': 3, 'y': 7},
        {'x': 3, 'y': 8},
        {'x': 3, 'y': 9},
        {'x': 3, 'y': 10},
        {'x': 3, 'y': 11}
    ]
    print("Walking down to switch stand (3, 11)...")
    walk_route(route_to_switch)
    
    # Face LEFT and toggle switch to State A
    print("Facing LEFT and toggling Mewtwo Switch...")
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
    mgba.press_buttons(["A"]) # "A secret switch!"
    time.sleep(1.5)
    mgba.press_buttons(["A"]) # "Press it?" YES/NO
    time.sleep(1.5)
    mgba.press_buttons(["A"]) # Confirm YES
    time.sleep(1.5)
    mgba.press_buttons(["A"]) # "Who wouldn't?" (Closes dialogue)
    time.sleep(2.0)
    print("Mansion is now globally in STATE A!")

# 2. Walk to (3, 11) if we aren't already there
walk_route([{'x': 3, 'y': 11}])

# 3. Walk the direct State A route to the balcony drop at (19, 18)
route_to_balcony = [
    # Walk RIGHT along Row 11 to Column 12
    {'x': 4, 'y': 11},
    {'x': 5, 'y': 11},
    {'x': 6, 'y': 11},
    {'x': 7, 'y': 11},
    {'x': 8, 'y': 11},
    {'x': 9, 'y': 11},
    {'x': 10, 'y': 11},
    {'x': 11, 'y': 11},
    {'x': 12, 'y': 11},
    # Walk DOWN Column 12 to Row 16 (open in State A!)
    {'x': 12, 'y': 12},
    {'x': 12, 'y': 13},
    {'x': 12, 'y': 14},
    {'x': 12, 'y': 15},
    {'x': 12, 'y': 16},
    # Walk RIGHT Row 16 to Column 21
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

print("3. Navigating 3F in State A directly to balcony drop tile (19, 18)...")
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
