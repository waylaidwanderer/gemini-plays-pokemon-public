import bridge
import time

# Walk from current position (11, 24) to (6, 20), then to (1, 20), then UP column 1 to search for the Secret House
route = [
    (11, 24),
    (11, 23), (10, 23), (9, 23), (8, 23), (7, 23), (6, 23),
    (6, 22), (6, 21), (6, 20), # Back to (6, 20)
    (5, 20), (4, 20), (3, 20), (2, 20), (1, 20), # LEFT to Column 1
    (1, 19), (1, 18), (1, 17), (1, 16), (1, 15), (1, 14), (1, 13), (1, 12), (1, 11), (1, 10), (1, 9), (1, 8), # UP Column 1 to Row 8
    (2, 8), (3, 8) # RIGHT to Column 3 (potential Secret House door)
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
print(f"Starting Secret House search from {curr}")

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
            # Check if we can interact (maybe we arrived at the Secret House door!)
            print("Trying to press A to enter house...")
            bridge.press_buttons(["A", "sleep 1000"])
            bridge.press_buttons(["B", "sleep 300", "B", "sleep 300"])
            after_a = bridge.get_coordinates()
            if after_a != curr:
                print(f"Successfully entered house or moved! New pos: {after_a}")
                break
                
            run_away()
            after_run = bridge.get_coordinates()
            if after_run != curr:
                print(f"Moved after run sequence! New position: {after_run}")
                for idx, coord in enumerate(route):
                    if after_run == coord:
                        route_idx = idx
                        break
            stuck_count = 0
    else:
        stuck_count = 0

print(f"Finished Secret House search. Final position: {bridge.get_coordinates()}")
