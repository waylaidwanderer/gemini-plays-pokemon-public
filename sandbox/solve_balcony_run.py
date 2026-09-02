import mgba
import time

def escape_battle():
    print("Wild encounter detected! Dismissing text and running away...")
    # First press B multiple times with sleep to clear initial text
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.3)
    
    # Press Down to select RUN
    mgba.press_buttons(["Down"])
    time.sleep(0.3)
    # Press Right to make sure cursor is on RUN
    mgba.press_buttons(["Right"])
    time.sleep(0.3)
    # Press A to confirm RUN
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    
    # Press B to dismiss the escape text
    for _ in range(3):
        mgba.press_buttons(["B"])
        time.sleep(0.3)
    print("Escape attempt finished. Resuming overworld navigation.")

def step(direction):
    current = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.6)
    next_pos = mgba.get_coordinates()
    
    # If coordinate didn't change, we might be blocked by a battle
    if next_pos == current:
        print(f"Blocked at {current}. Attempting battle escape...")
        escape_battle()
        time.sleep(1.5)
        # Try stepping again
        mgba.press_buttons([direction])
        time.sleep(0.6)
        next_pos = mgba.get_coordinates()
    return next_pos

def walk_route(route_coords):
    i = 0
    while i < len(route_coords):
        target = route_coords[i]
        curr = mgba.get_coordinates()
        if curr == target:
            print(f"Already at target index {i}: {target}")
            i += 1
            continue
            
        dx = target['x'] - curr['x']
        dy = target['y'] - curr['y']
        
        if abs(dx) + abs(dy) == 1:
            if dx == 1:
                direction = 'Right'
            elif dx == -1:
                direction = 'Left'
            elif dy == 1:
                direction = 'Down'
            else:
                direction = 'Up'
                
            print(f"Moving {direction} towards target {target}...")
            res = step(direction)
            if res == target or (i < len(route_coords)-1 and res == route_coords[i+1]):
                print(f"Reached {res}")
                if res == route_coords[i+1]:
                    i += 2
                else:
                    i += 1
            else:
                print(f"Failed to reach target {target}. Actual position: {res}. Retrying...")
                time.sleep(0.5)
        else:
            print(f"Displaced! Current: {curr}, Target: {target}. Attempting recovery...")
            found = False
            for idx, coord in enumerate(route_coords):
                if coord == curr:
                    print(f"Found current position {curr} in route at index {idx}. Resuming from there.")
                    i = idx + 1
                    found = True
                    break
            if not found:
                # Find the closest adjacent route tile to recover
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
                    if pdx == 1: pdir = 'Right'
                    elif pdx == -1: pdir = 'Left'
                    elif pdy == 1: pdir = 'Down'
                    else: pdir = 'Up'
                    print(f"Found adjacent route tile {target_coord} (index {best_idx}). Walking to it...")
                    res = step(pdir)
                    if res == target_coord:
                        i = best_idx + 1
                else:
                    print("Could not find adjacent route tile for recovery.")
                    return False
    return True

# Build complete route from current (12, 9)
route_to_balcony = [
    {'x': 12, 'y': 9},
    {'x': 12, 'y': 10},
    {'x': 12, 'y': 11},
    {'x': 11, 'y': 11},
    {'x': 10, 'y': 11},
    {'x': 10, 'y': 10},
    {'x': 10, 'y': 9},
    {'x': 10, 'y': 8},
    {'x': 10, 'y': 7},
    {'x': 10, 'y': 6},
    {'x': 11, 'y': 6},
    {'x': 12, 'y': 6},
    {'x': 13, 'y': 6},
    {'x': 14, 'y': 6},
    {'x': 15, 'y': 6},
    {'x': 16, 'y': 6},
    {'x': 17, 'y': 6},
    {'x': 18, 'y': 6},
    {'x': 19, 'y': 6},
    {'x': 19, 'y': 5},
    {'x': 19, 'y': 4},
    {'x': 20, 'y': 4},
    {'x': 20, 'y': 3},
    {'x': 21, 'y': 3},
    {'x': 22, 'y': 3},
    {'x': 23, 'y': 3},
    {'x': 24, 'y': 3},
    {'x': 25, 'y': 3},
    {'x': 26, 'y': 3}, # Pitfall tile on 3F
    
    # 2F East landing and path to balcony
    {'x': 26, 'y': 4},
    {'x': 26, 'y': 5},
    {'x': 26, 'y': 6},
    {'x': 26, 'y': 7},
    {'x': 26, 'y': 8},
    {'x': 26, 'y': 9},
    {'x': 26, 'y': 10},
    {'x': 26, 'y': 11},
    {'x': 26, 'y': 12},
    {'x': 25, 'y': 12},
    {'x': 24, 'y': 12},
    {'x': 24, 'y': 13},
    {'x': 24, 'y': 14},
    {'x': 24, 'y': 15},
    {'x': 24, 'y': 16},
    {'x': 23, 'y': 16},
    {'x': 22, 'y': 16},
    {'x': 21, 'y': 16}, # Balcony door on 2F (open in State A)
    {'x': 21, 'y': 17},
    {'x': 21, 'y': 18},
    {'x': 20, 'y': 18},
    {'x': 19, 'y': 18}  # Balcony drop tile on 2F
]

print("Starting State A route to balcony...")
print(f"Current position: {mgba.get_coordinates()}")

success = walk_route(route_to_balcony)
if success:
    print("Reached balcony drop tile (19, 18). Performing drop step...")
    mgba.press_buttons(["Down"])
    time.sleep(3.0)
    print(f"Coordinates after drop: {mgba.get_coordinates()}")
    mgba.take_screenshot()
else:
    print("Failed to reach balcony drop tile.")
    mgba.take_screenshot()
