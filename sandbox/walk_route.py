import mgba
import time

# List of target coordinates we want to reach in order.
# Map transitions are handled automatically by checking if current coordinates match the transition destination.
route = [
    # Area 1 (East)
    (12, 7), (12, 6), # UP onto plateau
    (13, 6), (14, 6), (15, 6), (16, 6), (17, 6), # RIGHT along plateau
    (17, 7), (17, 8), # DOWN to ground
    (18, 8), (19, 8), (20, 8), # RIGHT to col 20
    (20, 7), (20, 6), (20, 5), # UP to row 5
    (19, 5), (18, 5), (17, 5), (16, 5), (15, 5), (14, 5), (13, 5), (12, 5),
    (11, 5), (10, 5), (9, 5), (8, 5), (7, 5), (6, 5), (5, 5), (4, 5), (3, 5),
    (2, 5), (1, 5), (0, 5), # LEFT along row 5 (transitions to Area 2 at (39, 31))

    # Area 2 (North)
    (39, 31), # Entry transition confirmation
    (38, 31), (37, 31), (36, 31), (35, 31), (34, 31), (33, 31), (32, 31), (31, 31),
    (30, 31), (29, 31), (28, 31), (27, 31), (26, 31), (25, 31), (24, 31), (23, 31),
    (22, 31), (21, 31), # LEFT along row 31
    (21, 32), (21, 33), (21, 34), (21, 35), (21, 36), # DOWN (transitions to Center at (15, 0))

    # Safari Zone Center
    (15, 0), # Entry transition confirmation
    (15, 1), (15, 2), (15, 3), (15, 4), (15, 5), (15, 6), (15, 7), (15, 8), (15, 9), (15, 10), (15, 11), # DOWN to row 11
    (14, 11), (13, 11), (12, 11), (11, 11), (10, 11), (9, 11), (8, 11), (7, 11), (6, 11), (5, 11), (4, 11),
    (3, 11), (2, 11), (1, 11), (0, 11), # LEFT along row 11 (transitions to Area 3 at (29, 23))

    # Area 3 (West)
    (29, 23), # Entry transition confirmation
    (29, 22), (29, 21), (29, 20), (29, 19), (29, 18), (29, 17), (29, 16), (29, 15), (29, 14), # UP to row 14
    (28, 14), (27, 14), (26, 14), (25, 14), (24, 14), (23, 14), (22, 14), (21, 14), # LEFT to col 21
    (21, 15), (21, 16), (21, 17), (21, 18), # DOWN to row 18
    (21, 17), (21, 16), # UP onto stairs and plateau
    (20, 16), (19, 16), (18, 16), (17, 16), (16, 16), (15, 16), (14, 16), (13, 16), (12, 16),
    (11, 16), (10, 16), (9, 16), (8, 16), (7, 16), (6, 16), # LEFT along plateau
    (6, 17), (6, 18), (6, 19), (6, 20), # DOWN to descend stairs
    (5, 20), (4, 20), (3, 20), (2, 20), (1, 20), # LEFT to col 1
    (1, 19), (1, 18), (1, 17), (1, 16), (1, 15), (1, 14), # UP to row 14
    (2, 14), (3, 14), (4, 14), (5, 14), (6, 14), (7, 14), (8, 14), (9, 14), (10, 14), (11, 14), # RIGHT along row 14
    (11, 13), (11, 12), (11, 11) # UP into Rest House 3
]

def run_away():
    print("Wild battle detected! Attempting to run away...")
    # In Gen 1, pressing B multiple times can dismiss text, and then Down+Right+A selects RUN.
    # To be extremely safe, we send multiple packages of inputs.
    for _ in range(3):
        mgba.press_buttons(["B", "sleep 300"])
    # Navigate to RUN and select
    mgba.press_buttons(["Right", "sleep 200", "Down", "sleep 200", "A", "sleep 1000"])
    # Clear "Got away safely!" text
    for _ in range(4):
        mgba.press_buttons(["B", "sleep 300"])
    print("Run away sequence finished.")

def get_dir(curr, target):
    cx, cy = curr
    tx, ty = target
    if tx > cx: return "Right"
    if tx < cx: return "Left"
    if ty > cy: return "Down"
    if ty < cy: return "Up"
    return None

curr = mgba.get_coordinates()
print(f"Starting at {curr}")

route_idx = 0
# Find where we are in the route
for idx, coord in enumerate(route):
    if curr == coord:
        route_idx = idx
        break

print(f"Matched route index: {route_idx} (Coordinate: {route[route_idx]})")

stuck_count = 0
max_stuck = 3

while route_idx < len(route):
    target = route[route_idx]
    curr = mgba.get_coordinates()
    
    if curr == target:
        print(f"Arrived at target {target} (index {route_idx})")
        route_idx += 1
        stuck_count = 0
        continue
        
    direction = get_dir(curr, target)
    if direction is None:
        # We are at target or we jumped/warped to next map
        # Let's check if we transitioned to the next coordinate on the route
        if route_idx + 1 < len(route):
            next_target = route[route_idx + 1]
            if curr == next_target:
                print(f"Auto-transitioned/Warped to next target {next_target}!")
                route_idx += 2
                stuck_count = 0
                continue
        print(f"Error: Direction is None. Current {curr}, Target {target}. Exiting.")
        break
        
    print(f"Moving {direction} from {curr} towards {target}")
    mgba.press_buttons([direction, "sleep 350"])
    
    new_curr = mgba.get_coordinates()
    if new_curr == curr:
        stuck_count += 1
        print(f"Stuck! Didn't move. Current {curr}, Target {target}. Stuck count: {stuck_count}")
        if stuck_count >= max_stuck:
            # We are stuck, let's assume it's a battle or transition text
            # Try to run away/clear dialog
            run_away()
            # Recheck coordinates
            after_run = mgba.get_coordinates()
            if after_run != curr:
                print(f"Moved after run sequence! New position: {after_run}")
                # See if we matched next route points
                matched = False
                for idx, coord in enumerate(route):
                    if after_run == coord:
                        route_idx = idx
                        print(f"Re-aligned with route at index {route_idx}")
                        matched = True
                        break
                if not matched:
                    print("Could not align after run sequence, exiting.")
                    break
            stuck_count = 0
    else:
        stuck_count = 0
        # Check if we transitioned maps
        # If the coordinate distance is huge, we definitely transitioned!
        dist = abs(new_curr['x'] - curr['x']) + abs(new_curr['y'] - curr['y'])
        if dist > 1:
            print(f"Map Transition detected! Moved from {curr} to {new_curr}")
            # Find new coordinate in route
            matched = False
            for idx, coord in enumerate(route):
                if (new_curr['x'], new_curr['y']) == coord:
                    route_idx = idx
                    print(f"Aligned with route at index {route_idx} after transition")
                    matched = True
                    break
            if not matched:
                print("Transitioned but could not align with route. Exiting.")
                break

print("Finished walking script.")
