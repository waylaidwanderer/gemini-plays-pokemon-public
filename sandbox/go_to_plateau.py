import mgba
import time

route = [
    (11, 14), (10, 14), (9, 14), (8, 14), (7, 14), (6, 14), (5, 14), (4, 14), (3, 14), (2, 14), (1, 14),
    (1, 15), (1, 16), (1, 17), (1, 18), (1, 19), (1, 20),
    (2, 20), (3, 20), (4, 20), (5, 20), (6, 20),
    (6, 19)
]

def run_away():
    print("Wild battle detected! Attempting to run away...")
    for _ in range(3):
        mgba.press_buttons(["B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 200", "Down", "sleep 200", "A", "sleep 1000"])
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
for idx, coord in enumerate(route):
    if curr == coord:
        route_idx = idx + 1
        break

print(f"Target index starting at: {route_idx}")

stuck_count = 0
max_stuck = 3

while route_idx < len(route):
    target = route[route_idx]
    curr = mgba.get_coordinates()
    curr_tup = (curr['x'], curr['y'])
    
    if curr_tup == target:
        print(f"Arrived at target {target} (index {route_idx})")
        route_idx += 1
        stuck_count = 0
        continue
        
    direction = get_dir(curr_tup, target)
    if direction is None:
        print(f"Error: Direction is None. Current {curr_tup}, Target {target}. Exiting.")
        break
        
    print(f"Moving {direction} from {curr_tup} towards {target}")
    mgba.press_buttons([direction, "sleep 350"])
    
    new_curr = mgba.get_coordinates()
    new_curr_tup = (new_curr['x'], new_curr['y'])
    if new_curr_tup == curr_tup:
        stuck_count += 1
        print(f"Stuck! Didn't move. Current {curr_tup}, Target {target}. Stuck count: {stuck_count}")
        if stuck_count >= max_stuck:
            run_away()
            stuck_count = 0
    else:
        stuck_count = 0

print("Finished go_to_plateau.py")
