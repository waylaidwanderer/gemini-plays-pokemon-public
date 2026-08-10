import bridge
import time

# Walk back to west stairs at (6, 20), go left to (1, 20), and test walking DOWN Column 1 as far as possible!
route = [
    (15, 24),
    (15, 23), (14, 23), (13, 23), (12, 23), (11, 23), (10, 23), (9, 23), (8, 23), (7, 23), (6, 23),
    (6, 22), (6, 21), (6, 20), # Back to (6, 20)
    (5, 20), (4, 20), (3, 20), (2, 20), (1, 20) # LEFT to Column 1
]

def get_dir(curr, target):
    cx, cy = curr
    tx, ty = target
    if tx > cx: return "Right"
    if tx < cx: return "Left"
    if ty > cy: return "Down"
    if ty < cy: return "Up"
    return None

def run_away():
    print("Wild battle/interaction detected! Executing RUN sequence...")
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 300"])
    bridge.press_buttons(["Right", "sleep 200", "Down", "sleep 200", "A", "sleep 1200"])
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 300"])
    print("RUN sequence finished.")

curr = bridge.get_coordinates()
print(f"Starting West Side test at {curr}")

route_idx = 0
for idx, coord in enumerate(route):
    if curr == coord:
        route_idx = idx
        break

print(f"Matched route index: {route_idx}")

stuck_count = 0
max_stuck = 3

while route_idx < len(route):
    target = route[route_idx]
    curr = bridge.get_coordinates()
    
    if curr == target:
        print(f"Arrived at target {target} (index {route_idx})")
        route_idx += 1
        stuck_count = 0
        continue
        
    direction = get_dir(curr, target)
    if direction is None:
        print(f"Error: Direction is None. Current {curr}, Target {target}. Exiting.")
        break
        
    print(f"Moving {direction} from {curr} towards {target}")
    bridge.press_buttons([direction, "sleep 300"])
    
    new_curr = bridge.get_coordinates()
    if new_curr == curr:
        stuck_count += 1
        print(f"Stuck! Stuck count: {stuck_count}")
        if stuck_count >= max_stuck:
            run_away()
            after_run = bridge.get_coordinates()
            if after_run != curr:
                print(f"Moved after run sequence! New position: {after_run}")
                for idx, coord in enumerate(route):
                    if after_run == coord:
                        route_idx = idx
                        print(f"Re-aligned with route at index {route_idx}")
                        break
            stuck_count = 0
    else:
        stuck_count = 0

print(f"Arrived at (1, 20). Current: {bridge.get_coordinates()}")

# Now test walking DOWN Column 1 as far as possible!
curr = bridge.get_coordinates()
for y in range(21, 29):
    print(f"Trying to move Down from {curr} towards (1, {y})...")
    bridge.press_buttons(["Down", "sleep 300"])
    new_curr = bridge.get_coordinates()
    print(f"Now at {new_curr}")
    if new_curr == curr:
        print(f"Blocked walking DOWN Column 1 at {curr}!")
        break
    curr = new_curr

print(f"West side exploration finished. Final position: {bridge.get_coordinates()}")
