import mgba
import time

# Total steps remaining tracker (rough)
steps_taken = 0

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def run_away():
    print("Wild battle detected! Running away...")
    # Gen 1 battle escape
    for _ in range(4):
        mgba.press_buttons(["B", "sleep 300"])
    # Press Down, Right, A to RUN
    mgba.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A", "sleep 1500"])
    # Clear escape message
    for _ in range(4):
        mgba.press_buttons(["B", "sleep 300"])

# The route back to Center via the plateau
route = [
    # 1. Walk LEFT to (6, 23)
    (16, 23), (15, 23), (14, 23), (13, 23), (12, 23), (11, 23), (10, 23), (9, 23), (8, 23), (7, 23), (6, 23),
    # 2. Walk UP to (6, 18) (climbing stairs at 6, 19)
    (6, 22), (6, 21), (6, 20), (6, 19), (6, 18),
    # 3. Walk EAST along plateau to (21, 16)
    (7, 18), # wait, the plateau is on Row 16 or 18?
    # Let's check the route of walk_route.py for the plateau:
    # "plateau is on Row 16: (20, 16), (19, 16)... (6, 16)"
    # Ah! From (6, 20), we walked UP to (6, 16) to climb onto the plateau!
    # Let's check:
    # (6, 20) -> (6, 19) -> (6, 18) -> (6, 17) -> (6, 16)
    # Yes! Let's correct this:
]

# Let's write the route extremely carefully based on walk_route.py's coordinates:
# From walk_route.py:
# (21, 17), (21, 16), # UP onto stairs and plateau
# (20, 16) ... (6, 16) # LEFT along plateau
# (6, 17), (6, 18), (6, 19), (6, 20) # DOWN to descend stairs
# So descending was: (6, 16) -> (6, 17) -> (6, 18) -> (6, 19) -> (6, 20).
# Therefore, ascending is: (6, 20) -> (6, 19) -> (6, 18) -> (6, 17) -> (6, 16).
# Let's map the full sequence of targets:

targets = [
    # Walk left to (6, 23)
    (16, 23), (15, 23), (14, 23), (13, 23), (12, 23), (11, 23), (10, 23), (9, 23), (8, 23), (7, 23), (6, 23),
    # Walk up to (6, 16) to climb stairs onto plateau
    (6, 22), (6, 21), (6, 20), (6, 19), (6, 18), (6, 17), (6, 16),
    # Walk east along plateau to (21, 16)
    (7, 16), (8, 16), (9, 16), (10, 16), (11, 16), (12, 16), (13, 16), (14, 16), (15, 16), (16, 16), (17, 16), (18, 16), (19, 16), (20, 16), (21, 16),
    # Descend stairs to (21, 18)
    (21, 17), (21, 18),
    # Walk east to (29, 18)
    (22, 18), (23, 18), (24, 18), (25, 18), (26, 18), (27, 18), (28, 18), (29, 18),
    # Walk down to (29, 23)
    (29, 19), (29, 20), (29, 21), (29, 22), (29, 23),
    # Walk right to transition
    (30, 23) # This will transition us to Center at (0, 11)
]

def get_dir(curr, target):
    cx, cy = curr
    tx, ty = target
    if tx > cx: return "Right"
    if tx < cx: return "Left"
    if ty > cy: return "Down"
    if ty < cy: return "Up"
    return None

print("Starting walk_to_center_via_plateau.py...")
route_idx = 0

# Recheck where we are in targets
curr = get_pos()
for idx, coord in enumerate(targets):
    if curr == coord:
        route_idx = idx
        break

print(f"Start: {curr}, Matched target index: {route_idx}")

stuck_count = 0
max_stuck = 3

while route_idx < len(targets):
    target = targets[route_idx]
    curr = get_pos()
    
    if curr == target:
        print(f"Arrived at target {target} (index {route_idx})")
        route_idx += 1
        stuck_count = 0
        continue
        
    direction = get_dir(curr, target)
    if direction is None:
        # Check if we transitioned to next map
        if curr[0] == 0: # Safari Zone Center column 0
            print(f"Successfully transitioned to Center! Current position: {curr}")
            break
        print(f"Error: No direction from {curr} to {target}. Exiting.")
        break
        
    print(f"Moving {direction} from {curr} towards {target}")
    mgba.press_buttons([direction, "sleep 350"])
    steps_taken += 1
    
    new_curr = get_pos()
    if new_curr == curr:
        stuck_count += 1
        print(f"Stuck! Didn't move. Count: {stuck_count}")
        if stuck_count >= max_stuck:
            run_away()
            # clear any remaining text
            mgba.press_buttons(["B", "sleep 200"])
            stuck_count = 0
    else:
        stuck_count = 0
        # If the position changed significantly, we probably transitioned!
        dist = abs(new_curr[0] - curr[0]) + abs(new_curr[1] - curr[1])
        if dist > 1:
            print(f"Transition detected! Moved from {curr} to {new_curr}")
            if new_curr[0] == 0: # Safari Zone Center
                print("Transitioned to Center!")
                break
            # Otherwise try to realign
            for idx, coord in enumerate(targets):
                if new_curr == coord:
                    route_idx = idx
                    print(f"Realigned with targets at index {route_idx}")
                    break

print("Finished walking back to Center.")
