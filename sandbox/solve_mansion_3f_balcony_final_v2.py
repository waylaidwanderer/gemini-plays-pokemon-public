import mgba
import time
import os

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

# Cleanup obsolete final script if it exists
if os.path.exists('solve_mansion_3f_balcony_final.py'):
    try:
        os.remove('solve_mansion_3f_balcony_final.py')
        print("Cleaned up solve_mansion_3f_balcony_final.py")
    except Exception as e:
        print(f"Failed to remove solve_mansion_3f_balcony_final.py: {e}")

# Perfect State A route to balcony drop (19, 18) starting from (12, 12)
route_to_balcony = [
    # 1. Walk UP Column 12 to Row 11
    {'x': 12, 'y': 11},
    # 2. Walk LEFT along Row 11 to Column 10
    {'x': 11, 'y': 11},
    {'x': 10, 'y': 11},
    # 3. Walk UP Column 10 to Row 6
    {'x': 10, 'y': 10},
    {'x': 10, 'y': 9},
    {'x': 10, 'y': 8},
    {'x': 10, 'y': 7},
    {'x': 10, 'y': 6},
    # 4. Walk RIGHT along Row 6 to Column 17
    {'x': 11, 'y': 6},
    {'x': 12, 'y': 6},
    {'x': 13, 'y': 6},
    {'x': 14, 'y': 6},
    {'x': 15, 'y': 6},
    {'x': 16, 'y': 6},
    {'x': 17, 'y': 6},
    # 5. Walk DOWN Column 17 to Row 11
    {'x': 17, 'y': 7},
    {'x': 17, 'y': 8},
    {'x': 17, 'y': 9},
    {'x': 17, 'y': 10},
    {'x': 17, 'y': 11},
    # 6. Walk RIGHT along Row 11 to Column 21
    {'x': 18, 'y': 11},
    {'x': 19, 'y': 11},
    {'x': 20, 'y': 11},
    {'x': 21, 'y': 11},
    # 7. Walk DOWN Column 21 past open gate to Row 18
    {'x': 21, 'y': 12},
    {'x': 21, 'y': 13},
    {'x': 21, 'y': 14},
    {'x': 21, 'y': 15},
    {'x': 21, 'y': 16}, # open balcony gate in State A!
    {'x': 21, 'y': 17},
    {'x': 21, 'y': 18},
    # 8. Walk LEFT along Row 18 to Column 19
    {'x': 20, 'y': 18},
    {'x': 19, 'y': 18} # drop tile
]

print("Walking perfect State A route to balcony starting from (12, 12)...")
print("Current position:", mgba.get_coordinates())

if walk_route(route_to_balcony):
    print("Successfully reached balcony drop tile (19, 18)!")
    print("Performing drop step...")
    # Step down to drop
    mgba.press_buttons(["Down"])
    time.sleep(3.0) # wait generously for drop transition and B1F West fade-in
    print("Final coordinates after drop:", mgba.get_coordinates())
    mgba.take_screenshot()
else:
    print("Failed to reach balcony drop tile.")
    mgba.take_screenshot()
