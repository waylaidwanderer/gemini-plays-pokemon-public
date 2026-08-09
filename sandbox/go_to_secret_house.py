import mgba
import time

# Script to walk from (18, 24) to the Secret House at (3, 19) in Safari Zone Area 3 (West)
# It handles wild encounters automatically using run_away().

route = [
    # Start: (18, 24)
    (19, 24),
    (19, 23),
    (20, 23),
    (21, 23),
    (21, 22),
    (21, 21),
    (21, 20),
    (21, 19),
    (21, 18),
    (21, 17), # Climb East Stairs
    (21, 16), # On Plateau
    (20, 16), (19, 16), (18, 16), (17, 16), (16, 16), (15, 16), (14, 16), (13, 16), (12, 16), (11, 16), (10, 16), (9, 16), (8, 16), (7, 16), (6, 16), # Walk West along Plateau
    (6, 17), (6, 18), (6, 19), (6, 20), # Descend West Stairs
    (5, 20), (4, 20), (3, 20), # Walk Left to Column 3
    (3, 19) # UP into Secret House!
]

def run_away():
    print("Wild battle detected! Running away...")
    # In Gen 1, press Down + Right + A to select RUN.
    # We clear text first.
    for _ in range(3):
        mgba.press_buttons(["B", "sleep 300"])
    mgba.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A", "sleep 1000"])
    for _ in range(4):
        mgba.press_buttons(["B", "sleep 300"])
    print("Run away sequence complete.")

def get_dir(curr, target):
    cx, cy = curr['x'], curr['y']
    tx, ty = target[0], target[1]
    if tx > cx: return "Right"
    if tx < cx: return "Left"
    if ty > cy: return "Down"
    if ty < cy: return "Up"
    return None

curr = mgba.get_coordinates()
print(f"Starting at {curr}")

route_idx = 0
for idx, coord in enumerate(route):
    if (curr['x'], curr['y']) == coord:
        route_idx = idx
        break

print(f"Aligned with route at index {route_idx} (Coordinate: {route[route_idx]})")

stuck_count = 0
max_stuck = 2

while route_idx < len(route):
    target = route[route_idx]
    curr = mgba.get_coordinates()
    
    if (curr['x'], curr['y']) == target:
        print(f"Arrived at target {target} (index {route_idx})")
        route_idx += 1
        stuck_count = 0
        continue
        
    direction = get_dir(curr, target)
    if direction is None:
        # Check if we transitioned maps (e.g. entered Secret House)
        # Inside Secret House, our coordinates will change completely or the loop will end.
        print(f"No direction found. We might have entered the Secret House or finished. Current: {curr}")
        break
        
    print(f"Moving {direction} from {curr} towards {target}")
    mgba.press_buttons([direction, "sleep 400"])
    
    new_curr = mgba.get_coordinates()
    if new_curr == curr:
        stuck_count += 1
        print(f"Stuck! Stuck count: {stuck_count}")
        if stuck_count >= max_stuck:
            run_away()
            stuck_count = 0
    else:
        stuck_count = 0

print("Script finished. Current position:", mgba.get_coordinates())
