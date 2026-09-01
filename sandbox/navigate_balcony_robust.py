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

def move_to(target_x, target_y):
    # Attempt to move to an adjacent target tile. Handles battles and recalculations.
    for attempt in range(3):
        curr = mgba.get_coordinates()
        if curr == {'x': target_x, 'y': target_y}:
            return True
            
        dx = target_x - curr['x']
        dy = target_y - curr['y']
        
        if abs(dx) + abs(dy) != 1:
            print(f"Non-adjacent! Current: {curr}, Target: ({target_x}, {target_y}). Attempting to recover...")
            # If we are not adjacent, we might have been moved by a battle.
            # Try to escape battle first in case one is active
            escape_battle()
            time.sleep(2.0)
            curr = mgba.get_coordinates()
            if curr == {'x': target_x, 'y': target_y}:
                return True
            # Recalculate dx, dy
            dx = target_x - curr['x']
            dy = target_y - curr['y']
            if abs(dx) + abs(dy) != 1:
                print(f"Still non-adjacent after recovery check: {curr}")
                return False
            
        if dx == 1: direction = "Right"
        elif dx == -1: direction = "Left"
        elif dy == 1: direction = "Down"
        elif dy == -1: direction = "Up"
        
        print(f"Step Attempt {attempt+1}: Stepping {direction} from {curr} to ({target_x}, {target_y})...")
        mgba.press_buttons([direction])
        time.sleep(0.4)
        
        new_pos = mgba.get_coordinates()
        if new_pos == {'x': target_x, 'y': target_y}:
            return True
            
        print(f"Failed to reach target. Position is {new_pos}. Attempting escape...")
        escape_battle()
        time.sleep(2.0) # wait for overworld to reload
        
    return False

def walk_route(route_coords):
    for target in route_coords:
        # Dynamic check of adjacency. If we are far from the target, find a way back!
        curr = mgba.get_coordinates()
        if curr == target:
            continue
        
        # If we got misaligned, recalculate the local path to target!
        # Since target is on our highway, we can easily go UP to Row 2, then to target's column, then DOWN to target!
        dx = target['x'] - curr['x']
        dy = target['y'] - curr['y']
        if abs(dx) + abs(dy) != 1:
            print(f"Misalignment detected! Current: {curr}, Target: {target}. Recalculating via Row 2 highway...")
            # Generate highway route to target:
            highway_recovery = []
            # 1. UP to Row 2
            for y in range(curr['y'] - 1, 1, -1):
                highway_recovery.append({'x': curr['x'], 'y': y})
            # 2. Horizontal to target's column on Row 2
            step_x = 1 if target['x'] > curr['x'] else -1
            for x in range(curr['x'] + step_x, target['x'] + step_x, step_x):
                highway_recovery.append({'x': x, 'y': 2})
            # 3. DOWN to target's row
            for y in range(3, target['y'] + 1):
                highway_recovery.append({'x': target['x'], 'y': y})
                
            print(f"Recovery route: {highway_recovery}")
            if not walk_route(highway_recovery):
                print("Highway recovery failed.")
                return False
                
        # Now we are adjacent (or at target), execute the step
        curr = mgba.get_coordinates()
        if curr == target:
            continue
        if not move_to(target['x'], target['y']):
            print(f"Fatal: Failed to reach coordinate {target}")
            return False
        print(f"Successfully reached {target}")
    return True

# 1. Target switch route from current (5, 3)
# We can walk: (5, 3) -> (5, 2) -> (2, 2) -> (2, 6)
route_to_switch = [
    {'x': 5, 'y': 2},
    {'x': 4, 'y': 2}, {'x': 3, 'y': 2}, {'x': 2, 'y': 2},
    {'x': 2, 'y': 3}, {'x': 2, 'y': 4}, {'x': 2, 'y': 5}, {'x': 2, 'y': 6}
]

# 2. Route from (2, 6) to stairs at (5, 10) in State A
route_to_stairs = [
    {'x': 2, 'y': 5}, {'x': 2, 'y': 4}, {'x': 2, 'y': 3}, {'x': 2, 'y': 2},
    {'x': 3, 'y': 2}, {'x': 4, 'y': 2}, {'x': 5, 'y': 2},
    {'x': 5, 'y': 3}, {'x': 5, 'y': 4}, {'x': 5, 'y': 5}, {'x': 5, 'y': 6}, {'x': 5, 'y': 7}, {'x': 5, 'y': 8}, {'x': 5, 'y': 9}, {'x': 5, 'y': 10}
]

# 3. Route from (5, 11) to balcony drop (19, 18) on 3F in State A
route_to_balcony = [
    {'x': 6, 'y': 11}, {'x': 7, 'y': 11}, {'x': 8, 'y': 11}, {'x': 9, 'y': 11}, {'x': 10, 'y': 11}, {'x': 11, 'y': 11}, {'x': 12, 'y': 11},
    {'x': 12, 'y': 12}, {'x': 12, 'y': 13}, {'x': 12, 'y': 14}, {'x': 12, 'y': 15}, {'x': 12, 'y': 16},
    {'x': 13, 'y': 16}, {'x': 14, 'y': 16}, {'x': 15, 'y': 16}, {'x': 16, 'y': 16}, {'x': 17, 'y': 16}, {'x': 18, 'y': 16}, {'x': 19, 'y': 16}, {'x': 20, 'y': 16}, {'x': 21, 'y': 16},
    {'x': 21, 'y': 17}, {'x': 21, 'y': 18},
    {'x': 20, 'y': 18}, {'x': 19, 'y': 18}
]

print("Starting ultra-robust overworld traversal to balcony drop...")
print("Current Position:", mgba.get_coordinates())

print("Step 1: Walking to the Mewtwo Statue Switch at (2, 5) from current position...")
if walk_route(route_to_switch):
    print("Reached (2, 6) successfully! Facing UP to face the switch...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)

    # Toggle the switch to State A
    for i in range(1, 5):
        print(f"A-press {i}/4...")
        mgba.press_buttons(["A"])
        time.sleep(1.5)

    print("Switch toggled successfully to State A! Step 2: Walking to stairs at (5, 10)...")
    if walk_route(route_to_stairs):
        print("Warping to 3F West...")
        time.sleep(2.0) # wait for warp loading
        pos = mgba.get_coordinates()
        print("Landing position on 3F West:", pos)

        if pos == {'x': 5, 'y': 11}:
            print("Step 3: Navigating to balcony drop at (19, 18) on 3F in State A...")
            if walk_route(route_to_balcony):
                print("Executed balcony drop successfully!")
                time.sleep(2.0) # wait for drop transition
                print("Final landing position on B1F West:", mgba.get_coordinates())
            else:
                print("Interrupted on 3F route to balcony.")
        else:
            print("Landing position is not (5, 11). Current position:", pos)
    else:
        print("Failed to reach 2F stairs.")
else:
    print("Failed to reach 2F switch.")
